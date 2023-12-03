import pygame, sys
import model
import IHM
from const import GAME_STATE

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
			if gameState == GAME_STATE.TITLE_0:
				if 	 IHM.CheckRectCollide(platoJeu, gameState, "play"):
					gameState= GAME_STATE.CAP_SELECT_1 #Capacities Screen
				elif IHM.CheckRectCollide(platoJeu, gameState, "stop"):
					closeGame= True #Exit the While Loop
			#==== State 1 : Select the capacities
			elif gameState == GAME_STATE.CAP_SELECT_1:
				if 	 IHM.CheckRectCollide(platoJeu, gameState, "capInvLine"):
					platoJeu.ChangeCap("capInvLine")
				elif IHM.CheckRectCollide(platoJeu, gameState, "capInvCol"):
					platoJeu.ChangeCap("capInvCol")
			#==== State 2 : Select the Music
			elif gameState == GAME_STATE.MUSIC_SELECT_2:
				if 	 IHM.CheckRectCollide(platoJeu, gameState, "musicAstro"):
					platoJeu.ChangeMusic("astronaut")
				elif IHM.CheckRectCollide(platoJeu, gameState, "musicMercu"):
					platoJeu.ChangeMusic("mercury")
				elif IHM.CheckRectCollide(platoJeu, gameState, "GO"):
					gameState = GAME_STATE.MAIN_GAME_3
			#==== State 3 : Game
			elif gameState == GAME_STATE.MAIN_GAME_3:
				if IHM.CheckRectCollide(platoJeu, gameState, "columns"):
					platoJeu.addToken(platoJeu.mouseBoardPos[0])
				elif IHM.CheckRectCollide(platoJeu, gameState, "capJ1"):
					if platoJeu.curPlayer.ID == 1: 
						gameState = GAME_STATE.DO_CAP_4 #Do A Capacity
				elif IHM.CheckRectCollide(platoJeu, gameState, "capJ2"):
					if platoJeu.curPlayer.ID == 2:
						gameState = GAME_STATE.DO_CAP_4 #Do A Capacity
			#==== State 4 : Do A Capacity
			elif gameState == GAME_STATE.DO_CAP_4:
				if platoJeu.curPlayer.capacity == "capInvLine" and IHM.CheckRectCollide(platoJeu, gameState, "lines"):
					platoJeu.DoLineCap(platoJeu.mouseBoardPos[1])
					IHM.PlayASound("pew")
					gameState = GAME_STATE.MAIN_GAME_3 #Return to Game
				elif platoJeu.curPlayer.capacity == "capInvCol" and IHM.CheckRectCollide(platoJeu, gameState, "columns"):
					platoJeu.DoColCap(platoJeu.mouseBoardPos[0])
					IHM.PlayASound("pew")
					gameState = GAME_STATE.MAIN_GAME_3 #Return to Game
			#==== State 5 : End of Game (Winner or Draw)
			elif gameState == GAME_STATE.WINNER_5:
				#Click anywhere : restart the game
				platoJeu = platoJeu.ResetData()
				gameState = GAME_STATE.TITLE_0
		#==== State 6 : Side-Game (In case of Draw)
		elif event.type == pygame.KEYDOWN:
			if gameState == GAME_STATE.SIDE_GAME_6:
				#Movement of the ships
				#Player 1 (yellow)
				if   event.key == pygame.K_z:	  platoJeu.players[0].ship.GoUp()
				elif event.key == pygame.K_s:	  platoJeu.players[0].ship.GoDown()
				elif event.key == pygame.K_q:	  platoJeu.players[0].ship.GoLeft()
				elif event.key == pygame.K_d:	  platoJeu.players[0].ship.GoRight()
				elif event.key == pygame.K_SPACE: platoJeu.players[0].ship.Fire()
				#Player 2 (Blue)
				elif event.key == pygame.K_UP:    platoJeu.players[1].ship.GoUp()
				elif event.key == pygame.K_DOWN:  platoJeu.players[1].ship.GoDown()
				elif event.key == pygame.K_LEFT:  platoJeu.players[1].ship.GoLeft()
				elif event.key == pygame.K_RIGHT: platoJeu.players[1].ship.GoRight()
				elif event.key == pygame.K_KP0:   platoJeu.players[1].ship.Fire()
	
#===================== State Machine ===================================
	#==== State 0 : Title Screen
	if gameState == GAME_STATE.TITLE_0:
		pass
	#==== State 1 : Capacity Selection
	elif gameState == GAME_STATE.CAP_SELECT_1:
		allPlayerHasCap = False
		for player in platoJeu.players:
			allPlayerHasCap = (player.capacity != "")
		
		if allPlayerHasCap: gameState= GAME_STATE.MUSIC_SELECT_2
	#==== State 2 : Music Selection
	elif gameState == GAME_STATE.MUSIC_SELECT_2:
		pass
	#==== State 3 : Game
	elif gameState == GAME_STATE.MAIN_GAME_3:
		IHM.CheckRectCollide(platoJeu, gameState, "columns") #Update the column where the mouse is
		if platoJeu.DetectVictory():
			gameState = GAME_STATE.WINNER_5
		elif platoJeu.DetectDraw():
			gameState = GAME_STATE.SIDE_GAME_6

	#==== State 4 : Do A Capacity
	elif gameState == GAME_STATE.DO_CAP_4:
		IHM.CheckRectCollide(platoJeu, gameState, "columns") #Update the column where the mouse is
		IHM.CheckRectCollide(platoJeu, gameState, "lines") #Update the line where the mouse is
	#==== State 5 : End of the Game (Winner)
	elif gameState == GAME_STATE.WINNER_5:
		pass
	#==== State 6 : Side-Game (In case of Draw)
	elif gameState == GAME_STATE.SIDE_GAME_6:
		for player in platoJeu.players:
			#Movement of the bullet
			if player.ship.bulExist:
				if pygame.time.get_ticks() >= player.ship.lastTick + 100: #in ms
					player.ship.MoveBullet(20) #Move by 10px every 100ms
			#The bullet has hit a ship ?
			if IHM.CheckRectCollide(platoJeu, gameState, "hitJ"+str(player.ID)):
				player.ship.GetHit()
			#The ship has 0 HP (the other win)
			if player.ship.HP <= 0:
				platoJeu.winnerID = (platoJeu.numPlayer+1) - player.ID
				gameState = GAME_STATE.WINNER_5

	print(pygame.mouse.get_pos()) #debug : show the mouse position
	
	pygame.display.update()

#If we exit the main loop, exit the program
pygame.quit()
sys.exit()