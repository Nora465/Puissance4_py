import pygame

class Plateau():
	"""
	Class to store the data of the game
	"""
	def __init__(self, numOfPlayer: int):
		#Initialize the game board
		self.numLines = 7
		self.numCol = 7
		self.board = []
		for i in range(self.numCol):
			self.board.append([0] * self.numLines)
		self.curMusic = "" #either "astronaut" or "mercury"
		self.mouseBoardPos = [0, 0] #Position of the mouse on board => (col, line)

		#Initialize the players
		self.numPlayer = numOfPlayer
		self.players = []
		for i in range(numOfPlayer):
			self.players.append(Player(i+1))
		self.curPlayer:Player = self.players[0] # 0: P1/Yellow 1: P2/Blue ...
		self.availableCap = ["capInvLine", "capInvCol"]
		self.winnerID = 0

	def ChangeMusic(self, newMusic:str):
		""" Change the playing music (either astronaut or mercury) and start the play """
		self.curMusic = newMusic
		if   newMusic == "astronaut": pygame.mixer.music.load("./musics/Astronaut.mp3")
		elif newMusic == "mercury"  : pygame.mixer.music.load("./musics/Mercury.mp3")
		pygame.mixer.music.play(0)

#===================== PLAYERS ===================================
	def NextPlayer(self):
		""" Switch to the next player """
		nextID = self.curPlayer.ID + 1
		#If nextID is bigger than the number of players, return to player 1
		if nextID > self.numPlayer:
			nextID= 1
		
		self.curPlayer = self.players[nextID-1]

	def ChangeCap(self, newCap:str):
		""" Change the capacity of CURRENT player, and then switch to the next player \n\r 
		Return True if the cap has been applied \n\r
		Return False if the cap is not available (or doesn't exist) """
		if self.availableCap.count(newCap) == 1:
			self.availableCap.remove(newCap)
			self.curPlayer.capacity = newCap
			self.NextPlayer()
		
#===================== ADDING TOKENS ===================================
	def ColIsNotFull(self, col:int):
		""" Return true if the "col" can accept another token """
		return self.board[col][self.numLines-1] == 0

	def __FindNextAvailableLine(self, col:int): 
		""" Find the next available line in the "col" to put a token """
		for i in range(self.numLines):
			if self.board[col][i] == 0:
				return i

	def addToken(self, col:int)-> bool:
		"""
		Insert a token in the board array, and switch to the next player \n\r
		"col" must be between 0 to 6 \n\r
		"""
		if self.ColIsNotFull(col):
			tokLine = self.__FindNextAvailableLine(col)
			self.board[col][tokLine] = self.curPlayer.ID
			self.NextPlayer()
	
	def DoColCap(self, col:int):
		""" Do the capacity : "Exchange the tokens of a column" """
		for i in range(self.numLines):
			self.__ExchangeTokenID(col, i)
		print("player"+str(self.curPlayer.ID)+" has done his capacity:" + str(self.curPlayer.capacity))
		self.NextPlayer()

	def DoLineCap(self, line:int):
		""" Do the capacity : "Exchange the tokens of a line" """
		for i in range(self.numCol):
			self.__ExchangeTokenID(i, line)
		print("player"+str(self.curPlayer.ID)+" has done his capacity:" + str(self.curPlayer.capacity))
		self.NextPlayer()
	
	def __ExchangeTokenID(self, col:int, line:int):
		""" Exchange the color of token (for a capacity), if the placeholder has a token """
		if not self.board[col][line] == 0:
			newID = self.board[col][line] + 1
			if newID > self.numPlayer:  newID = 1
			
			self.board[col][line] = newID

#===================== VICTORY CONDITIONS ===================================
	def DetectVictory(self):
		""" Detect the victory of a player (return True if there is a WINNER) """
		#Check Lines ?
		for c in range(self.numCol-3):
			for l in range(self.numLines):
				if self.board[c][l] == self.board[c+1][l] \
				== self.board[c+2][l] == self.board[c+3][l] != 0:
					self.winnerID = self.board[c][l]
					print("win is line")
					return True
    
		#Check Columns ?
		for c in range(self.numCol):
			for l in range(self.numLines-3):
				if self.board[c][l] == self.board[c][l+1] \
				== self.board[c][l+2] == self.board[c][l+3] != 0:
					self.winnerID = self.board[c][l]
					print("win is column")
					return True

		#Check Diag : Right (bottom to top)
		for c in range(self.numCol-3):
			for l in range(self.numLines-3):
				if self.board[c][l] == self.board[c+1][l+1] \
				== self.board[c+2][l+2] == self.board[c+3][l+3] != 0:
					self.winnerID = self.board[c][l]
					print("win is diag1")
					return True

		#Check Diag : Left (bottom to top)
		for c in range(self.numCol-3):
			for l in range(3, self.numLines):
				if self.board[c][l] == self.board[c+1][l-1] \
				== self.board[c+2][l-2] == self.board[c+3][l-3] != 0:
					self.winnerID = self.board[c][l]
					print("win is diag2")
					return True
		return False

	def DetectDraw(self):
		""" Detect a draw (the grid has no occurence of "0") """
		#//TODO add more intelligence ? don't need to wait for the board to be full, to declare a Draw
		isDraw = True
		for col in self.board:
			for line in col:
				if line == 0: isDraw = False
		return isDraw

	def ResetData(self):
		""" Return a new Class, to reset the game """
		return Plateau(self.numPlayer)
		pass
#===================== PLAYER CLASS =========================================
#============================================================================
class Player():
	"""
	Class to store the data of a single player
	"""
	def __init__(self, IDPlayer:int):
		self.ID = IDPlayer
		self.capacity = "" #capacity selected by player
		self.cooldownCap = 0 #//TODO implement a cooldown after the use of a capacity
	
	def hasCap(self, capName:str):
		""" Return True if this player has the capacity """
		if self.capacity == capName:
			return True
		else: return False