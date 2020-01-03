from random import shuffle
from dealer import Dealer
from player import Player


class CardGame:
	def __init__(self):
		pass



# Set up match
dealer = Dealer()
player1 = Player(dealer)
dealer.add_player(player1)
player1.buy_chips(1000)
player1.place_bet(100)

# Begin round
dealer.shuffle()
dealer.deal_round()
print(f"Player1's hand = {player1.hand}")
print(f"Dealer's hand = {dealer.hand}")

# Player one's turn
while player1.status == "playing":
	action = input("Would you like to hit or stand? ")
	if action == "hit":
		player1.hit()
	elif action == "stand":
		player1.stand()
print(f"Player1's hand: {player1.hand}")

# Dealer's turn
print(f"dealer's total: {dealer.get_hand_total()}")
while (dealer.get_hand_total() < player1.get_hand_total() 
		and player1.status != "busted"
		and dealer.status != "busted"):
 	dealer.hit()
print(f"dealer's hand = {dealer.hand}")

# who won?
if player1.status == "busted" and dealer.status == "busted":
	print("the dealer and player both busted, this should\
		be impossible in b lackjack")
elif player1.status == "busted":
	print("player busted. The dealer wins.")
elif dealer.status == "busted":
	print("Dealer busted. The player wins.")
elif dealer.get_hand_total() > player1.get_hand_total():
	print("Dealer has a higher hand. Dealer wins.")
elif dealer.get_hand_total() < player1.get_hand_total():
	print("Player has a higher hand. Player wins.")
else:
	print("there has been an overlooked case, who won?")

# dealer.allocate_pot()
