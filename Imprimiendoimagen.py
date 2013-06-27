
import pygame
import random
import time
import pickle
black = ( 0, 0, 0)
white = ( 255, 255, 255)
red = ( 255, 0, 0)

class Block(pygame.sprite.Sprite):

	def __init__(self, width, height,name,pareja):
		pygame.sprite.Sprite.__init__(self)
		self.nombre = name
		self.pareja = pareja
		self.imagen=pygame.image.load("index.jpeg")
		self.color=black
		self.image = pygame.Surface([width, height])
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		
					
	def mostrarcara(self):
		self.image.blit(self.imagen, (0,0))
		fuente=pygame.font.SysFont(None,25)
		x=len(self.nombre)-1
		margen=15
		altura=50
		if x < 10:
			margen=30	
		if x > 13 :
			nombre=fuente.render(self.nombre[:13],True,(black))
			self.image.blit(nombre,(margen, altura))
			nom=fuente.render(self.nombre[13:],True,(black))
			self.image.blit(nom,(margen, altura+25))
		else:
			nombre=fuente.render(self.nombre,True,(black))	
			self.image.blit(nombre,(margen, altura))
			
	def mostrarlomo(self):
		self.image.fill(self.color)		
	
				
	def comparar(self,obj):
		if self.nombre == obj.pareja:
			return True
		else: return False	
		
def iniciarpantalla():
		pygame.init()
		screen_width=800
		screen_height=650
		screen=pygame.display.set_mode([screen_width,screen_height])
		return screen

def abrirarchivo(nom):
	arch=[]
	x=open(nom,'r')
	arch=pickle.load(x)
	x.close()
	return arch

def crearcordenadas():
	l=[]
	y=0
	for i in range(0,4):
		x=150
		for j in range(0,4):
			aux=[]
			aux.append(x)
			aux.append(y)
			x=x+150+10
			l.append(aux)
		y=y+160		
	return l
	
def crearcartas(nom):
	l=[]
	cord=crearcordenadas()
	parejas=abrirarchivo(nom)
	aux=len(parejas)-1
	aux2=15
	for i in range(8):
		ran=random.randint(0,aux)
		ran2=random.randint(0,aux2)
		block = Block(150, 150,parejas[ran][0],parejas[ran][1])
		block.rect.x = cord[ran2][0]
		block.rect.y = cord[ran2][1]
		cord.remove(cord[ran2])
		aux2=aux2-1
		ran2=random.randint(0,aux2)
		l.append(block)
		block =Block( 150, 150,parejas[ran][1],parejas[ran][0])
		block.rect.x = cord[ran2][0]
		block.rect.y = cord[ran2][1]
		cord.remove(cord[ran2])
		parejas.remove(parejas[ran])
		l.append(block)
		aux2=aux2-1
		aux=aux-1
	return l	

def borrarportiempo(lista,lista2):
	aux=len(lista)-1
	ran=random.randint(0,aux)	
	pareja=lista[ran].pareja
	for i in lista :
		if pareja == i.nombre:
			obje=i
	lista2.remove(lista[ran])		
	lista.remove(lista[ran])
	lista.remove(obje)
	lista2.remove(obje)

def nivel(nom,score,screen):	
	listaobjetos=[]
	fon=pygame.font.SysFont(None,50)
	fuente=pygame.font.SysFont(None,35)
	sup=fon.render("Puntaje",True,(0,0,0))
	block_list = pygame.sprite.Group()
	listaobjetos=crearcartas(nom)
	for objeto in listaobjetos:
		block_list.add(objeto)
	player = Block( 5, 5,'','')
	done=False
	clock=pygame.time.Clock()
	cont=0
	doble=0
	tiempo=time.time()
	# -------- Main Program Loop -----------
	while listaobjetos and not done:
		puntaje=fon.render(str(score),True,(0,0,0))
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				done=True 
		screen.fill(white)
		pos = pygame.mouse.get_pos()
		player.rect.x=pos[0]
		player.rect.y=pos[1]
		ev = pygame.event.wait()
		if(ev.type == pygame.MOUSEBUTTONDOWN): 
			blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
			if blocks_hit_list:
				block=blocks_hit_list[0]
				
				cont=cont+1
				block.mostrarcara()
				if cont != 2:
					aux=block
					block_list.draw(screen)
				else:
					cont=0
					screen.blit(sup,(10,0))
					screen.blit(puntaje,(60,30))
					block_list.draw(screen)
					s=time.time()
					e=s+0.35
					while time.time() < e :
						pygame.display.flip()
						clock.tick(30)
					if block.comparar(aux) :
						if time.time() < doble+3:
							score+=100
						doble=time.time()
						score +=100
						block_list.remove(aux)
						block_list.remove(block)
						listaobjetos.remove(aux)
						listaobjetos.remove(block)
						aux=None
					else:
						aux.mostrarlomo()
						block.mostrarlomo()
						aux=None
		if time.time() > tiempo+30:
			borrarportiempo(listaobjetos,block_list)
			tiempo=time.time()
		screen.blit(sup,(10,0))
		screen.blit(puntaje,(60,30))
		block_list.draw(screen)
		clock.tick(30)
		pygame.display.flip()
	return score	

screen=iniciarpantalla()
score=0
niveles=['provincias','sudamerica']
opcion=input('ingrese el nivel que desea jugar 1)provincias 2)sudamerica 3)todos')
opcion=opcion-1
if opcion < 2 :
	score= nivel(niveles[opcion],score,screen)
if opcion ==2:
	for i in niveles:
		score=nivel(i,score,screen)
print score					
pygame.quit()
