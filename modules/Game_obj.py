import pygame
from modules.Helper import set_rect
from modules.Loader import image_loader

class Game_obj ( pygame.sprite.Sprite ):
	def __init__ ( self, group, anchor, pos, image_src ):
		super().__init__(group)
		self.image = image_loader(image_src)
		self.rect = set_rect(anchor, pos, self.image)


class Game_obj_clone ( pygame.sprite.Sprite ):
	def __init__(self, group, anchor, pos, image):
		super().__init__(group)
		self.image = image
		self.rect = set_rect(anchor, pos, self.image)