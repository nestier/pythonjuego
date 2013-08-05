import pygame
from botons import Option

def confondo(band, screen, fondo):
	if band:
		screen.fill((0, 0, 0))
	else:
		screen.blit(fondo, (0, 0))

def comojugar(screen):
	try:
		fondo = pygame.image.load("image/mapa-mundi.jpg")
		band = False
	except pygame.error:
		band = True	
	menu_font = pygame.font.Font(None, 40)
	done = False
	options = [Option("Volver", (345, 250))]
	fon = pygame.font.SysFont(None, 40)
	while not done:
		pygame.event.pump()
		confondo(band, screen, fondo)
		for option in options:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
					break
				if option.rect.collidepoint(pygame.mouse.get_pos()):
					option.hovered = True					
					if(event.type == pygame.MOUSEBUTTONDOWN):
						if option.text == "Volver":
							done=True
				else:
					option.hovered = False
			texto2 = fon.render('Es un juego de memoria,has click en las cartas', True, (0, 0, 0))
			texto = fon.render('y encuentra sus parejas,pero las parejas son geograficas,', True, (0, 0, 0))
			texto1 = fon.render('encuentra el pais y su capital o la provincia y su capital', True, (0, 0, 0))			
			screen.blit(texto2, (75,100))
			screen.blit(texto, (10, 150))
			screen.blit(texto1, (20, 200))		
			option.draw()
			score = 0
		pygame.display.update()
