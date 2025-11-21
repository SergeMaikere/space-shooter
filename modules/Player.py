import pygame
from modules.Game_obj import Game_obj
from modules.Laser import Laser
from modules.Loader import image_loader
from modules.Groups import all_sprites


class Player (Game_obj):
	def __init__ ( self, anchor, pos ):
		super().__init__(all_sprites, anchor, pos, image_loader('player.png'))
		self.direction = pygame.math.Vector2()
		self.speed = 300

		self.__laser_image = image_loader('laser.png')
		self.is_allowed_to_shoot = True
		self.__since_last_shot = 0
		self.cooldown = 400
		self.e_game_over = pygame.event.custom_type()

	def __move ( self, dt ):
		self.rect.center += self.direction * self.speed * dt
	
	def __set_direction ( self, keys ):
		self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
		self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
		self.direction = self.direction.normalize() if self.direction else self.direction
	
	def __fire_laser ( self, keys, laser_sound ):
		if ( not keys[pygame.K_SPACE] or not self.is_allowed_to_shoot ):
			return
		
		self.__reset_shooting_cooldown()
		Laser('midbottom', self.rect.midtop, self.__laser_image)
		self.__set_laser_sound(laser_sound)

	def __reset_shooting_cooldown ( self ):
		self.is_allowed_to_shoot = False
		self.__since_last_shot = pygame.time.get_ticks()


	def __set_laser_sound ( self, laser_sound ):
		laser_sound.set_volume(0.4)
		laser_sound.play()

	def __set_is_allowed_to_shot ( self ):
		current_time = pygame.time.get_ticks()
		self.is_allowed_to_shoot = current_time - self.__since_last_shot >= self.cooldown 

	def __game_over ( self, meteor_sprites ):
		if pygame.sprite.spritecollide(self, meteor_sprites, True, pygame.sprite.collide_mask):
			pygame.event.post(pygame.event.Event(self.e_game_over))


	def update ( self, helper ):
		keys = pygame.key.get_pressed()
		self.__set_direction(keys)
		self.__move(helper['dt'])
		self.__fire_laser(keys, helper['game_sounds']['laser'])
		self.__set_is_allowed_to_shot()
		self.__game_over(helper['meteor_sprites'])