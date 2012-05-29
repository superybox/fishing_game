#!/usr/bin/env python
import os
import pygame
from gameobjects.vector2 import Vector2
from pygame.locals import *
from random import randint
#local folder
from explosion import AnimatedSprite
from imcombine import imcombine


class StaticAniSprite(AnimatedSprite):
	def __init__(self,images,fps=10):
		AnimatedSprite.__init__(self,images,fps)
		self.location=(0,0)
		
	def update(self,t):
		if t-self._last_update>self._delay:
			self._frame+=1
			if self._frame>=len(self._images):
				self._frame=0
			self.image=self._images[self._frame]
			self._last_update=t
	def render(self,screen):
		self.update(pygame.time.get_ticks())
		screen.blit(self.image,self.location)

def main():

	RESOLUTION=(1400,900)
	pygame.init
	screen=pygame.display.set_mode(RESOLUTION)
	background=pygame.Surface(RESOLUTION)
	path=os.getcwd()+'/data'
	mybg_images=imcombine('bg',path)
	clock=pygame.time.Clock()

	sprites=[]
	mybg=StaticAniSprite(mybg_images,15)
	mybg.locaton=(150,150)
	sprites.append(mybg)

	while True:
		for event in pygame.event.get():
			if event.type==QUIT:
				return
		
		screen.blit(background,(0,0))
		time_passed=clock.tick(30)

		#sprite=sprites[0]
		#print('ANOTHER',sprite)
		#sprite.render(screen)
		for sprite in sprites:
			print('THIS IS',sprite)
			sprite.render(screen)
		pygame.display.update()

if __name__=='__main__':
	main()
