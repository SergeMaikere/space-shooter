import pygame
from numpy import random
from modules.Display_surface import Display
from modules.Meteor import Meteor
from modules.Star import Star
from modules.Player import Player
from modules.Score import Score
from modules.Helper import set_repeating_event
from modules.Loader import image_loader, explosion_loader, sounds_loader, sounds
from modules.Groups import all_sprites, meteor_sprites


def set_starry_sky ():
	star_image = image_loader('star.png')
	for i in range(20):
		Star(screen.get_dimensions(), star_image)

def set_game_music ( sound ):
	sound.play(loops=-1)
	sound.set_volume(0.4)

pygame.init()
clock = pygame.time.Clock()

screen = Display(1280, 720)
screen.set_caption('Space Shooter III - Revenge Of The Bit')

set_starry_sky()
 
meteor = image_loader('meteor.png')
e_meteor = set_repeating_event(600)

player = Player('midleft', (screen.width/2, screen.height/2))

score = Score((screen.width/2, screen.height - 50))

frames = [ explosion_loader(i ) for i in range(21) ]

game_sounds = sounds_loader(sounds)

set_game_music(game_sounds['game_music'])

update_sprites_args = {
	'meteor_sprites': meteor_sprites, 
	'screen_image': screen.image, 
	'frames': frames, 
	'game_sounds': game_sounds
}

running = True
while running: 
	update_sprites_args['dt'] = clock.tick(60) / 1000

	# Event loop
	for event  in pygame.event.get():
		running = not event.type == pygame.QUIT and not event.type == player.e_game_over

		if event.type == e_meteor:
			Meteor( (all_sprites, meteor_sprites), 'midbottom', (random.randint(0, screen.width), 0), meteor, screen.get_dimensions() )
	
	# Background
	screen.set_background()

	# Update all behaviours
	all_sprites.update(update_sprites_args)

	# Add game objs to screen
	all_sprites.draw(screen.image)

	pygame.display.update()

pygame.quit()
