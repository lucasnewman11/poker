class player():
	
	def __init__(self, chips = 0):
		self.stack = chips
		self.hand = []
			
	def show(self):
		print self.hand
		
	def getbet(self):
		bet = raw_input("%s's turn (%r):" % self, self.hand)
		return bet
		
		
class deck():
	
	def __init__(self):
		ranks = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
		suits = ['s', 'c', 'h', 'd']
		self.deck = [i + j for i in ranks for j in suits]
		
	def shuffle(self):
		import random
		random.shuffle(self.deck)
		
class table():
	
	from collections import deque	
	
	def __init__(self, players):
	
		self.players = deque(players)
		self.button = self.players[len(players]
		self.small = players[0]
		self.big = players[1]
		
	def rotate():
		self.players.rotate[-1]
		self.button = self.players[len(self.players]
		self.small = self.players[0]
		self.big = self.players[1]
				
class hand():

	def __init__(self, deck, table, blinds)
		self.table = table
		self.board = []
		self.blinds = blinds
		self.pot = 0
		
		
	def dealcard(self):
		for i in self.table.players:
			i.hand.append(self.deck.pop()) 
			
	def street(self):
		self.board.append(self.deck.pop())
	
	def start():
		self.deck.shuffle()
		self.dealcard() * 2
			
	def round(players):
		match = 0
		for i in players:
			bet = i.getbet()
			if bet.upper.startswith('f'):
				del i
				continue
			if bet.upper.startswith('c'):
				i.stack -= match
				self.pot += match
			if bet > match:
				match = 
		
class 
	
			
			
		
	

		
	
