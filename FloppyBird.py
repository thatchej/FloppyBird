import pygame
import math
import sys

#initializations
pygame.init()

size                    = width, height = 960, 640
screen             		= pygame.display.set_mode(size)

start_button 			= pygame.image.load("start_button.png")
background_initial 		= pygame.image.load("background_initial.png")
background_initial_rect = background_initial.get_rect()
background         		= pygame.image.load("background.bmp")
background_rect    		= background.get_rect()

#WOW SUCH BIRD VARIABLES
bird               		= pygame.image.load("bird.png")
bird_rect          		= bird.get_rect()
bird.convert_alpha()
bird_x             		= 200 #the character sprite will always have the same x value


gravity            		= -3

def draw_bird(screen, x, y):
	screen.blit(bird, (x, y))

def main():

	bird_y = 270

	#gives the user a cool little intro screen when they first start
	
	#screen.blit(background_initial, background_initial_rect)
	#screen.blit(start_button, (480, 500))
	#pygame.display.update()

	#for event in pygame.event.get():
	#		if event.type == pygame.QUIT:
	#			sys.exit()
	#		if event.type == pygame.KEYDOWN:
	#			if event.key == pygame.MOUSEBUTTONDOWN:
	#				if get_pos() == (480, 500):
	#game controlling loop
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE:
					for x in range(0, 12):
						bird_y -= 5
						screen.blit(background, background_rect)
						draw_bird(screen, bird_x, bird_y)
						pygame.display.update()
					
		#draws the background and bird on each reset
		screen.blit(background, background_rect)
		
		#adjusts for gravity and draws the bird
		for x in range(0, 12):
			bird_y -= gravity
			screen.blit(background, background_rect)
			draw_bird(screen, bird_x, bird_y)
			pygame.display.update()

		pygame.display.flip()

if __name__ == "__main__":
	main()