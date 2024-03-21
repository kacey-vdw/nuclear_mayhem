import pygame

class button():

	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) #changes size of image
		self.rect = self.image.get_rect() #creates rectangle around image
		self.rect.topleft = (x, y)

	def draw(self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y)) #draws image on screen
		action = False #initialises action
		pos = pygame.mouse.get_pos() #get mouse position

		#check mouse is over button and clicked (conditions)
		if self.rect.collidepoint(pos):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
					action = True

		return action