# Gestion de l'IHM
import pygame
import model

noir = (1, 1, 1)
blanc = (255, 255, 255)

#==================== PyGame Things ===================
screen = pygame.display.set_mode((1200, 800)) #TAILLE DE LA FENETRE

tablette = pygame.image.load("assets/Tablette.png")
tablette = pygame.transform.scale(tablette, (900, 700))

pionj= pygame.image.load("assets/PionJaune.png")
pionjBarre= pygame.image.load("assets/PionJauneCroix.png")
pionb = pygame.image.load("assets/pion20bleu.png")

#============ FUNCTIONS =====================================
def ShowPlato():
	screen.fill((blanc))
	screen.blit(tablette, (0,0))
	#pos for bouton change color 24 659

def updatePlateau(Platojeu :model.Plateau, needUpdate= True):	#mise à jour de l'affichage
	if needUpdate:
		ShowPlato()
		showTheFirst(Platojeu)
		
		AllPos = Platojeu.allPions
		for i in range(len(AllPos)):			#i: colonne
			for j in range(len(AllPos[i])):		#j : ligne 
				placerPion(AllPos[i][j], (i, j))
		
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

def placerPion(color:str, place:tuple):		#Place un pion graphiquement
	#Goulotte: 60 de largeur et 490 de hauteur
	#pion: 65 de largeur et 56 de hauteur
	#point initial: (220, 80)
	#68 : espace en largeur
	
	posX= 220 + (68 * place[0])
	posY= 513 - (56 * place[1])

	if   color == "yellow":	screen.blit(pionj, (posX, posY))
	elif color == "blue":	screen.blit(pionb, (posX, posY))

def showTheFirst(platoJeu:model.Plateau):		#trouver un meilleur nom (affiche le pion tout en haut, pour indiquer où il va tomber)
	xPos = 219 + (68 * platoJeu.UpPion) #220=emplacement 1er colonne // 70=distance entre chaque colonne
	pionsCol = platoJeu.allPions[platoJeu.UpPion]
	
	if len(pionsCol) == 7:
		screen.blit(pionjBarre, (xPos, 95))
	else:
		screen.blit(pionj, (xPos, 95))