from modules.Game_obj import Game_obj_clone
from modules.Helper import get_random_pos

class Star ( Game_obj_clone ):
	def __init__ ( self, group, anchor, dims, image ):
		super().__init__(group, anchor, get_random_pos(dims['w'], dims['h']), image)
