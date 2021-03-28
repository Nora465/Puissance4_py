# HMI Things
import pygame
import model

#==================== PyGame Things ===================
pygame.init()

screen = pygame.display.set_mode((1200, 800)) # Window Size

coordsGrid = (150, 50) #relative coordinates for placing imgs on grid

#==================== Load IMAGES ===================
#transform.scale = Increase/Reduce the size of image
#Grid for Tokens
gridImg = pygame.image.load("assets/Tablette.png")
gridImg = pygame.transform.scale(gridImg, (900, 700))

#Tokens
pionj		= pygame.image.load("assets/PionJaune.png")
pionjBarre	= pygame.image.load("assets/PionJauneCroix.png")
pionb 		= pygame.image.load("assets/PionBleu.png")
pionbBarre	= pygame.image.load("assets/PionBleuCroix.png")

#Background
bgImg = pygame.image.load("assets/bg.png")
bgImg = pygame.transform.scale(bgImg, (1200, 800))

#Start Screen : Buttons
playBP = pygame.image.load("assets/playButton.png")
quitBP = pygame.image.load("assets/quitButton.png")

#Start Screen : Title
titleImg = pygame.image.load("assets/titre.png")
titleImg = pygame.transform.scale(titleImg, (274*2,148*2))

#Victory Screen
victoire_j1 = pygame.image.load("assets/victoire_j.png")
victoire_j2 = pygame.image.load("assets/victoire_b.png")
egalite = pygame.image.load("assets/egalite.png")

#To show the current player
j1_menu = pygame.image.load("assets/J1_menu.png")
j2_menu = pygame.image.load("assets/J2_menu.png")
j1_play = pygame.image.load("assets/J1_play.png")
j2_play = pygame.image.load("assets/J2_play.png")

#Capacities Screen
capInvLine = pygame.image.load("assets/capLine.png")
capInvLine = pygame.transform.scale(capInvLine, (150, 150))
arrowLineJ1 = pygame.image.load("assets/arrowLineJ1.png")
arrowLineJ2 = pygame.image.load("assets/arrowLineJ2.png")

capInvCol = pygame.image.load("assets/capColumn.png")
capInvCol = pygame.transform.scale(capInvCol, (150, 150))
arrowColJ1 = pygame.image.load("assets/arrowColumnJ1.png")
arrowColJ2 = pygame.image.load("assets/arrowColumnJ2.png")
#Go button (after the selection of music)
go = pygame.image.load("assets/go.png")
go = pygame.transform.scale(go, (100, 100))

#music screen : texts
txtMusAstro = pygame.image.load("assets/MusSelAstro.png")
txtMusMercu = pygame.image.load("assets/MusSelMercu.png")

choose = pygame.image.load("assets/choose.png")
choose = pygame.transform.scale(choose, (1000, 500))

musique = pygame.image.load("assets/musique.png")
musique = pygame.transform.scale(musique, (1000, 500))

astroImg = pygame.image.load("assets/astronaut.png")
astroImg = pygame.transform.scale(astroImg, (50, 50))

mercuImg = pygame.image.load('assets/mercury.png')
mercuImg = pygame.transform.scale(mercuImg, (50, 50))
#==================== Load SOUNDS ===================
pew = pygame.mixer.Sound('effects/heat-vision.mp3')

#============ FUNCTIONS =====================================
def showScreen(platoJeu:model.Plateau, gameState:int):
	""" Blit things to the screen, and launch musics """
#=============== GameState 0 - Title Screen ==================================
	if gameState == 0:
		#Images
		screen.blit(bgImg, (0,0))
		screen.blit(titleImg, (350, 20))
		screen.blit(playBP, (300,400))
		screen.blit(quitBP, (700, 400))
		#Sounds
		if not pygame.mixer.music.get_busy():
			pygame.mixer.music.load("./musics/ElevatorMusic.mp3")
			pygame.mixer.music.play(1)
#=============== GameState 1 - Select the capacities ==================================
	elif gameState == 1:
		#Images
		screen.blit(bgImg, (0, 0))
		screen.blit(choose, (150, 0))

		for cap in platoJeu.availableCap:
			if   cap == "capInvLine": screen.blit(capInvLine, (505, 250))
			elif cap == "capInvCol":  screen.blit(capInvCol, (500, 450))

		#Show the current player on screen
		if platoJeu.curPlayer.ID == 1:
			screen.blit(j1_play, (200, 100))
			screen.blit(j2_menu, (850, 100))
		elif platoJeu.curPlayer.ID == 2:
			screen.blit(j1_menu, (200, 100))
			screen.blit(j2_play, (850, 100))

		#show the capacity each player have
		for player in platoJeu.players:
			if   player.capacity == "capInvLine":
				if 	 player.ID == 1: screen.blit(capInvLine, (200, 270))
				elif player.ID == 2: screen.blit(capInvLine, (860, 270))
			elif player.capacity == "capInvCol":
				if 	 player.ID == 1: screen.blit(capInvCol, (200, 270))
				elif player.ID == 2: screen.blit(capInvCol, (860, 270))

		#Play sound (if not already started)
		if not pygame.mixer.music.get_busy():
			pygame.mixer.music.load('./musics/ElevatorMusic.mp3')
			pygame.mixer.music.play(0)
#=============== GameState 2 - Select the Music ==================================
	elif gameState == 2:
		screen.blit(bgImg, (0, 0))
		screen.blit(musique, (100, -100))
		screen.blit(astroImg, (200, 150))
		screen.blit(mercuImg, (300, 150))
		#Music Selection Texts
		if platoJeu.curMusic == "astronaut":
			screen.blit(txtMusAstro, (200, 200))
		elif platoJeu.curMusic == "mercury":
			screen.blit(txtMusMercu, (200, 200))
		#Blit the "GO" button only if a music has been selected
		if platoJeu.curMusic != "":
			screen.blit(go, (525, 650))
#=============== GameState 3/4 - 3:Game | 4:Do A Cap ==================================
	elif gameState == 3 or gameState == 4:
		screen.blit(bgImg, (0, 0))
		screen.blit(gridImg, coordsGrid)
		showTheFirst(platoJeu, gameState)

		#Blit the players capacities
		for player in platoJeu.players:
			if   player.capacity == "capInvLine":
				if 	 player.ID == 1: screen.blit(capInvLine, (50, 600))
				elif player.ID == 2: screen.blit(capInvLine, (1000, 600))
			elif player.capacity == "capInvCol":
				if 	 player.ID == 1: screen.blit(capInvCol, (50, 600))
				elif player.ID == 2: screen.blit(capInvCol, (1000, 600))
		
		#Blit the player indicator
		if platoJeu.curPlayer.ID == 1:
			screen.blit(j1_play, (50, 20))
			screen.blit(j2_menu, (1030, 20))
		elif platoJeu.curPlayer.ID == 2:
			screen.blit(j1_menu, (50, 20))
			screen.blit(j2_play, (1030, 20))

		#Blit the board Tokens
		AllPos = platoJeu.board
		for i in range(len(AllPos)):			#i: column
			for j in range(len(AllPos[i])):		#j : line 
				PlaceToken(AllPos[i][j], (i, j))
		
#=============== GameState 5 - End Of Game (WIN) ==================================
	elif gameState == 5:
		pygame.mixer.music.stop()
		if platoJeu.winnerID == 0:
			screen.blit(egalite, (400, 250))
		if platoJeu.winnerID == 1:
			screen.blit(victoire_j1, (400, 250))
		elif platoJeu.winnerID == 2:
			screen.blit(victoire_j2, (400, 250))

def CheckRectCollide(platoJeu:model.Plateau, gameState:int, event:str):
	mousePos = pygame.mouse.get_pos()
	isOK = False
	#=============== GameState 0 - Title Screen ==================================
	if gameState == 0:
		if 	 event == "play" and playBP.get_rect(topleft = (300, 400)).collidepoint(mousePos):
			isOK = True
		elif event == "stop" and quitBP.get_rect(topleft = (700, 400)).collidepoint(mousePos):
			isOK = True
	#=============== GameState 1 - Select the capacities ==================================
	elif gameState == 1:
		if 	 event == "capInvLine" and capInvLine.get_rect(topleft = (505, 250)).collidepoint(mousePos):
			isOK = True
		if 	 event == "capInvCol" and capInvCol.get_rect(topleft = (500, 450)).collidepoint(mousePos):
			isOK = True
	#=============== GameState 2 - Select the Music ==================================
	elif gameState == 2:
		if 	 event == "musicAstro" and astroImg.get_rect(topleft = (200, 150)).collidepoint(mousePos):
			isOK = True
		if 	 event == "musicMercu" and mercuImg.get_rect(topleft = (300, 150)).collidepoint(mousePos):
			isOK = True
		if   event == "GO" and go.get_rect(topleft = (525, 650)).collidepoint(mousePos) and platoJeu.curMusic != "":
			isOK = True
	#=============== GameState 3 - Game==========================================
	elif gameState == 3:
		tabOfRect= createCol()
		for i in range(len(tabOfRect)):
			if event == "columns" and tabOfRect[i].collidepoint(mousePos):
				platoJeu.mouseBoardPos[0] = i #Save the column where the mouse is
				isOK = True
		
		#size of "Cap" button : (150, 150)
		if   event == "capJ1" and pygame.Rect((50, 600), (150, 150)).collidepoint(mousePos):
			isOK = True
		elif event == "capJ2" and pygame.Rect((1000, 600), (150, 150)).collidepoint(mousePos):
			isOK = True
	#=============== GameState 4 - Do A Capacity ==================================
	elif gameState == 4:
		tabOfRect= createCol()
		for i in range(len(tabOfRect)):
			if event == "columns" and tabOfRect[i].collidepoint(mousePos):
				platoJeu.mouseBoardPos[0] = i #Save the column where the mouse is
				isOK = True

		tabOfLines= createLines()
		for i in range(len(tabOfLines)):
			if event== "lines" and tabOfLines[i].collidepoint(mousePos):
				platoJeu.mouseBoardPos[1] = i #Save the line where the mouse is
				isOK = True
	#=============== GameState 5 - End of game (Win or Draw) ==================================
	elif gameState == 5:
		pass
	return isOK

def PlayASound(name:str):
	if (name == "pew"): pew.play()

def createCol(): #créé les colonnes, qui servira à déclencher les events
	#Les colonnes font 60 de largeur, et 490 de hauteur
	#rect_col1 = pygame.draw.rect(screen, blanc, (220, 80, 62, 490), 1) #60 de largeur et 490 de hauteur
	#rect_col2 = pygame.draw.rect(screen, blanc, (290, 80, 62, 490), 1)
	retTab = []
	xPos = 0

	for i in range(7):
		xPos = 219 + (68 * i) + coordsGrid[0] #220=emplacement 1er colonne // 70=distance entre chaque colonne //offsetX
		retTab.append(pygame.Rect((xPos, 80+coordsGrid[1], 62, 490)))
		#retTab.append(pygame.draw.rect(screen, (noir), (xPos, 80+coordsGrid[1], 62, 490), 1)) #use this to show the columns
	return retTab

def createLines():
	retLines = []
	yPos = 0

	for i in range(7): #7 lines
		yPos= 561 - (56 * i)
		retLines.append(pygame.Rect((368, yPos, 473, 59)))
		#retLines.append(pygame.draw.rect(screen, (0,0,0), (368, yPos, 473, 59), 1)) #use this to show the lines
	return retLines


def PlaceToken(player:int, place:tuple):
	""" Place a Token in the board array"""
	#Goulotte: 60 de largeur et 490 de hauteur
	#pion: 65 de largeur et 56 de hauteur
	#point initial: (220, 80)
	#68 : espace en largeur
	
	posX= coordsGrid[0] + 220 + (68 * place[0])
	posY= coordsGrid[1] + 513 - (56 * place[1])

	if   player == 1:	screen.blit(pionj, (posX, posY))
	elif player == 2:	screen.blit(pionb, (posX, posY))

def showTheFirst(platoJeu:model.Plateau, gameState:int):		#//TODO trouver un meilleur nom (affiche le pion tout en haut, pour indiquer où il va tomber)	
	imgToBlit = 0

	if gameState == 3:
		if platoJeu.ColIsNotFull(platoJeu.mouseBoardPos[0]): #if the column is not full
			if platoJeu.curPlayer.ID == 1: imgToBlit= pionj
			elif platoJeu.curPlayer.ID == 2: imgToBlit= pionb
		else: #if the column is full
			if platoJeu.curPlayer.ID == 1: imgToBlit= pionjBarre
			elif platoJeu.curPlayer.ID == 2: imgToBlit= pionbBarre
		xPos = 219 + (68 * platoJeu.mouseBoardPos[0]) + coordsGrid[0] #220=emplacement 1er colonne // 70=distance entre chaque colonne
		screen.blit(imgToBlit, (xPos, coordsGrid[1] + 95))

	elif gameState == 4:
		if platoJeu.curPlayer.capacity == "capInvLine":
			if   platoJeu.curPlayer.ID == 1: imgToBlit= arrowLineJ1
			elif platoJeu.curPlayer.ID == 2: imgToBlit= arrowLineJ2
			yPos = 511 - (56 * platoJeu.mouseBoardPos[1]) + coordsGrid[1] #220=emplacement 1er colonne // 70=distance entre chaque colonne
			screen.blit(imgToBlit, (coordsGrid[0] + 150, yPos))	

		elif platoJeu.curPlayer.capacity == "capInvCol":
			if   platoJeu.curPlayer.ID == 1: imgToBlit= arrowColJ1
			elif platoJeu.curPlayer.ID == 2: imgToBlit= arrowColJ2
			xPos = 219 + (68 * platoJeu.mouseBoardPos[0]) + coordsGrid[0] #220=emplacement 1er colonne // 70=distance entre chaque colonne
			screen.blit(imgToBlit, (xPos, coordsGrid[1] + 95))
		