from modules.Helper import add_to_surface, get_random_pos
from modules.Loader import image_loader
import pygame

class Display:

	def __init__ ( self, pygame, width, height ):
		self.width = width  
		self.height = height  
		self.__caption = None
		self.surface = pygame.display.set_mode( (self.width, self.height) )
		self.positions = [ get_random_pos(self.width, self.height) for i in range(20) ]


	def set_caption ( self, text ):
		self.__caption = text
		pygame.display.set_caption(self.__caption)

	def set_background ( self ):
		self.surface.fill('darkgrey')
		star = image_loader('star.png')
		for i in range(20):
			self.surface.blit(star, self.positions[i])

	def add_game_obj ( self, game_obj ):
		return add_to_surface(self.surface, game_obj)


