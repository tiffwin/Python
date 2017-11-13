from __future__ import print_function
from __future__ import division

from easygopigo3 import EasyGoPiGo3
import signal
import speech

from time import sleep


def Main():
	
	robotCar = EasyGoPiGo3()

	while True:

		command = speech.run()

		if command == 'go':
			print(command)
			robotCar.forward()

		elif command == 'back':
			print(command)
			robotCar.backward()

		elif command == 'left':
			print(command)
			robotCar.left()

		elif command == 'right':
			print(command)
			robotCar.right()
		
		elif command == 'stop':
			print(command)
			robotCar.stop()

		elif command == 'quit':
			print(command)
			robotCar.stop()
			break

		else:
			print("No command heard")
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