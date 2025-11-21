import pygame
from modules.Game_obj import Game_obj
from modules.Groups import all_sprites, meteor_sprites
from numpy import random

class Meteor ( Game_obj ):
	def __init__ ( self, pos, image, dims ):
		super().__init__((all_sprites, meteor_sprites), 'midbottom', pos, image)
		self.rotation = 0
		self.rotation_speed = random.uniform(-80, 80)
		self.speed = random.uniform(100, 200)
		self.direction = pygame.math.Vector2((random.uniform(-0.5, 0.5), 1))
		self.screen_dimensions = dims

	def __die_off_screen ( self ):
		if self.rect.top > self.screen_dimensions['h']:
			self.kill()

	def __move ( self, dt ):
		self.rect.center += self.direction * self.speed * dt

	def __rotate ( self, dt ):
		self.rotation += self.rotation_speed * dt
		self.image = pygame.transform.rotozoom(self._og_image, self.rotation, 1)
		self.rect = self.image.get_frect(center = self.rect.center) 

	def update ( self, helper ):
		self.__rotate(helper['dt'])
		self.__move(helper['dt'])
		self.__die_off_screen()