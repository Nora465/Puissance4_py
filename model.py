#The class
import pygame

noir = (1, 1, 1)
blanc = (255, 255, 255) #INITIALISATION COULEURS 


class Goulotte(): #une des goulottes (=colonne) du plateau de jeu
	"""
	Représente une des colonnes du plateau de jeu
	"""
	def __init__(self, nbG:int):
		self.pionPos:list = [] #tableau des pions ("Yellow" ou "Blue")
		self.nbGoulotte:int = nbG #position de la goulotte (0 à 6)

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

class Plateau():
	"""
	Représente le plateau de jeu
	"""
	def __init__(self):				# Création des 7 goulottes du jeu
		self.g0 = Goulotte(0)
		self.g1 = Goulotte(1)
		self.g2 = Goulotte(2)
		self.g3 = Goulotte(3)
		self.g4 = Goulotte(4)
		self.g5 = Goulotte(5)
		self.g6 = Goulotte(6)

		self.UpPion = 0 #//TODO trouver un meilleur nom (le pion qui apparait en haut de l'écran)

		self.allPions = [self.g0.pionPos, self.g1.pionPos, self.g2.pionPos, 
						self.g3.pionPos, self.g4.pionPos, self.g5.pionPos, self.g6.pionPos]

class Player():
	"""
	docstring
	"""
	def __init__(self):
		pass