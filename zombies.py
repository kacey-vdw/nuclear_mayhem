import pygame

class zombie():

	def __init__(self, x, y, scale):
		width = pygame.image.load("images/zombie1.png").get_width()
		height = pygame.image.load("images/zombie1.png").get_height()
		self.coords = (x, y)

		self.image1 = pygame.transform.scale(pygame.image.load("images/zombie1.png"), (int(width * scale), int(height * scale)))
		self.image2 = pygame.transform.scale(pygame.image.load("images/zombie2.png"), (int(width * scale), int(height * scale)))
		self.image3 = pygame.transform.scale(pygame.image.load("images/zombie3.png"), (int(width * scale), int(height * scale)))
		self.image1F = pygame.transform.scale(pygame.image.load("images/zombie1F.png"), (int(width * scale), int(height * scale)))
		self.image2F = pygame.transform.scale(pygame.image.load("images/zombie2F.png"), (int(width * scale), int(height * scale)))
		self.image3F = pygame.transform.scale(pygame.image.load("images/zombie3F.png"), (int(width * scale), int(height * scale)))
		self.rip = pygame.transform.scale(pygame.image.load("images/zombie4.png"), (int(width * .9), int(height * .9)))

		self.image = self.image1

		self.rect = self.image1.get_rect()
		self.rect.topleft = (x, y)
		self.prev_update = pygame.time.get_ticks()
		self.health = 90
		self.death = False
		

	def draw(self, surface, other_drag1, other_drag2):
		cooldown = 600
		dragging = False
		radioactive_spill_rect = pygame.Rect(500, 300, 90, 50)
		time = pygame.time.get_ticks()
		flipped = False

		if self.death == False:

			#movement
			health = pygame.Rect (self.rect.x, self.rect.y-10, self.health, 10)

			if not pygame.Rect.colliderect(self.rect, radioactive_spill_rect):
				if self.rect.centerx > radioactive_spill_rect.x:
					flipped = True
					self.rect.centerx -= 1
				elif self.rect.centerx < radioactive_spill_rect.x:
					self.rect.centerx += 1
				if self.rect.centery > radioactive_spill_rect.y:
					self.rect.centery -= 1
				elif self.rect.centery < radioactive_spill_rect.y:
					self.rect.centery += 1

			elif pygame.Rect.colliderect(self.rect, radioactive_spill_rect) and self.health >-0.25:
				self.health -= 0.25
			if self.health == 0:
				self.death = True

			if flipped:
				image1 = self.image1F
				image2 = self.image2F
				image3 = self.image3F
			else:
				image1 = self.image1
				image2 = self.image2
				image3 = self.image3 

			#picking up
			other_drags = False
			if other_drag1 or other_drag2:
				other_drags = True

			if other_drags == False:

				if dragging == False:
					if pygame.mouse.get_pressed()[0] == 1 and self.rect.collidepoint(pygame.mouse.get_pos()):
						dragging = True

					if self.image == image3:
						self.image = image2

				if dragging == True:#while mouse pressed

					self.image = image3
					self.rect.center = pygame.mouse.get_pos()

			#sprite changes
			if time - self.prev_update >= cooldown:
				if self.image == image1:
					self.image = image2
				elif self.image == image2:
					self.image = image1
				self.prev_update = time

			pygame.draw.rect(surface, (255, 0, 0), health)
			surface.blit(self.image, (self.rect.x, self.rect.y))

		else:
			surface.blit(self.rip, (self.rect.x+10, self.rect.y+45))

		return self.death, dragging
			#true if dead, true if dragged

	def reset(self):
		self.health = 90
		self.death = False
		self.rect.topleft = self.coords