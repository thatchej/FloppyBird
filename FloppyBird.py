###################################
# 		    FloppyBird            #
#   						      #
#     A simple game inspired      #
#	  by the recently viral       #
#     game 'Flappy Bird' by       #
#     Dong Nguyen.                #
#								  #
#     Author: Jaron Thatcher      #
#     Date:   Feb 9, 2014         #
#                                 #
###################################

import pygame
import sys

class Bird(pygame.sprite.Sprite):
	#main character sprite
	#goes up when the user presses space
	#otherwise falls with gravity

	#Constructor
	def __init__(self):
		 #call the parent class
		 pygame.sprite.Sprite.__init__(self)
		 self.image = pygame.image.load("images/bird.png")
		 self.rect = self.image.get_rect()
		 self.rect.x = 200
		 self.rect.y = 270

	def jump(self):
		#if the user presses space, then the bird goes up
		self.image = pygame.image.load("images/bird_up.png")
		self.rect.y -= 4

	def update(self):
		#takes care of the gravity aspect of the game
		self.image = pygame.image.load("images/bird_down.png")
		self.rect.y += 3

class Pipe(pygame.sprite.Sprite):
	#pipe sprite
	#moves right to left while the player dodges them
	#if the player collides with a pipe, GAME OVER

	#Constructor
	def __init__(self):
		#call the parent class
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/pipe_top_middle.png")
		self.rect = self.image.get_rect()
		self.rect.x = 480
		self.rect.y = 0
		#idea:
		#list of lists to contain pairs of pipes that go together
		#     - [[pipe_top_middle, pipe_bottom_middle],[pipe_top_bottom, pipe_bottom_bottom]]
	
	def update(self):
		#moves the pipes from left to right every frame
		self.rect.x -= 3


def did_collide(bird, pipe):
	#checks to see if a pipe and a bird collided, and if so ends the game
	return pygame.sprite.collide_rect(bird, pipe)

def main():

	#initializations
	pygame.init()
	screen = pygame.display.set_mode((960, 640))
	pygame.display.set_caption('Floppy Bird')

	#creates background 
	background = pygame.image.load("images/background.bmp")
	
	#displays the background
	screen.blit(background, (0, 0))
	pygame.display.flip()

	#prepares game objects
	bird = Bird()
	pipe = Pipe()
	all_sprites = pygame.sprite.RenderPlain((bird, pipe))
	clock = pygame.time.Clock()

	#game controlling loop
	while 1:

		clock.tick(60) #60 fps
		
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				#if the user presses space, the bird jumps
				if event.key == pygame.K_SPACE:
					for x in range (0, 23):
						bird.jump()
						pipe.update() #keeps pipe movement smooth - probably a better way to do this
						#draws everything so it appears smooth to the user
						screen.blit(background, (0, 0))
						all_sprites.draw(screen)
						pygame.display.flip()

		if did_collide(bird, pipe):
			sys.exit()
		if bird.rect.y in range(630, 650):
			sys.exit()

		all_sprites.update()
		#draws everything
		screen.blit(background, (0, 0))
		all_sprites.draw(screen)
		pygame.display.flip()

 
if __name__ == "__main__":
	main()




















