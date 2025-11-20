import pygame
from modules.Game_obj import Game_obj
from modules.Explosion import Explosion
from modules.Groups import all_sprites

class Laser ( Game_obj ):
	def __init__ ( self, anchor, pos, image ):
		super().__init__(all_sprites, anchor, pos, image)
		self.speed = 400

	def __dies_of_screen ( self ):
		self.rect.bottom < 0 and self.kill()

	def __on_meteor_collision ( self, meteor_sprites ):
		if pygame.sprite.spritecollide(self, meteor_sprites, True):
			Explosion(self.rect.midtop)
			self.kill()


	def __move ( self, dt ):
		self.rect.top -= self.speed * dt

	

	def update ( self, bag_of_tricks ):
		self.__dies_of_screen()
		self.__on_meteor_collision(bag_of_tricks['meteor_sprites'])
		self.__move(bag_of_tricks['dt'])