#!/usr/bin/env python
import os
import pygame
from gameobjects.vector2 import Vector2
from pygame.locals import *
from random import randint
#local folder
from imcombine import imcombine


class StaticAniSprite(pygame.sprite.Sprite):
	def __init__(self,pos,images,fps,surface):
		self.fps=10
		self.location=pos
		self.screen=surface
		self._images=images
		
		self._start=pygame.time.get_ticks()
		self._delay=1000/fps
		self._last_update=0
		self._frame=0
		self.image=self._images[self._frame]
		
	def update(self,t):
		if t-self._last_update>self._delay:
			self._frame+=1
			if self._frame>=len(self._images):
				self._frame=0
			self.image=self._images[self._frame]
			self._last_update=t
	def render(self):
		self.update(pygame.time.get_ticks())
		self.screen.blit(self.image,self.location)

def main():

	RESOLUTION=(200,200)
	pygame.init
	screen=pygame.display.set_mode(RESOLUTION)
	background=pygame.Surface(RESOLUTION)
	background.fill((255,255,255))
	path=os.getcwd()+'/data'
	mybg_images=imcombine('halo',path)
	clock=pygame.time.Clock()

	sprites=[]
	mybg=StaticAniSprite(mybg_images,15)
	sprites.append(mybg)

	while True:
		for event in pygame.event.get():
			if event.type==QUIT:
				return
		
		screen.blit(background,(0,0))
		mybg.render(screen)
		time_passed=clock.tick(30)

		#sprite=sprites[0]
		#print('ANOTHER',sprite)
		#sprite.render(screen)
		pygame.display.update()

if __name__=='__main__':
	main()
