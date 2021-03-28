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
#===================== EVENT Loop ===================================
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			closeGame= True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			#==== State 0 : Title Screen
			if gameState == 0:
				if 	 IHM.CheckRectCollide(platoJeu, gameState, "play"):
					gameState= 1 #Capacities Screen
				elif IHM.CheckRectCollide(platoJeu, gameState, "stop"):
					closeGame= True #Exit the While Loop
			#==== State 1 : Select the capacities
			elif gameState == 1:
				if 	 IHM.CheckRectCollide(platoJeu, gameState, "capInvLine"):
					platoJeu.ChangeCap("capInvLine")
				elif IHM.CheckRectCollide(platoJeu, gameState, "capInvCol"):
					platoJeu.ChangeCap("capInvCol")
			#==== State 2 : Select the Music
			elif gameState == 2:
				if 	 IHM.CheckRectCollide(platoJeu, gameState, "musicAstro"):
					platoJeu.ChangeMusic("astronaut")
				elif IHM.CheckRectCollide(platoJeu, gameState, "musicMercu"):
					platoJeu.ChangeMusic("mercury")
				elif IHM.CheckRectCollide(platoJeu, gameState, "GO"):
					gameState = 3
			#==== State 3 : Game
			elif gameState == 3:
				if IHM.CheckRectCollide(platoJeu, gameState, "columns"):
					platoJeu.addToken(platoJeu.mouseBoardPos[0])
				elif IHM.CheckRectCollide(platoJeu, gameState, "capJ1"):
					if platoJeu.curPlayer.ID == 1: 
						gameState = 4 #Do A Capacity
				elif IHM.CheckRectCollide(platoJeu, gameState, "capJ2"):
					if platoJeu.curPlayer.ID == 2: 
						gameState = 4 #Do A Capacity
			#==== State 4 : Do A Capacity
			elif gameState == 4:
				if platoJeu.curPlayer.capacity == "capInvLine" and IHM.CheckRectCollide(platoJeu, gameState, "lines"):
					platoJeu.DoLineCap(platoJeu.mouseBoardPos[1])
					IHM.PlayASound("pew")
					gameState = 3 #Return to Game
				elif platoJeu.curPlayer.capacity == "capInvCol" and IHM.CheckRectCollide(platoJeu, gameState, "columns"):
					platoJeu.DoColCap(platoJeu.mouseBoardPos[0])
					IHM.PlayASound("pew")
					gameState = 3 #Return to Game
			#==== State 5 : End of Game (Winner or Draw)
			elif gameState == 5 :
				#Click anywhere : restart the game
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
		IHM.CheckRectCollide(platoJeu, gameState, "columns") #Update the column where the mouse is
		if platoJeu.DetectVictory() or platoJeu.DetectDraw():
			gameState = 5

	#State 4 : Do A Capacity
	elif gameState == 4:
		IHM.CheckRectCollide(platoJeu, gameState, "columns") #Update the column where the mouse is
		IHM.CheckRectCollide(platoJeu, gameState, "lines") #Update the line where the mouse is
	#State 5 : End of the Game (Winner or Draw)
	elif gameState == 5:
		pass
	#print(pygame.mouse.get_pos()) #debug : show the mouse position
	
	pygame.display.update()

#If we exit the main loop, exit the program
pygame.quit()
sys.exit()