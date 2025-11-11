import pygame
from modules.Display_surface import Display
from modules.Game_obj import Game_obj
from modules.Player import Player
from modules.Helper import get_random_pos


def set_starry_sky ():
	positions = [get_random_pos(screen.width, screen.height) for i in range(20)]
	return [ Game_obj(all_sprites, 'center', pos, 'star.png') for pos in positions ]

pygame.init()

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

screen = Display(1280, 720)
screen.set_caption('Space Shooter III - Revenge Of The Bit')

stars = set_starry_sky()
meteor = Game_obj(all_sprites, 'center', (screen.width/2, screen.height/2), 'meteor.png')
laser = Game_obj(all_sprites, 'bottomleft', (20, screen.height - 20), 'laser.png')
player = Player(all_sprites, 'midleft', (screen.width/2, screen.height/2), 'player.png')


running = True
while running:
	dt = clock.tick(120) / 1000

	# Event loop
	for event in pygame.event.get():
		running = not event.type == pygame.QUIT
	
	# Background
	screen.set_background()

	# Update all behaviours
	all_sprites.update(dt)

	# Add game objs to screen
	all_sprites.draw(screen.image)

	pygame.display.update()

pygame.quit()
