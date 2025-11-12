from modules.Game_obj import Game_obj_clone

class Meteor ( Game_obj_clone ):
	def __init__ ( self, group, anchor, pos, image, dims ):
		super().__init__(group, anchor, pos, image)
		self.speed = 400
		self.screen_dimensions = dims

	def update ( self, dt ):
		self.rect.top > self.screen_dimensions['h'] and self.kill()
		self.rect.y += self.speed * dt