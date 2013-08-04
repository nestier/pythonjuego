import pygame

class Option(object):

	hovered = False
	def __init__(self, text, pos):
		self.text = text
		self.pos = pos
		self.set_rect()
		self.draw()
			
	def draw(self):
		self.set_rend()
		screen.blit(self.rend, self.rect)
	
	def set_rend(self):
		self.rend = menu_font.render(self.text, True, self.get_color())
	
	def get_color(self):
		if self.hovered:
			return (255, 255, 255)
		else:
			return (0, 0, 0)
	
	def set_rect(self):
		self.set_rend()
		self.rect = self.rend.get_rect()
		self.rect.topleft = self.pos

def iniciarpantalla():
		pygame.init()
		screen_width = 800
		screen_height = 450
		screen=pygame.display.set_mode([screen_width,screen_height])
		return screen

screen = iniciarpantalla()
menu_font = pygame.font.Font(None, 40)
