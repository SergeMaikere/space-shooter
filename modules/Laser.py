from modules.Game_obj import Game_obj_clone

class Laser ( Game_obj_clone ):
	def __init__ ( self, group, anchor, pos, image ):
		super().__init__(group, anchor, pos, image)
		self.speed = 400

	def update ( self, dt ):
		self.rect.y < 0 and self.kill()
		self.rect.y -= self.speed * dt