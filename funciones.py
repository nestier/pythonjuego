import pygame
import random
import time
import pickle
import puntajes
import error

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

class Block(pygame.sprite.Sprite):

	def __init__(self, width, height,name,pareja,escapital):
		pygame.sprite.Sprite.__init__(self)
		self.nombre = name
		self.escapital = escapital
		self.pareja = pareja
		try:
			self.imagen = self.__imagenes()
		except pygame.error:
			self.imagen = pygame.image.load("image/index.jpeg")
		try:
			self.fondo = pygame.image.load("image/fondo.jpeg")
		except pygame.error:
			self.fondo = None
		self.color = black
		self.image = pygame.Surface([width, height])
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.mostrarlomo()
		
	def __imagenes(self):
		if self.escapital:
			return pygame.image.load("image/"+self.pareja+".jpeg")
		else:
			return pygame.image.load("image/"+self.nombre+".jpeg")
			
	def mostrarcara(self):
		self.image.blit(self.imagen, (0, 0))
		fuente = pygame.font.SysFont(None, 22)
		x = len(self.nombre)
		if x < 12 :
			altura = 30
		else:
			altura = 10
		margen = 2
		l = []
		palabra = ''
		for c in self.nombre:
			if c == ' ':
				l.append(palabra)
				palabra = ''
			else:
				if c == '_':
					c = ' '
				palabra += c
		l.append(palabra)
		for i in l:
			if len(i) > 6:
				margen = 2
			else:
				margen = 20
			nombre = fuente.render(i, True, (black))
			self.image.blit(nombre, (margen, altura))
			altura += 20
		
	def mostrarlomo(self):
		if self.fondo != None:
			self.image.blit(self.fondo, (0,0))
		else:
			self.image.fill(self.color)

	def comparar(self, obj):
		if self.nombre == obj.pareja:
			return True
		else: return False

		
def iniciarpantalla():
		pygame.init()
		screen_width = 800
		screen_height = 650
		screen = pygame.display.set_mode([screen_width, screen_height])
		return screen

def abrirarchivo(nom):
	arch = []
	x = open(nom,'r')
	arch = pickle.load(x)
	x.close()
	return arch

def crearcordenadas(rango, tam, can):
	l = []
	y = 0
	if can > 16:
		aux1 = rango / 2
		aux2 = 6
	elif can == 8:
		aux2 = can / 2
		aux1 = 2
	else:
		aux1 = 6
		aux2 = rango / 2
	
	for i in range(aux1):
		x = 150
		for j in range(aux2):
			aux = []
			aux.append(x)
			aux.append(y)
			x = x + tam + 10
			l.append(aux)
		y = y + tam + 10
			
	return l
	
def crearcartas(nom, can):
	l = []
	tam = 100
	rango = can / 2
	cord = crearcordenadas(rango, tam , can)
	parejas = abrirarchivo("nivel/"+nom)
	aux = len(parejas) - 1
	can = can - 1
	for i in range(rango):
		ran = random.randint(0, aux)
		ran2 = random.randint(0, can)
		block = Block(tam, tam, parejas[ran][0], parejas[ran][1], False)
		block.rect.x = cord[ran2][0]
		block.rect.y = cord[ran2][1]
		cord.remove(cord[ran2])
		can -= 1
		ran2 = random.randint(0, can)
		l.append(block)
		block = Block( tam, tam, parejas[ran][1], parejas[ran][0], True)
		block.rect.x = cord[ran2][0]
		block.rect.y = cord[ran2][1]
		cord.remove(cord[ran2])
		parejas.remove(parejas[ran])
		l.append(block)
		can -= 1
		aux -= 1
	return l

def borrarportiempo(lista, lista2):
	aux = len(lista) - 1
	ran = random.randint(0, aux)
	pareja = lista[ran].pareja
	dif = lista[ran].escapital
	for i in lista :
		if pareja == i.nombre:
			if dif != i.escapital:
				obje = i
	lista2.remove(lista[ran])
	lista.remove(lista[ran])
	lista.remove(obje)
	lista2.remove(obje)
	
def confondo(screen):
	band=False
	try:
		fondo = pygame.image.load("image/mapa-mundi.jpg")
	except pygame.error:
		band = True
	if band:
		screen.fill(white)
	else:
		screen.blit(fondo, (0,0))

def terminarnivel(score, nom, screen):	
	siguiente = True
	highscore=puntajes.compararpuntaje(score, nom)
	fon = pygame.font.SysFont(None, 30)
	while siguiente:
		if highscore:
			texto = fon.render('Su puntaje es: ' + str(score)+' usted a alcanzado un maximo puntaje', True, black)
			texto1 = fon.render('Haga click para continuar', True, black)
		else:
			texto = fon.render('Su puntaje es: ' + str(score), True, black)
			texto1 = fon.render('Haga click para continuar', True, black)	
		for event in pygame.event.get():
			confondo(screen)
			screen.blit(texto, (150, 150))
			screen.blit(texto1, (280, 330))
			pygame.display.flip()
			if(event.type == pygame.MOUSEBUTTONDOWN):
				if highscore:
					puntajes.escribirnombre(screen, score, nom)
				siguiente = False

def nivel(nom, score, screen, cantidad):	
	try:	
		listaobjetos = []
		fon = pygame.font.SysFont(None, 30)
		fuente = pygame.font.SysFont(None, 35)
		sup = fon.render("PUNTOS", True, (0, 0, 0))
		block_list = pygame.sprite.Group()
		listaobjetos = crearcartas(nom, cantidad)
		for objeto in listaobjetos:
			block_list.add(objeto)
		player = Block( 5, 5, '', '', False)
		done = False
		clock = pygame.time.Clock()
		cont = 0
		doble = 0
		reloj = time.time()
		combo = ''
		tiempoborrar = 30
		confondo(screen)
		# -------- Main Program Loop -----------
		while listaobjetos and not done:
			confondo(screen)
			puntaje = fon.render(str(score), True, black)
			seborra = fon.render('Se borra en', True, black)
			tborrar = fon.render(str(tiempoborrar), True, black)
			com = fon.render(combo, True, black)
			if (time.time() - reloj) > 1:
				reloj = time.time()
				tiempoborrar -= 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True 
				confondo(screen)
				pos = pygame.mouse.get_pos()
				player.rect.x = pos[0]
				player.rect.y = pos[1]
				if(event.type == pygame.MOUSEBUTTONDOWN):
					blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
					if blocks_hit_list:
						block = blocks_hit_list[0]
						cont += 1
						block.mostrarcara()
						if cont != 2:
							aux = block
							block_list.draw(screen)
						else:
							cont = 0
							screen.blit(com, (10, 100))
							screen.blit(sup, (30, 0))
							screen.blit(puntaje, (60, 20))
							screen.blit(seborra, (10, 50))
							screen.blit(tborrar, (50, 70))
							block_list.draw(screen)
							s = time.time()
							e = s + 0.35
							while time.time() < e :
								pygame.display.flip()
								clock.tick(30)
							if time.time() > doble + 3:
								combo = ''
							if block.comparar(aux) :
								combo = 'COMBOx2'
								if time.time() < doble + 3:
									score += 100
								doble = time.time()
								score += 100
								block_list.remove(aux)
								block_list.remove(block)
								listaobjetos.remove(aux)
								listaobjetos.remove(block)
								aux = None
							else:
								aux.mostrarlomo()
								block.mostrarlomo()
								aux = None
			if tiempoborrar == 0:
				borrarportiempo(listaobjetos, block_list)
				tiempoborrar = 30
			screen.blit(com, (10, 100))
			screen.blit(seborra, (10, 50))
			screen.blit(tborrar, (50, 70))
			screen.blit(sup, (30, 0))
			screen.blit(puntaje, (60, 20))
			block_list.draw(screen)
			clock.tick(30)
			pygame.display.flip()
			pygame.display.update()
		return score
	except :
		error.mensaje(screen)	
