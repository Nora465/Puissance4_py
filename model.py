import pygame, numpy as np

class Plateau():
	"""
	Représente le plateau de jeu
	"""
	def __init__(self, numOfPlayer: int):
		#Initialize the game board
		self.numLines = 7
		self.numCol = 7
		self.board = np.zeros((self.numCol, self.numLines), np.int8)
		self.curMusic = "" #either "astronaut" or "mercury"
		self.mouseBoardPos = [0, 0] #Position of the mouse on board => (col, line)

		#Initialize the players
		self.numPlayer = numOfPlayer
		self.players = []
		for i in range(numOfPlayer):
			self.players.append(Player(i+1))
		self.curPlayer:Player = self.players[0] # 1: P1/Yellow 2: P2/Blue ...
		self.__availableCap = ["capInvLine", "capInvCol"]
		self.winnerID = 0

	def ChangeMusic(self, newMusic:str):
		self.curMusic = newMusic
		if   newMusic == "astronaut": pygame.mixer.music.load("./musics/Astronaut.mp3")
		elif newMusic == "mercury"  : pygame.mixer.music.load("./musics/Mercury.mp3")
		pygame.mixer.music.play(0)

#===================== PLAYERS ===================================
	def NextPlayer(self):
		""" increment the current player """
		nextID = self.curPlayer.ID + 1
		#If nextID is bigger than the number of players, return to player 1
		if nextID > self.numPlayer:
			nextID= 1
		
		self.curPlayer = self.players[nextID-1]

	def ChangeCap(self, newCap:str):
		""" Change the capacity of current player, and then change the current player \n\r 
		Return True if the cap has been applied \n\r
		Return False if the cap is not available (or doesn't exist) """
		if self.__availableCap.count(newCap) == 1:
			self.__availableCap.remove(newCap)
			self.players[self.curPlayer.ID-1].capacity = newCap
			self.NextPlayer()
			return True
		return False
		
#===================== ADDING TOKENS ===================================
	def ColIsNotFull(self, col:int):
		""" Return true if the column can accept another token """
		return self.board[col][self.numLines-1] == 0

	def __FindNextAvailableLine(self, col:int): #Find the available line in the board (to put a token)
		for i in range(self.numLines):
			if self.board[col][i] == 0:
				return i

	def addToken(self, numGoulotte:int)-> bool:
		"""
		Insert a token in the board
		numGoulotte : between 0 to 6
		return : the need to update the screen
		"""
		if self.ColIsNotFull(numGoulotte): #emplacement disponible ?			
			tokLine = self.__FindNextAvailableLine(numGoulotte)
			self.board[numGoulotte, tokLine] = self.curPlayer.ID
			return True
		return False
	
	def DoColCap(self, col:int):
		for i in range(7):
			if self.board[col,i] == 0 :
				pass
			else:
				self.board[col,i] = 3-self.board[col,i]
		print("player"+str(self.curPlayer.ID)+" has done his capacity:" + str(self.curPlayer.capacity))
		self.NextPlayer()

	def DoLineCap(self, line:int):
		for i in range(6):
			if self.board[i, line] == 0:
				pass
			else:
				self.board[i, line] = 3-self.board[i, line]
		print("player"+str(self.curPlayer.ID)+" has done his capacity:" + str(self.curPlayer.capacity))
		self.NextPlayer()

#===================== VICTORY CONDITIONS ===================================
	def DetectVictory(self):
		#print(self.board)
		""" Detect the victory of a player (return the ID of winner, or 0 if nobody win) """
		#Check Lines ?
		for c in range(self.numCol-3):
			for l in range(self.numLines):
				if self.board[c][l] == self.board[c+1][l] \
				== self.board[c+2][l] == self.board[c+3][l] != 0:
					self.__SetWinner(self.board[c][l])
					print("win is line")
					return True
    
		#Check Columns ?
		for c in range(self.numCol):
			for l in range(self.numLines-3):
				if self.board[c][l] == self.board[c][l+1] \
				== self.board[c][l+2] == self.board[c][l+3] != 0:
					self.__SetWinner(self.board[c][l])
					print("win is column")
					return True

		#Check Diag : Right (bottom to top)
		for c in range(self.numCol-3):
			for l in range(self.numLines-3):
				if self.board[c][l] == self.board[c+1][l+1] \
				== self.board[c+2][l+2] == self.board[c+3][l+3] != 0:
					self.__SetWinner(self.board[c][l])
					print("win is diag1")
					return True

		#Check Diag : Left (bottom to top)
		for c in range(self.numCol-3):
			for l in range(3, self.numLines):
				if self.board[c][l] == self.board[c+1][l-1] \
				== self.board[c+2][l-2] == self.board[c+3][l-3] != 0:
					self.__SetWinner(self.board[c][l])
					print("win is diag2")
					return True
		return False

	def __SetWinner(self, IDWinner:int):
		self.winnerID = IDWinner

	def DetectDraw(self):
		""" Detect a draw (grid is full) """
		return not np.any((self.board == 0))

	def ResetData(self):
		""" Return a new Class, to reset the game """
		return Plateau(self.numPlayer)
		pass
#===================== PLAYER CLASS =========================================
#============================================================================
class Player():
	"""
	docstring
	"""
	def __init__(self, IDPlayer:int):
		self.name = "P" + str(IDPlayer)
		self.ID = IDPlayer
		self.capacity = "" #capacity selected by player
	
	def hasCap(self, capName:str):
		if self.capacity == capName:
			return True
		else: return False