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
bird_up               	= pygame.image.load("images/bird_up.png")
bird_down               = pygame.image.load("images/bird_down.png")
bird_x             		= 200 #the character sprite will always have the same x value

pipe_top_middle			= pygame.image.load("images/pipe_top_middle.png")
pipe_bottom_middle		= pygame.image.load("images/pipe_bottom_middle.png") #MAKING THIS RIGHT NOW

gravity            		= -3

#TODO: ADD CLASSES FOR BIRDS AND PIPES INHERITING SPRITES SO WE CAN EASILY DETECT COLLISION AND MAYBE 
#	   MAKE THIS CODE NOT SO AWFUL



def draw_bird(orientation, x, y):
	if(orientation == 'up'):
		screen.blit(bird_up, (x, y))
	elif(orientation == 'down'):
		screen.blit(bird_down, (x, y))
	else:
		screen.blit(bird, (x, y))

def draw_pipe_pair(pipe_x, pipe_type):
	if pipe_type == 'middle':
		screen.blit(pipe_top_middle, (pipe_x, 0))
		screen.blit(pipe_bottom_middle, (pipe_x, 360))

def check_for_collision(bird, pipe):
	if bird.get_rect() == pipe.get_rect:
		sys.exit()

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
						draw_pipe_pair(pipe_x, 'middle')	
						draw_bird('up', bird_x, bird_y)
						pipe_x -= 2
						print bird_up.get_rect()
						print pipe_top_middle.get_rect()
						#check_for_collision(bird_up, pipe_top_middle)
						
						pygame.display.update()
					
		#adjusts for gravity and draws the bird, pipes, and background
		#TODO: Make this a function and call it here
		for x in range(0, 15):
			bird_y -= gravity
			screen.blit(background, background_rect)
			draw_pipe_pair(pipe_x, 'middle')
			draw_bird('down', bird_x, bird_y)
			pipe_x -= 2
			pipe_top_middle_rect = pipe_top_middle.get_rect() #updates the current rectangle for collision detection purposes
			pygame.display.update()
						
		

if __name__ == "__main__":
	main()