import pygame
from numpy import random
from modules.Display import Display
from modules.Meteor import Meteor
from modules.Star import Star
from modules.Player import Player
from modules.Score import Score
from modules.Helper import set_repeating_event
from modules.Loader import image_loader, explosion_loader, sounds_loader, sounds
from modules.Groups import all_sprites, meteor_sprites



# Utils

initate_time = lambda: pygame.time.Clock()

set_meteors = lambda: ( image_loader('meteor.png'), set_repeating_event(300) )

get_random_pos_top_screen = lambda width: ( random.randint(0, width), 0 )

time_to_quit_the_game = lambda event, e_game_over:  event.type == pygame.QUIT or event.type == e_game_over

make_new_meteor = lambda dims, meteor_image: Meteor( get_random_pos_top_screen(dims['w']), meteor_image, dims )

def set_starry_sky (dims):
	star_image = image_loader('star.png')
	return [ Star(dims, star_image) for i in range(20) ]

def set_game_music ( sound ):
	sound.play(loops=-1)
	sound.set_volume(0.4)




# Create Game loop elements

pygame.init()

clock = initate_time()

screen = Display(1280, 720, 'Space Shooter III - Revenge Of The Bit')

stars = set_starry_sky(screen.dims)
 
meteor_image, e_meteor = set_meteors()

player = Player('midleft', (screen.width/2, screen.height/2))

score = Score((screen.width/2, screen.height - 50))

frames = [ explosion_loader(i ) for i in range(21) ]

game_sounds = sounds_loader(sounds)

update_sprites_args = {
	'meteor_sprites': meteor_sprites, 
	'screen_image': screen.image, 
	'frames': frames, 
	'game_sounds': game_sounds
}

set_game_music(game_sounds['game_music'])



# Game Loop

running = True
while running: 

	# delta-time of a single frame in sec 
	# Is necessary for homogenus sprite movement speed accross all machines
	update_sprites_args['dt'] = clock.tick() / 1000

	# Event loop
	for event  in pygame.event.get():
		running = not time_to_quit_the_game(event, player.e_game_over)

		if event.type == e_meteor:
			make_new_meteor(screen.dims, meteor_image)
	
	# Background
	screen.set_background_color('#3a2e3f')

	# Update all behaviours
	all_sprites.update(update_sprites_args)

	# Add game elements to display screen
	all_sprites.draw(screen.image)

	pygame.display.update()

pygame.quit()
