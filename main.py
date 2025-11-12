import pygame
from modules.Display_surface import Display
from modules.Game_obj import Game_obj, Game_obj_clone
from modules.Player import Player
from modules.Helper import get_random_pos
from modules.Loader import load_image


def set_starry_sky ( group ):
	positions = [get_random_pos(screen.width, screen.height) for i in range(20)]
	star_image = load_image('star.png')
	return [ Game_obj_clone(group, 'center', pos, star_image) for pos in positions ]

pygame.init()

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

screen = Display(1280, 720)
screen.set_caption('Space Shooter III - Revenge Of The Bit')

stars = set_starry_sky(all_sprites)
meteor = Game_obj(all_sprites, 'center', (screen.width/2, screen.height/2), 'meteor.png')
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
