import pygame
from numpy import random
import modules.Loader

# General setup

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
running = True

# Utils functions
quit_game = lambda pygame, event: False if event.type == pygame.QUIT else True 
get_random_pos = lambda: ( random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT) )

def setBackground ( screen ):
	screen.fill('darkgray')
	star = modules.Loader.image_loader('star.png')
	for i in range(20):
		screen.blit(star, get_random_pos())



pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter I - Revenge Of The Bit')

while running:
	# Event loop
	for event in pygame.event.get():
		running = quit_game(pygame, event)

	# Draw game
	setBackground(screen)
	
	pygame.display.update()


pygame.quit()
