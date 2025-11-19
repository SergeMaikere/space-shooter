import pygame
from modules.Game_obj import Game_obj
from numpy import random

class Meteor ( Game_obj ):
	def __init__ ( self, group, anchor, pos, image, dims ):
		super().__init__(group, anchor, pos, image)
		self.rotation = 0
		self.rotation_speed = random.uniform(-30, 30)
		self.speed = random.uniform(100, 200)
		self.direction = pygame.math.Vector2((random.uniform(-0.5, 0.5), 1))
		self.screen_dimensions = dims

	def __die_off_screen ( self ):
		self.rect.top > self.screen_dimensions['h'] and self.kill()

	def __move ( self, dt ):
		self.rect.center += self.direction * self.speed * dt

	def __rotate ( self, dt ):
		self.rotation += self.rotation_speed * dt
		self.image = pygame.transform.rotozoom(self._og_image, self.rotation, 1)

	def update ( self, dt, meteor_sprite, screen_image ):
		self.__rotate(dt)
		self.__move(dt)
		self.__die_off_screen()