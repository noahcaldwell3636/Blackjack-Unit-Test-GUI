"""
- Just a card object
TODO:
	- Ace currently just representing 11, needs to be 1 when hand is
	over 21. Might want to implement that logic in the player class.
"""
class Card:

	allowed_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
	allowed_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
		self.image = None
		self.face_down_image = None

		try:
			worth = int(value)
		except:
			if self.value == "A":
				worth = 11
			elif self.value == "K":
				worth = 10
			elif self.value == "Q":
				worth = 10	
			elif self.value == "J":
				worth = 10
			else:
				raise ValueError(f"card value invalid ({self.value})")


		self.worth = worth

	def __repr__(self):
		return f"{self.value} of {self.suit}"

	"""Assign an image to the card for it to be represented in the GUI."""
	def assign_image(self, img):
		self.image = img

	"""Assign face down image"""
	def assign_face_down_image(self, img):
		self.face_down_image = img
