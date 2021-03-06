import pygame
import funciones
import puntajes
import explicacion
import error
from botons import Option

def iniciarpantalla():
		pygame.init()
		screen_width = 800
		screen_height = 450
		screen=pygame.display.set_mode([screen_width,screen_height])
		return screen

def confondo(band):
	if band:
		screen.fill((0, 0, 0))
	else:
		screen.blit(fondo, (0, 0))

def opcioncantidad(nom):
	done = False
	cantidades = [8, 16, 24]
	score=0
	options = [Option("4", (365, 105)), Option("8", (365, 155)),
		Option("12", (365, 205)),Option("Todos", (350, 255)),Option("Volver",(350,305))] 
	while not done:
		pygame.event.pump()
		confondo(band)
		for option in options:
			if option.rect.collidepoint(pygame.mouse.get_pos()):
				option.hovered = True
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						done = True
						break
					if(event.type == pygame.MOUSEBUTTONDOWN):
						if option.text == "4":
							score = funciones.nivel(nom, score, screen, cantidades[0])
							funciones.terminarnivel(score, nom, screen)
						elif option.text == "8":
							score = funciones.nivel(nom, score, screen, cantidades[1])
							funciones.terminarnivel(score, nom, screen)
						elif option.text == "12":
							score = funciones.nivel(nom, score, screen, cantidades[2])
							funciones.terminarnivel(score, nom, screen)
						elif option.text == "Todos":
							for i in cantidades:
								score = funciones.nivel(nom, score, screen, i)
							funciones.terminarnivel(score, nom, screen)	
						elif option.text == "Volver":
							done=True		
			else:
				option.hovered = False
			option.draw()
			score = 0
		pygame.display.update()
		
def opcionjugar():
	done = False
	options = [Option("Provincias", (340, 105)), Option("Sudamerica", (335, 155)),
		Option("Volver", (345, 205))]
	while not done:
		pygame.event.pump()
		confondo(band)
		for option in options:
			for event in pygame.event.get():
				if option.rect.collidepoint(pygame.mouse.get_pos()):
					option.hovered = True
				if event.type == pygame.QUIT:
					done = True
					break
				if(event.type == pygame.MOUSEBUTTONDOWN):
					if option.text == "Sudamerica":
						nom = 'sudamerica'
						opcioncantidad(nom)
					if option.text == "Provincias":
						nom = 'provincias'
						opcioncantidad(nom)
					if 	option.text == "Volver":
						done=True
				else:
					option.hovered = False
			option.draw()
			score = 0
		pygame.display.update()		

def opcionpuntajes():
	done = False
	options = [Option("Provincias", (340, 105)), Option("Sudamerica", (335, 155)),
		Option("Volver", (345, 205))]
	while not done:
		pygame.event.pump()
		confondo(band)
		for option in options:
			if option.rect.collidepoint(pygame.mouse.get_pos()):
				option.hovered = True
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						done = True
						break
					if(event.type == pygame.MOUSEBUTTONDOWN):
						if option.text == "Sudamerica":
							nom = 'sudamerica'
							puntajes.mostrarpuntajes(nom, screen)
						if option.text == "Provincias":
							nom = 'provincias'
							puntajes.mostrarpuntajes(nom, screen)
						if 	option.text == "Volver":
							done=True
			else:
				option.hovered = False
			option.draw()
			score = 0
		pygame.display.update()	
screen = iniciarpantalla()
band = False
try:
	fondo = pygame.image.load("image/mapa-mundi.jpg")
except pygame.error:
	band = True	
menu_font = pygame.font.Font(None, 40)

#Opciones = [Option("Sonido", (140, 105)), Option("Prendido", (135, 155)),Option("Volver", (145, 205))]	

        		
options = [Option("Jugar", (340, 105)), Option("Mejores Puntajes", (335, 155)),
		Option("Opciones", (345, 205)), Option("Como Jugar", (345, 255))]

score = 0
done = False
while not done:
	pygame.event.pump()
	confondo(band)
	try:
		for option in options:
			if option.rect.collidepoint(pygame.mouse.get_pos()):
				option.hovered = True
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						done = True
						break
					if(event.type == pygame.MOUSEBUTTONDOWN):
						if option.text == "Jugar":
							opcionjugar()
							break					
						if option.text == "Mejores Puntajes":
							opcionpuntajes()
							break
						if option.text == "Como Jugar":
							explicacion.comojugar(screen)	
						#if 	option.text == "Opciones":
						#	options = Opciones
						#if 	option.text == "Prendido":
						#	option.text = "Apagado"
						#elif option.text == "Apagado":
						#	option.text = "Prendido"
						
			else:
				option.hovered = False
			option.draw()
			score = 0
	except :
		error.mensaje(screen)	
	pygame.display.update()
pygame.quit()    
