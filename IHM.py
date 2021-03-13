# HMI Things
import pygame
import model

black = (1, 1, 1)
white = (255, 255, 255)

#==================== PyGame Things ===================
screen = pygame.display.set_mode((1200, 800)) # Window Size

gameBoard = pygame.image.load("assets/Tablette.png")
gameBoard = pygame.transform.scale(gameBoard, (900, 700)) #Increase size of gameBoard 

pionj		= pygame.image.load("assets/PionJaune.png")
pionjBarre	= pygame.image.load("assets/PionJauneCroix.png")
pionb 		= pygame.image.load("assets/PionBleu.png")
pionbBarre	= pygame.image.load("assets/PionBleuCroix.png")

needUpdate = True #True if the board need to be updated

#============ FUNCTIONS =====================================
def ShowBoardElem():
	screen.fill((white))
	screen.blit(gameBoard, (0,0))
	#pos for first bouton (24, 659)

def updateHMI(boardData :model.Plateau):	#Update the program window
	global needUpdate #reference to the global variable
	if needUpdate:
		ShowBoardElem()
		showTheFirst(boardData)
		
		AllPos = boardData.allTokens
		for i in range(len(AllPos)):			#i: column
			for j in range(len(AllPos[i])):		#j : line 
				placerPion(AllPos[i][j], (i, j))
		needUpdate = False
		
def createCol(): #créé les colonnes, qui servira à déclencher les events
	#Les colonnes font 60 de largeur, et 490 de hauteur
	#rect_col1 = pygame.draw.rect(screen, blanc, (220, 80, 62, 490), 1) #60 de largeur et 490 de hauteur
	#rect_col2 = pygame.draw.rect(screen, blanc, (290, 80, 62, 490), 1)
	retTab = []
	xPos = 0
	for i in range(7):
		xPos = 219 + (68 * i) #220=emplacement 1er colonne // 70=distance entre chaque colonne
		retTab.append(pygame.Rect((xPos, 80, 62, 490)))
		#retTab.append(pygame.draw.rect(screen, (noir), (xPos, 80, 64, 490), 1)) #permet d'afficher les cols
	return retTab

def placerPion(playerTok:int, place:tuple):		#Place un pion graphiquement
	#Goulotte: 60 de largeur et 490 de hauteur
	#pion: 65 de largeur et 56 de hauteur
	#point initial: (220, 80)
	#68 : espace en largeur
	
	posX= 220 + (68 * place[0])
	posY= 513 - (56 * place[1])

	if   playerTok == 1:	screen.blit(pionj, (posX, posY))
	elif playerTok == 2:	screen.blit(pionb, (posX, posY))

def showTheFirst(platoJeu:model.Plateau):		#trouver un meilleur nom (affiche le pion tout en haut, pour indiquer où il va tomber)
	xPos = 219 + (68 * platoJeu.shadowToken) #220=emplacement 1er colonne // 70=distance entre chaque colonne
	pionsCol = platoJeu.allTokens[platoJeu.shadowToken]
	
	if len(pionsCol) < 7: #if the column is not full
		if platoJeu.curPlayer:
			screen.blit(pionj, (xPos, 95))
		else:
			screen.blit(pionb, (xPos, 95))
	else:					#if the column is full
		if platoJeu.curPlayer:
			screen.blit(pionjBarre, (xPos, 95))
		else:
			screen.blit(pionbBarre, (xPos, 95))