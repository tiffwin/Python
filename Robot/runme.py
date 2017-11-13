from __future__ import print_function
from __future__ import division

import easygopigo3
import signal
import speech

from time import sleep

class Robot(object):
	def __init__(self):
		self.robot = EasyGoPiGo3()

	def command_forward(self):
		self.robot.forward()

	def command_backward(self):
		self.robot.backward()

	def command_left(self):
		self.robot.left()

	def command_right(self):
		self.robot.right()

	def command_stop(self):
		self.robot.stop()


def Main():
	
	robotCar = Robot()

	while True:
		command = speech.run()

		if command == 'go':
			robotCar.command_forward()

		elif command == 'back':
			robotCar.command_backward()

		elif command == 'left':
			robotCar.command_left()

		elif command == 'right':
			robotCar.command_right()

		else:
			continue


if __name__ == "__main__":
    # set up a handler for ignoring the Ctrl+Z commands
    signal.signal(signal.SIGTSTP, lambda signum, frame : print("Press the appropriate key for closing the app."))

    try:
        Main()
    except IOError as error:
        # if the GoPiGo3 is not reachable
        # then print the error and exit
        print(str(error))
        exit(1)

    exit(0)