import pygame, sys
import model
import IHM
#======================================================================
pygame.init()

pygame.display.set_caption("My Connect-4 Game!")

platoJeu = model.Plateau(2) #Data of the Game

gameState = 0
closeGame = False
while not closeGame:
	IHM.showScreen(platoJeu, gameState) #Blit the elements on screen (depending on the state)
	IHM.createLines()
#===================== EVENT Loop ===================================
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			closeGame= True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			#State 0 : Title Screen
			if gameState == 0:
				if 	 IHM.CheckRectCollide(platoJeu, gameState, "play"):
					gameState= 1 #go to Capacities Screen
				elif IHM.CheckRectCollide(platoJeu, gameState, "stop"):
					closeGame= True
			#State 1 : Select the capacities
			elif gameState == 1:
				if 	 IHM.CheckRectCollide(platoJeu, gameState, "capInvLine"):
					platoJeu.ChangeCap("capInvLine")
				elif IHM.CheckRectCollide(platoJeu, gameState, "capInvCol"):
					platoJeu.ChangeCap("capInvCol")
			#State 2 : Select the Music
			elif gameState == 2:
				if 	 IHM.CheckRectCollide(platoJeu, gameState, "musicAstro"):
					platoJeu.ChangeMusic("astronaut")
				elif IHM.CheckRectCollide(platoJeu, gameState, "musicMercu"):
					platoJeu.ChangeMusic("mercury")
				elif IHM.CheckRectCollide(platoJeu, gameState, "GO"):
					gameState= 3
			#State 3 : Game
			elif gameState == 3:
				if IHM.CheckRectCollide(platoJeu, gameState, "columns"):
					if platoJeu.addToken(platoJeu.mouseBoardPos[0]): #if mouse click, add a token in the column "i"
						#print("player"+str(platoJeu.curPlayer.ID) + " win is : "+ str(platoJeu.DetectVictory()))
						platoJeu.NextPlayer()
				elif IHM.CheckRectCollide(platoJeu, gameState, "capJ1"):
					if platoJeu.curPlayer.ID == 1:
						gameState= 4 #Do A Capacity
						
				elif IHM.CheckRectCollide(platoJeu, gameState, "capJ2"):
					if platoJeu.curPlayer.ID == 2:
						gameState= 4 #Do A Capacity
			#State 4 : Do A Capacity
			elif gameState == 4:
				if platoJeu.curPlayer.capacity == "capInvLine" and IHM.CheckRectCollide(platoJeu, gameState, "lines"):
					platoJeu.DoLineCap(platoJeu.mouseBoardPos[1])
					gameState = 3 #Return to Game
				elif platoJeu.curPlayer.capacity == "capInvCol" and IHM.CheckRectCollide(platoJeu, gameState, "columns"):
					platoJeu.DoColCap(platoJeu.mouseBoardPos[0])
					gameState = 3 #Return to Game
			#State 5/6 : End of Game (Either 5:WIN or 6:DRAW)
			elif gameState == 5 or gameState == 6:
				#Click anywhere : go to gameState 0
				platoJeu = platoJeu.ResetData()
				gameState = 0
	
#===================== State Machine ===================================
	#State 0 : Title Screen
	if gameState == 0:
		pass
	#State 1 : Capacity Selection
	elif gameState == 1:
		allPlayerHasCap = False
		for player in platoJeu.players:
			allPlayerHasCap = (player.capacity != "")
		
		if allPlayerHasCap: gameState= 2
	#State 2 : Music Selection
	elif gameState == 2:
		pass
	#State 3 : Game
	elif gameState == 3:
		IHM.CheckRectCollide(platoJeu, gameState, "columns") #Update the shadow token

		if platoJeu.DetectVictory():
			gameState = 5
		elif platoJeu.DetectDraw():
			gameState = 6
	#State 4 : Do A Capacity
	elif gameState == 4:
		#//TODO afficher une fleche, à la place d'un pion (sur lignes et sur colonnes)
		IHM.CheckRectCollide(platoJeu, gameState, "columns") #Update the column where the mouse is
		IHM.CheckRectCollide(platoJeu, gameState, "lines") #Update the line where the mouse is
	#State 5 : End of the Game (Winner only)
	elif gameState == 5:
		pass
	#State 6 : End of the Game (Draw only)
	elif gameState == 6:
		pass
	#print(pygame.mouse.get_pos()) #debug : show the mouse position
	
	pygame.display.update()

#If we exit the main loop, exit the program
pygame.quit()
sys.exit()