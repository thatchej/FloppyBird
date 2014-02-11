import pygame
import sys

#initializations
pygame.init()
screen = pygame.display.set_mode((960, 640))
pygame.display.set_caption('Floppy Bird')

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
		 self.jumping = 0

	def jump(self):
		#if the user presses space, then the bird goes up	
		for x in range(0, 15):
			self.rect.y -= 5
			self.jumping = 1

	def fall(self):
		for x in range(0, 15):
			self.rect.y += 5

def main():

	background = pygame.image.load("images/background.bmp")
	screen.blit(background, (0, 0))
	pygame.display.flip()

	bird = Bird()
	allsprites = pygame.sprite.RenderPlain((bird))
	clock = pygame.time.Clock()
	pygame.display.flip()

	#game controlling loop
	while 1:

		clock.tick(60) #60 fps

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.K_SPACE:
				bird.jump()
    		
    		
   

if __name__ == "__main__":
	main()