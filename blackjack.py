from __future__ import print_function
from builtins import input
from random import shuffle

class Player(object):
	def __init__(self,bankroll):
		self.bankroll = bankroll

class Deck(object):
	def __init__(self):
		self.cards = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']*4

	def shuffle(self):
		return shuffle(self.cards)

	def dealCard(self):
		return self.cards.pop(0)

def check_hand(cards):
	value = 0
	ace = False

	for i in cards:
		if i == '10' or i == 'J' or i == 'Q' or i == 'K':
			value += 10
		elif i == '9' or i == '8' or i == '7' or i == '6' or i == '5' or i == '4' or i == '3' or i == '2':
			value += int(i)
		elif i == 'A' and ace == False:
			ace == True
		elif i == 'A' and ace == True:
			value +=1

	if ace == True:
		if value <= 10:
			value += 11
		else:
			value += 1

	#FOR BUG CHECKING
	print ("Cards total value: " , value)
	return value

def play():
	player = Player(100)

	print('')
	print('******************************')
	print('Welcome to the Blackjack Game!')
	print('******************************\n')
	print('Your chips: ', player.bankroll, '\n')

	while player.bankroll > 0:
		start_game(player)

	if player.bankroll <= 0:
		if input('No more money! Play again? (Y/N').upper() == 'Y':
			play()

def start_game(player):
	while True:
		try:
			bet = int(input('Enter bet amount: '))
			
			if bet > player.bankroll:
				print("You don't have that much money.\n")
			elif bet <= 0:
				print ("You need to enter a positive amount.\n")
			else:
				print ('Bet placed:', bet, '\n')
				break
		except:
			print("You need to enter a number.\n")
			continue

	player.bankroll -= bet
	print("Money in pocket: ", player.bankroll, '\n')

	#Start the game
	print("Starting game...\n")

	#Shuffles new deck
	deck = Deck()
	deck.shuffle()

	player_cards = []
	dealer_cards = []
	
	#Deals card to player, then dealer, then player, then dealer
	player_cards.append(deck.dealCard())
	dealer_cards.append(deck.dealCard())
	player_cards.append(deck.dealCard())
	dealer_cards.append(deck.dealCard())

	print("Dealer's hand: ", dealer_cards)
	print("Your hand: ", player_cards, '\n') 

	while True:
		if check_hand(player_cards) == 21:
			break

		player_choice = input('Stand(S) or Hit(H)? \n')

		if player_choice.upper() == 'S':
			print("I stand!\n")
			break

		if player_choice.upper() == 'H':
			print("HIT ME!\n")

			player_cards.append(deck.dealCard())
			print("Dealer's hand: ", dealer_cards)
			print("Your hand: ", player_cards, '\n') 

			#Checks if player's hand has busted
			if check_hand(player_cards) > 21:
				print("Busted! \n")
				print("Your chips: ", player.bankroll)
			else:
				continue
		else:
			continue
	
	while check_hand(dealer_cards) < 17:
		dealer_cards.append(deck.dealCard())
		print("Dealer's hand: ", dealer_cards)
		print("Your hand: ", player_cards, '\n') 


	if check_hand(dealer_cards) > 21:
		print("Dealer busted, you win! \n")
		player.bankroll += bet*2
		print("You won: ", bet*2)
		print("Your chips:", player.bankroll, '\n')
	
	elif check_hand(dealer_cards) == check_hand(player_cards):
		print("It's a tie! Your bet is being returned to you. \n")

	elif check_hand(player_cards) == 21:
		print("You've hit Blackjack! \n")
		player.bankroll += bet*2
		print("You won: ", bet*2, '\n')

	elif check_hand(dealer_cards) == 21:
		print("Dealer blackjack! \n")

	elif check_hand(dealer_cards) > check_hand(player_cards):
		print("Dealer wins! \n")

	else:
		print("You win! \n")
		player.bankroll += bet*2
		print("You won: ", bet*2)
		print("Your chips: ",player.bankroll, '\n')

play()