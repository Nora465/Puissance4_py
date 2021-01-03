import pygame, sys
import model, IHM

pygame.init()

pygame.display.set_caption("New Interface")

platoJeu = model.Plateau() #Ma POO

def updateNeedMaj(numGou:int):
	if platoJeu.UpPion != numGou:
		platoJeu.UpPion = numGou
		return True
	else: return False

needMAJ = True

IHM.updatePlateau(platoJeu)

while True:
	tabOfRect = IHM.createCol() #création des colonnes pour detecter la souris

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit() #ferme pygame
			sys.exit() #ferme le programme
			
		if tabOfRect[0].collidepoint(pygame.mouse.get_pos()): #Souris entre dans goulotte 1
			needMAJ = updateNeedMaj(0)
			if event.type == pygame.MOUSEBUTTONDOWN:
				needMAJ = platoJeu.g0.addYellow() #ajout d'un pion jaune

		elif tabOfRect[1].collidepoint(pygame.mouse.get_pos()): #Souris entre dans goulotte 2
			needMAJ = updateNeedMaj(1)
			if event.type == pygame.MOUSEBUTTONDOWN:
				needMAJ = platoJeu.g1.addYellow() #ajout d'un pion jaune

		elif tabOfRect[2].collidepoint(pygame.mouse.get_pos()): #Souris entre dans goulotte 2
			needMAJ = updateNeedMaj(2)
			if event.type == pygame.MOUSEBUTTONDOWN:
				needMAJ = platoJeu.g2.addYellow() #ajout d'un pion jaune
				
		elif tabOfRect[3].collidepoint(pygame.mouse.get_pos()): #Souris entre dans goulotte 2
			needMAJ = updateNeedMaj(3)
			if event.type == pygame.MOUSEBUTTONDOWN:
				needMAJ = platoJeu.g3.addYellow() #ajout d'un pion jaune

		elif tabOfRect[4].collidepoint(pygame.mouse.get_pos()): #Souris entre dans goulotte 2
			needMAJ = updateNeedMaj(4)
			if event.type == pygame.MOUSEBUTTONDOWN:
				needMAJ = platoJeu.g4.addYellow() #ajout d'un pion jaune

		elif tabOfRect[5].collidepoint(pygame.mouse.get_pos()): #Souris entre dans goulotte 2
			needMAJ = updateNeedMaj(5)
			if event.type == pygame.MOUSEBUTTONDOWN:
				needMAJ = platoJeu.g5.addYellow() #ajout d'un pion jaune

		elif tabOfRect[6].collidepoint(pygame.mouse.get_pos()): #Souris entre dans goulotte 2
			needMAJ = updateNeedMaj(6)
			if event.type == pygame.MOUSEBUTTONDOWN:
				needMAJ = platoJeu.g6.addYellow() #ajout d'un pion jaune

	#print(pygame.mouse.get_pos()) #debug : affiche la position de la souris
	
	IHM.updatePlateau(platoJeu, needMAJ)
	needMAJ = False

	pygame.display.flip()
