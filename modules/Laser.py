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

	def __on_meteor_collision ( self, meteor_sprites, explosion_sound ):
		if pygame.sprite.spritecollide(self, meteor_sprites, True):
			Explosion(self.rect.midtop)
			self.kill()
			self.__set_eplosion_sound(explosion_sound)

	def __set_eplosion_sound ( self, explosion_sound ):
		explosion_sound.set_volume(0.4)
		explosion_sound.play()

	def __move ( self, dt ):
		self.rect.top -= self.speed * dt

	def update ( self, helper ):
		self.__dies_of_screen()
		self.__on_meteor_collision(helper['meteor_sprites'], helper['game_sounds']['explosion'])
		self.__move(helper['dt'])