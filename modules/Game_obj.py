import pygame
from modules.Helper import set_rect
from modules.Loader import load_font, get_font_image
from modules.Groups import all_sprites


class Game_obj ( pygame.sprite.Sprite ):
	def __init__(self, group, anchor, pos, image):
		super().__init__(group)
		self._og_image = image
		self.image = self._og_image
		self.rect = set_rect(anchor, pos, self.image)


class Game_obj_font ( pygame.sprite.Sprite ):
	def __init__(self, pos, font_src, text, color, size):
		super().__init__(all_sprites)
		self.font = load_font(font_src, size)
		self.color = color
		self.size = size
		self.pos = pos
		self.__text = text
		
		self.image = get_font_image(self.__text, self.color, self.font)
		self.rect = set_rect('midbottom', self.pos, self.image)

	def set_text ( self, text ):
		self.__text = text
		self.image = get_font_image(self.__text, self.color, self.font)
		self.rect = set_rect('midbottom', self.pos, self.image)


