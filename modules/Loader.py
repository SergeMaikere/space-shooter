import pygame
from os.path import join
from modules.Helper import pipe, curry, adjust_func_for_list_map, remove_format_from_file_name, add_keys_to_list, add_to_obj
from functools import reduce

sounds = [ 'explosion.wav', 'game_music.wav', 'laser.wav' ]

sounds_keys = adjust_func_for_list_map(remove_format_from_file_name)(sounds)

load_image = lambda name: pygame.image.load( join('assets', 'images', name) )

load_explosion = lambda n: pygame.image.load( join('assets','images', 'explosion', f'{n}.png') )

load_font = lambda name, size: pygame.font.Font( join('assets', 'images', name ), size )

load_sound = lambda name: pygame.mixer.Sound( join('assets', 'audio', name) )

load_sounds = lambda sounds : map(load_sound, sounds)

convert_image = lambda surface: surface.convert_alpha()

get_font_image = lambda text, color, font: font.render(text, True, color)


image_loader = pipe(load_image, convert_image)

explosion_loader = pipe(load_explosion, convert_image)

sounds_loader = pipe(
	adjust_func_for_list_map(load_sound),
	curry(add_keys_to_list)(sounds_keys),
	lambda my_sounds: reduce( add_to_obj, my_sounds, {} )
)
