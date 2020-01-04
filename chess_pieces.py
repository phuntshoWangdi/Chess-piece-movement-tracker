import pygame

class Chess_Pieces(pygame.sprite.Sprite):
	
	def __init__(self,img):
		super().__init__()
		self.image=pygame.image.load(img).convert_alpha()
		self.rect=self.image.get_rect()

	def mr(self,pixels):
		self.rect.x+=pixels
		print("x:",self.rect.x)
	
	def ml(self,pixels):
		self.rect.x-=pixels
		print("x:",self.rect.x)

	def mu(self,pixels):
		self.rect.y-=pixels
		print("y:",self.rect.y)

	def md(self,pixels):
		self.rect.y+=pixels
		print("y:",self.rect.y)
