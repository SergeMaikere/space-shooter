import pygame

class Display:

	def __init__ ( self, width, height ):
		self.width = width  
		self.height = height  
		self.__caption = None
		self.image = pygame.display.set_mode( (self.width, self.height) )


	def set_caption ( self, text ):
		self.__caption = text
		pygame.display.set_caption(self.__caption)

	def set_background ( self ):
		self.image.fill('#3a2e3f')

	def get_dimensions ( self ):
		return { 'w': self.width, 'h': self.height }
