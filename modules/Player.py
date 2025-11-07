
from modules.Game_obj import Game_obj
import pygame

class Player (Game_obj):
	def __init__ ( self, anchor, pos, image_src ):
		Game_obj.__init__(self, anchor, pos, image_src)
		self.direction = pygame.math.Vector2()
		self.speed = 300

	
	def set_direction ( self ):
		keys = pygame.key.get_pressed()
		self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
		self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
		self.direction = self.direction.normalize() if self.direction else self.direction


	def move ( self, dt ):
		self.rect.center += self.direction * self.speed * dt
