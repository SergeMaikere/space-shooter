import pygame
from os.path import join
import modules.Helper

load_image = lambda name: pygame.image.load( join('assets', 'images', name) )
convert_image = lambda surface: surface.convert_alpha()
image_loader = modules.Helper.pipe([load_image, convert_image])
