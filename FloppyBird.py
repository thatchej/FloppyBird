import pygame
import math
import sys

#initializations
pygame.init()

size                    = width, height = 960, 640
screen             		= pygame.display.set_mode(size)

start_button 			= pygame.image.load("images/start_button.png")
background_initial 		= pygame.image.load("images/background_initial.png")
background_initial_rect = background_initial.get_rect()
background         		= pygame.image.load("images/background.bmp")
background_rect    		= background.get_rect()

#WOW SUCH BIRD VARIABLES
bird               		= pygame.image.load("images/bird.png")
bird_rect          		= bird.get_rect()
bird.convert_alpha()
bird_up               	= pygame.image.load("images/bird_up.png")
bird_up_rect          	= bird.get_rect()
bird.convert_alpha()
bird_down               = pygame.image.load("images/bird_down.png")
bird_down_rect          = bird.get_rect()
bird.convert_alpha()
bird_x             		= 200 #the character sprite will always have the same x value
up 						= "up"
down					= "down"

pipe_top_middle			= pygame.image.load("images/pipe_top_middle.png")
pipe_top_middle_rect	= pipe_top_middle.get_rect()


gravity            		= -3

def draw_bird(orientation, x, y):
	if(orientation == "up"):
		screen.blit(bird_up, (x, y))
	elif(orientation == "down"):
		screen.blit(bird_down, (x, y))
	else:
		screen.blit(bird, (x, y))

def main():

	bird_y = 270
	pipe_x = 480

	#game controlling loop
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE:
					for x in range(0, 15):
						bird_y -= 5
						screen.blit(background, background_rect)
						screen.blit(pipe_top_middle, (pipe_x, 0))	
						draw_bird(up, bird_x, bird_y)
						pygame.display.update()
					
		#adjusts for gravity and draws the bird, pipes, and background
		#TODO: Make this a function and call it here
		for x in range(0, 15):
			bird_y -= gravity
			screen.blit(background, background_rect)
			screen.blit(pipe_top_middle, (pipe_x, 0))
			draw_bird(down, bird_x, bird_y)
			pygame.display.update()
			pipe_x -= 3			
		

if __name__ == "__main__":
	main()