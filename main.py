import pygame
from modules.Loader import image_loader
from modules.Helper import set_rect, add_to_surface, pipe, curry, get_random_pos, is_out_of_bound

# General setup


# Utils functions
def setScreen ( w, h ):
	screen = pygame.display.set_mode((w, h))
	pygame.display.set_caption('Space Shooter I - Revenge Of The Bit')	
	return screen

def setBackground ( screen, positions ):
	screen.fill('darkgray')
	star = image_loader('star.png')
	for i in range(20):
		screen.blit(star, positions[i])

def set_game_obj (anchor, pos, src):
	return pipe(
		[
			image_loader,
			curry(set_rect)(anchor, pos),
		]
	)(src)

def move_player ( width, direction, player ):
	player["rect"].x += direction 
	return player



WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
screen = { "width": WINDOW_WIDTH, "height": WINDOW_HEIGHT, "surface": None }

pygame.init()

screen["surface"] = setScreen(screen['width'], screen['height'])
positions = [ get_random_pos(screen["width"], screen["height"]) for i in range(20) ]
add_to_screen = curry(add_to_surface)(screen["surface"])

player = set_game_obj('midleft', (0, screen["height"]/2), 'player.png')
meteor = set_game_obj('center', (screen["width"]/2, screen["height"]/2), 'meteor.png')
laser = set_game_obj('bottomleft', (20, screen["height"] - 20), 'laser.png')

direction = 1
running = True
while running:
	# Event loop
	for event in pygame.event.get():
		running = not event.type == pygame.QUIT

	# Directing direction
	direction *= ( -1 if is_out_of_bound(player["rect"], screen["width"]) else 1 )

	# Background
	setBackground(screen["surface"], positions)
	
	# Add game objs to screen
	add_to_screen(meteor)
	add_to_screen(laser)	
	pipe( 
		[ 
			curry(move_player)(screen["width"], direction),
			add_to_screen
		] 
	)(player)
	
	pygame.display.update()

pygame.quit()
