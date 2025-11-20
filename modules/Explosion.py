import pygame
from modules.Game_obj import Game_obj
from modules.Groups import all_sprites
from modules.Loader import explosion_loader
from modules.Helper import set_rect

class Explosion ( pygame.sprite.Sprite ):
	def __init__( self, pos ):
		super().__init__(all_sprites)
		self.frames_i = 0
		self.image = explosion_loader(0)
		self.rect = set_rect('center', pos, self.image)

	def update ( self, helper ):
		self.frames_i += int(20 * helper['dt']) or 1
		
		if self.frames_i >= len(helper['frames']): 
			self.kill()
		else:
			self.image = helper['frames'][self.frames_i]