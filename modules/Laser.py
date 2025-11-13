import pygame
from modules.Game_obj import Game_obj_clone

class Laser ( Game_obj_clone ):
	def __init__ ( self, group, anchor, pos, image ):
		super().__init__(group, anchor, pos, image)
		self.speed = 400

	def update ( self, dt, meteor_sprites ):
		self.rect.top -= self.speed * dt
		self.rect.bottom < 0 and self.kill()
		pygame.sprite.spritecollide(self, meteor_sprites, True) and self.kill()