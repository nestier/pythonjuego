import pygame
import pickle
from Botons import Option
import Funciones
		
class Option2(Option):

	hovered = False
	
	def __init__(self, text, pos):
		self.letra='A'
		self.cont=0	
		super(Option2, self).__init__(text, pos)
		
	
	def set_rend(self):
		menu_font = pygame.font.Font(None, 40)
		self.rend = menu_font.render(self.letra, True, self.get_color())
	
	def cambiarletra(self):
		lista=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		if self.cont < 25:
			self.cont+=1
		else:
			self.cont=0
		self.letra=lista[self.cont]
	
	def getletra(self):
		return self.letra			

def iniciarpantalla():
		pygame.init()
		screen_width = 800
		screen_height = 450
		screen=pygame.display.set_mode([screen_width,screen_height])
		return screen

def guardararchivo(lista,nom):
	x = open(nom,'w')
	pickle.dump(lista, x)


def guardarpuntaje(obj, punt, nombre):
	nom=[obj[0].getletra()+obj[1].getletra()+obj[2].getletra(),punt]
	lista=[]
	lista=Funciones.abrirarchivo(nombre)
	for obj in lista:
		if obj[1]< nom[1]:
			aux=nom
			nom=obj
			obj=aux
	guardararchivo(lista,nombre)
			
def compararpuntaje(punt, nom, screen):
	nombre=	"puntajes/"+nom
	lista=Funciones.abrirarchivo(nombre)
	for obj in lista:
		if obj[1] < punt:
			escribirnombre(screen,punt,nombre)
			break

def confondo(screen, band, fondo):
	if band:
		screen.fill(white)
	else:
		screen.blit(fondo, (0,0))

def escribirnombre(screen,puntaje,nombre):
	band = False
	clock = pygame.time.Clock()
	try:
		fondo = pygame.image.load("image/mapa-mundi.jpg")
	except pygame.error:
		band = True	
	menu_font = pygame.font.Font(None, 40)
	         		
	options = [Option2("1", (140, 105)), Option2("2", (135, 155)),
			Option2("3", (145, 205)),Option("listo",(145,265))]
		
	puntaje = 0
	done = False

	while not done:
		pygame.event.pump()
		confondo(screen, band, fondo)
		for option in options:
			if option.rect.collidepoint(pygame.mouse.get_pos()):
				option.hovered = True
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						done = True
						break
					if(event.type == pygame.MOUSEBUTTONDOWN):
						if option.text == "1":
							option.cambiarletra()
							break
						if option.text == "2":
							option.cambiarletra()
							break
						if option.text == "3":
							option.cambiarletra()
							break
						if option.text=='listo':
							guardarpuntaje(options, puntaje, nombre)
							done=True						
			else:
				option.hovered = False
			
			option.draw()
			score = 0
		pygame.display.flip()
		clock.tick(30)	
		pygame.display.update()
	
