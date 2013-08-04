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
		menu_font = pygame.font.Font(None, 80)
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
	x = open('puntajes/'+nom,'w')
	pickle.dump(lista, x)


def guardarpuntaje(obj, punt, nombre):
	nom=[obj[0].getletra()+obj[1].getletra()+obj[2].getletra(),punt]
	lista=[]
	lista=Funciones.abrirarchivo('puntajes/'+nombre)
	aux=[]
	for obj in lista:
		if obj[1]< nom[1]:
			aux=nom[:]
			nom[0]=obj[0]
			nom[1]=obj[1]
			obj[0]=aux[0]
			obj[1]=aux[1]				
	guardararchivo(lista,nombre)
			
def compararpuntaje(punt, nom):
	nombre=	"puntajes/"+nom
	lista=Funciones.abrirarchivo(nombre)
	
	for obj in lista:
		if obj[1] < punt:
			return True
	return False		

def confondo(screen, band, fondo):
	if band:
		screen.fill(white)
	else:
		screen.blit(fondo, (0,0))

def mostrarpuntajes(nom, screen):
	nombre= nombre=	"puntajes/"+nom
	lista=Funciones.abrirarchivo(nombre)
	fon = pygame.font.SysFont(None, 40)
	listo=Option("Volver", (340,285))
	band = False
	try:
		fondo = pygame.image.load("image/mapa-mundi.jpg")
	except pygame.error:
		band = True	
	done=False
	while not done:
		x=250
		y=50
		cont=0
		pygame.event.pump()
		confondo(screen, band, fondo)
		for puntajes in lista:
			cont+=1
			if cont == 6:
				x=450
				y=50
			texto = fon.render(str(puntajes[0])+' '+str(puntajes[1]), True, (0,0,0))
			screen.blit(texto, (x, y))
			y+=50
		if listo.rect.collidepoint(pygame.mouse.get_pos()):
			listo.hovered = True	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
					break
				if(event.type == pygame.MOUSEBUTTONDOWN):
					done=True	
		listo.draw()		
		pygame.display.update()

def escribirnombre(screen,puntaje,nombre):
	band = False
	clock = pygame.time.Clock()
	try:
		fondo = pygame.image.load("image/mapa-mundi.jpg")
	except pygame.error:
		band = True	
	menu_font = pygame.font.Font(None, 40)
	fon = pygame.font.SysFont(None, 40)         		
	options = [Option2("1", (240, 205)), Option2("2", (340, 205)),
			Option2("3", (440, 205)),Option("listo",(340,265))]
	done = False
	texto = fon.render('Haga clik en las letras para escribir su nombre', True, (0,0,0))
	while not done:
		pygame.event.pump()
		confondo(screen, band, fondo)
		screen.blit(texto, (100, 150))
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
	
