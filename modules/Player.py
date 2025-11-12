
from modules.Game_obj import Game_obj
from modules.Laser import Laser
from modules.Loader import image_loader
import pygame

class Player (Game_obj):
	def __init__ ( self, group, anchor, pos, image_src ):
		Game_obj.__init__(self, group, anchor, pos, image_src)
		self.__group = group

		self.direction = pygame.math.Vector2()
		self.__laser_image = image_loader('laser.png')
		self.speed = 300

		self.is_allowed_to_shoot = True
		self.__since_last_shot = 0
		self.cooldown = 400

	def __move ( self, dt ):
		self.rect.center += self.direction * self.speed * dt
	
	def __set_direction ( self, keys ):
		self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
		self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
		self.direction = self.direction.normalize() if self.direction else self.direction
	
	def __fire_laser ( self, keys ):
		if ( not keys[pygame.K_SPACE] or not self.is_allowed_to_shoot ):
			return
		self.is_allowed_to_shoot = False
		self.__since_last_shot = pygame.time.get_ticks()
		Laser(self.__group, 'midbottom', self.rect.midtop, self.__laser_image)

	def set_is_allowed_to_shot ( self ):
		current_time = pygame.time.get_ticks()
		self.is_allowed_to_shoot = current_time - self.__since_last_shot >= self.cooldown 

	def update ( self, dt ):
		keys = pygame.key.get_pressed()
		self.__set_direction(keys)
		self.__move(dt)
		self.__fire_laser(keys)
		self.set_is_allowed_to_shot()