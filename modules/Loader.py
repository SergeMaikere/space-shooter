import pygame
from os.path import join
from modules.Helper import pipe

load_image = lambda name: pygame.image.load( join('assets', 'images', name) )

convert_image = lambda surface, alpha=True: surface.convert_alpha() if alpha else surface.convert()

image_loader = pipe(load_image, convert_image)

load_font = lambda name, size: pygame.font.Font( join('assets', 'images', name ), size )

get_font_image = lambda text, color, font: font.render(text, True, color)
