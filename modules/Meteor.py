import pygame
from modules.Game_obj import Game_obj_clone
from numpy import random

class Meteor ( Game_obj_clone ):
	def __init__ ( self, group, anchor, pos, image, dims ):
		super().__init__(group, anchor, pos, image)
		self.speed = random.uniform(200, 500)
		self.direction = pygame.math.Vector2((random.uniform(-0.5, 0.5), 1))
		self.screen_dimensions = dims

	def update ( self, dt, meteor_sprite ):
		self.rect.top > self.screen_dimensions['h'] and self.kill()
		self.rect.center += self.direction * self.speed * dt