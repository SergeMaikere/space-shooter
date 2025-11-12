
from modules.Game_obj import Game_obj
from modules.Laser import Laser
from modules.Loader import image_loader
import pygame

class Player (Game_obj):
	def __init__ ( self, group, anchor, pos, image_src ):
		Game_obj.__init__(self, group, anchor, pos, image_src)
		self.__group = group
		self.direction = pygame.math.Vector2()
		self.speed = 300
		self.__laser_image = image_loader('laser.png')

	def __move ( self, dt ):
		self.rect.center += self.direction * self.speed * dt
	
	def __set_direction ( self, keys ):
		self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
		self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
		self.direction = self.direction.normalize() if self.direction else self.direction
	
	def __fire_laser ( self, keys ):
		if ( not keys[pygame.K_SPACE] ):
			return
		Laser(self.__group, 'midbottom', self.rect.midtop, self.__laser_image)


	def update ( self, dt ):
		keys = pygame.key.get_pressed()
		self.__set_direction(keys)
		self.__move(dt)
		self.__fire_laser(keys)