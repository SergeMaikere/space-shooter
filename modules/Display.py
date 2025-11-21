import pygame

class Display:

	def __init__ ( self, width, height, text='Add caption' ):
		self.width = width  
		self.height = height  
		self.dims = { 'w': self.width, 'h': self.height }
		self._caption = self.__set_init_caption(text)
		self.image = pygame.display.set_mode( (self.width, self.height) )

	@property
	def caption ( self ):
		return self._caption

	@caption.setter
	def caption ( self, text ):
		self._caption = text
		pygame.display.set_caption(self._caption)

	def __set_init_caption ( self, text ):
		pygame.display.set_caption(text)
		return text

	def set_background_color ( self, color ):
		self.image.fill(color)
