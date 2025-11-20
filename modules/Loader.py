import pygame
from os.path import join
from modules.Helper import pipe

load_image = lambda name: pygame.image.load( join('assets', 'images', name) )

load_explosion = lambda n: pygame.image.load( join('assets','images', 'explosion', f'{n}.png') )

convert_image = lambda surface: surface.convert_alpha()

load_font = lambda name, size: pygame.font.Font( join('assets', 'images', name ), size )

get_font_image = lambda text, color, font: font.render(text, True, color)

image_loader = pipe(load_image, convert_image)

explosion_loader = pipe(load_explosion, convert_image)
