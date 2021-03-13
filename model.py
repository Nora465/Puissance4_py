#The class
import pygame

noir = (1, 1, 1)
blanc = (255, 255, 255) #INITIALISATION COULEURS 

numOfLines = 6
numOfCol = 7

class Goulotte(): #une des goulottes (=colonne) du plateau de jeu
	"""
	Représente une des colonnes du plateau de jeu
	"""
	def __init__(self, nbG:int):
		self.pionPos:list = [] #tableau des pions (1 ou 2)
		self.nbGoulotte:int = nbG #position de la goulotte (0 à 6)
"""
	def addYellow(self) ->bool:
		if len(self.pionPos) < 7: #7 pions max dans chaque goulotte
			self.pionPos.insert(0, "yellow")
			return True
		return False

	def addBlue(self) ->bool:
		if len(self.pionPos) < 7: #7 pions max dans chaque goulotte
			self.pionPos.insert(0, "blue")
			return True
		return False

	def addPion(self, curPlayer:int) ->bool:
		if len(self.pionPos) < 7: #7 pions max dans chaque goulotte
			self.pionPos.insert(0, ("yellow", "blue")[curPlayer==1])
			return True
		return False
		"""

class Plateau():
	"""
	Représente le plateau de jeu
	"""
	def __init__(self, numOfPlayer: int):				# Création des 7 goulottes du jeu
		self.g0 = Goulotte(0)
		self.g1 = Goulotte(1)
		self.g2 = Goulotte(2)
		self.g3 = Goulotte(3)
		self.g4 = Goulotte(4)
		self.g5 = Goulotte(5)
		self.g6 = Goulotte(6)

		self.numPlayer = numOfPlayer
		self.curPlayer = True # True: P1/Yellow False: P2/Blue ...

		self.shadowToken = 0 #le pion qui apparait en haut de l'écran

		self.allTokens = [self.g0.pionPos, self.g1.pionPos, self.g2.pionPos, 
						self.g3.pionPos, self.g4.pionPos, self.g5.pionPos, self.g6.pionPos]

	def addToken(self, numGoulotte:int)-> bool:
		if len(self.allTokens[numGoulotte]) < 7: #7 pions max dans chaque goulotte
			self.allTokens[numGoulotte].insert(6, 1 if self.curPlayer else 2)
			self.curPlayer = not self.curPlayer #Change the current player
			#self.DetectVictory(numGoulotte)
			#self.DetectLines(len(self.allTokens[numGoulotte])-1)
			return True
		return False

	def DetectVictory(self, numColumn:int):
		lastPos = (numColumn, len(self.allTokens[numColumn]))
		isvictorious = (self.DetectColumns(lastPos[0])) or (self.DetectLines(lastPos[1]))
		self.findTokensAround(lastPos)

	def DetectLines(self, numLine:int)-> bool:
		"numLine : numéro de ligne (0-6) du dernier pion posé"
		potentialCols = [] #columns with the same number of token than the actual token
		for i in range(len(self.allTokens)): #loop through columns
			if len(self.allTokens[i]) >= numLine: #checks if 
				potentialCols.append(i) #add good column to array
		if len(potentialCols) <= 4: return False #if less than 4 tokens aligned, not win
		
		temp = 0
		oldOne = 0
		tab=[]
		for i in range(len(potentialCols)): #check if there is no gap between 4 tokens
			if (potentialCols[i]) == oldOne+1:
				temp += 1
				#if potentialCols[i] == 
				test = self.allTokens[potentialCols[i]][numLine]
				pass
			else:
				temp = 0
			oldOne = potentialCols[i]
		if temp >= 4:
			pass

	def DetectColumns(self, numColumn:int)-> bool:
		if len(self.allTokens[numColumn]) >= 4: #4 tokens should be here at least
			pass


	def findTokensAround(self, posToken:tuple):
		if (len(self.allTokens[posToken[0]]) == len(self.allTokens[posToken[0]-1])):
			pass

		#for i in range(len(self.allTokens)):
			#if len(self.allTokens[i]) != 0:



class Player():
	"""
	docstring
	"""
	def __init__(self, colorPlayer:str):
		self.name = "P1" if (colorPlayer=="yellow") else "P2"
		self.color = colorPlayer #either "yellow" or "blue"
		self.capacity = "" #capacity selected by player
		self.winner = False

	def ChangeCap(self, newCap:str):
		#Check : Old capacity must be different from the new one
		if self.capacity == newCap:
			return -1
		self.capacity = newCap
		return 0