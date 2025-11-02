from functools import reduce
from inspect import signature
from numpy import random

pipe = lambda funcs: lambda arg: reduce( lambda g, f: f(g), [arg] + funcs )


def curry ( fn ):
	def curried ( *args ):
		if len(args) >= len(signature(fn).parameters):
			return fn(*args)
		else:
			return lambda *args2: curried( *args, *args2 )
	return curried

get_random_pos = lambda w, h: ( random.randint(0, w), random.randint(0, h) )

def set_rect ( anchor, position, surface ):
	rect = None

	if anchor == 'topleft':
		rect = surface.get_rect(topleft=position)
	elif anchor == 'midtop':
		rect = surface.get_rect(midtop=position)
	elif anchor == 'topright':
		rect = surface.get_rect(topright=position)
	elif anchor == 'midright':
		rect = surface.get_rect(midright=position)
	elif anchor == 'bottomright':
		rect = surface.get_rect(bottomright=position)
	elif anchor == 'midbottom':
		rect = surface.get_rect(midbottom=position)
	elif anchor == 'bottomleft':
		rect = surface.get_rect(bottomleft=position)
	elif anchor == 'midleft':
		rect = surface.get_rect(midleft=position)
	else:
		rect = surface.get_rect(center=position)

	return { "surface": surface, "rect": rect }

is_out_of_bound = lambda rect, width: rect.left < 0 or rect.right > width

def add_to_surface (surface, my_obj): 
	surface.blit(my_obj["surface"], my_obj["rect"]) 
	return my_obj

def voyeur ( element ):
	print('\nSEEEERGE')
	print(element)
	print('\n')
	return element