from modules.Helper import set_rect
from modules.Loader import image_loader

class Game_obj:
	def __init__ ( self, anchor, pos, image_src ):
		self.anchor = anchor
		self.pos = pos
		self.image_src = image_src
		self.surface = image_loader(self.image_src)
		self.rect = set_rect(self.anchor, self.pos, self.surface)