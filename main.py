import pygame
from numpy import random
from modules.Display_surface import Display
from modules.Meteor import Meteor
from modules.Star import Star
from modules.Player import Player
from modules.Helper import set_repeating_event
from modules.Loader import load_image


def set_starry_sky ( group ):
	star_image = load_image('star.png')
	for i in range(20):
		Star(group, 'center', screen.get_dimensions(), star_image)

pygame.init()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

screen = Display(1280, 720)
screen.set_caption('Space Shooter III - Revenge Of The Bit')

stars = set_starry_sky(all_sprites)

meteor = load_image('meteor.png')
e_meteor = set_repeating_event(600)

player = Player(all_sprites, 'midleft', (screen.width/2, screen.height/2), 'player.png')


running = True
while running:
	dt = clock.tick(120) / 1000

	# Event loop
	for event in pygame.event.get():
		running = not event.type == pygame.QUIT

		if event.type == e_meteor:
			Meteor( all_sprites, 'midbottom', (random.randint(0, screen.width), 0), meteor, screen.get_dimensions() )
	
	# Background
	screen.set_background()

	# Update all behaviours
	all_sprites.update(dt)

	# Add game objs to screen
	all_sprites.draw(screen.image)

	pygame.display.update()

pygame.quit()
