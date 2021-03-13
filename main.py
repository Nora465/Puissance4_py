import pygame, sys
import model, IHM

def UpdateShadowTokenPos(numChan:int)-> bool:
	"""
	determine if the shadow token has change its position \n
	return a bool that represent the need to update the board
	"""
	if platoJeu.shadowToken != numChan:
		platoJeu.shadowToken = numChan	#store the new position in PlatoJeu
		return True
	else: 
		return False

#======================================================================
pygame.init()

pygame.display.set_caption("My Connect-4 Game!")

platoJeu = model.Plateau(2) #My POO (english : Object-Oriented Programming)

#needUpdate:bool = True #True if the board need to be updated

IHM.ShowBoardElem() #display the board at launch

while True:
	tabOfRect = IHM.createCol() #Get an array of the 7 rectangles (to detect the mouse cursor)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit() #close pygame
			sys.exit() #close the python program
		
		for i in range(len(tabOfRect)):
			if tabOfRect[i].collidepoint(pygame.mouse.get_pos()): #is mouse in the column "i" ?
				IHM.needUpdate = UpdateShadowTokenPos(i) #Update the position of the shadow token
				if event.type == pygame.MOUSEBUTTONDOWN:
					IHM.needUpdate = platoJeu.addToken(i) #if mouse click, add a token in the column "i"
					

	#print(pygame.mouse.get_pos()) #debug : show the mouse position
	
	IHM.updateHMI(platoJeu) #Update the board, only if needed
	IHM.needUpdate = False

	pygame.display.update()
