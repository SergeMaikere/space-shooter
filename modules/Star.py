from modules.Game_obj import Game_obj
from modules.Groups import all_sprites
from modules.Helper import get_random_pos

class Star ( Game_obj ):
	def __init__ ( self, dims, image ):
		super().__init__(all_sprites, 'center', get_random_pos(dims['w'], dims['h']), image)
