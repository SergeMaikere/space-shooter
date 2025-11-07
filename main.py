import pygame
from modules.Display_surface import Display
from modules.Game_obj import Game_obj
from modules.Player import Player


pygame.init()

clock = pygame.time.Clock()

screen = Display(pygame, 1280, 720)
screen.set_caption('Space Shooter III - Revenge Of The Bit')

player = Player('midleft', (screen.width/2, screen.height/2), 'player.png')
meteor = Game_obj('center', (screen.width/2, screen.height/2), 'meteor.png')
laser = Game_obj('bottomleft', (20, screen.height - 20), 'laser.png')


running = True
while running:
	dt = clock.tick(120) / 1000

	# Event loop
	for event in pygame.event.get():
		running = not event.type == pygame.QUIT

	# Background
	screen.set_background()

	# Specifies player movements
	player.set_direction()
	player.move(dt)

	# Add game objs to screen
	screen.add_game_obj(meteor)
	screen.add_game_obj(laser)	
	screen.add_game_obj(player)

	pygame.display.update()

pygame.quit()
