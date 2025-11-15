import pygame
from modules.Game_obj import Game_obj_font
from modules.Loader import get_font_image

class Score ( Game_obj_font ):
	def __init__( self, pos ):
		super().__init__( pos, 'Oxanium-Bold.ttf', '0', '#ffffff', 42 )
		self.offset = pygame.time.get_ticks()


	def __set_score_timer ( self ):
		self.set_text( str((pygame.time.get_ticks() - self.offset) // 100) )

	def __set_score_rect ( self, screen_image ):
		pygame.draw.rect(screen_image, (240, 240, 240), self.rect.inflate(30, 15).move(0, -6), 5, 10)

	def update ( self, dt, meteor_sprites, screen_image ):
		self.__set_score_timer()
		self.__set_score_rect(screen_image)