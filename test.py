#!/usr/bin/env python
#coding=utf-8

import pygame
import os
from pygame.locals import *
from play import StaticAniSprite
from imcombine import imcombine

class Fish_Main():
	def __init__(self,size=(800,600),title=u'pygame'):
		#initail pygame
		pygame.init()
		#set title name utf-8 
		self.title=title.encode('utf-8')
		pygame.display.set_caption(self.title)
		#screen size
		self.size=size
		self.screen=pygame.display.set_mode(self.size)
		#default background is white
		self.screen.fill((255,255,255))
		#button list
		self.button=[]
		self.nothing=0
		self.signal='tmp'
	def fish_run(self):
		bgimage=Fish_BgImage(self.size,os.getcwd()+'/data','bg')
		startbutton=Fish_StartButton(600,350,150,50)
		closebutton=Fish_CloseButton(600,450,150,50)
		self.fish_getButton(startbutton)
		self.fish_getButton(closebutton)
		print(self.button)
		#loop
		while True:
			#get button
			#handle event
			self.fish_handleEvent()
			if self.nothing==0:
				#exe Fish_BgImage widget
				bgimage.fish_draw()
				startbutton.fish_draw(self.screen)
				closebutton.fish_draw(self.screen)
			pygame.display.update()
	def fish_getButton(self,button):
		self.button.append(button)
	def fish_handleEvent(self):
		for event in pygame.event.get():
			if event.type==QUIT:
				exit()
			if event.type==MOUSEBUTTONDOWN:
				for button in self.button:
					if (button.fish_containsPoint(pygame.mouse.get_pos())):
						button.fish_mouseDown()
						self.signal=button.fish_signal()
			for button in self.button:
				if (button.fish_containsPoint(pygame.mouse.get_pos())):
					button.fish_mouseOver()
				if (button.fish_containsPoint(pygame.mouse.get_pos()))==0:
					button.fish_mouseLeft()
				if self.signal=='start':
					bg=Fish_Background(self.size)
					bg.fish_draw(self.screen)
					self.nothing=1
				if self.signal=='quit':
					exit()
				
class Fish_Background():
	def __init__(self,size):
		self.size=size
	def fish_draw(self,surface):
		surface.fill((255,255,255))
class Fish_BgImage():
	def __init__(self,size,path,fname):
		self.size=size
		self.path=path
		self.fname=fname
		self.sprites=[]
		self.screen=pygame.display.set_mode(self.size)
		bgcb=imcombine(self.fname,self.path)
		bgim=StaticAniSprite(bgcb,15)
		bgim.location=(0,0)
		self.sprites.append(bgim)
		self.surface=pygame.Surface(self.size)
	def fish_draw(self):
		self.screen.blit(self.surface,(0,0))
		sprite=self.sprites[0]
		sprite.render(self.screen)
class Fish_Button():
	def __init__(self,x,y,w,h):
		self.rect=Rect(x,y,w,h)
		self.w=self.rect.w
		self.h=self.rect.h
	def fish_containsPoint(self,pos):
		return self.rect.collidepoint(pos)
	def fish_draw(self,surface):
		pygame.draw.rect(surface,(100,100,100),self.rect)
	def fish_mouseOver(self):
		if self.rect.w==self.w and self.rect.h==self.h:
			self.rect=self.rect.inflate(3,3)
	def fish_mouseLeft(self):
		if self.rect.w>self.w and self.rect.h>self.h:
			self.rect=self.rect.inflate(-3,-3)
	def fish_mouseDown(self):
		self.rect=self.rect.move(5,5)
	def fish_signal(self):
		print('use to tell main class what to do')
class Fish_StartButton(Fish_Button):
	def __init__(self,x,y,w,h):
		Fish_Button.__init__(self,x,y,w,h)
	def fish_signal(self):
		return 'start'
class Fish_CloseButton(Fish_Button):
	def __init__(self,x,y,w,h):
		Fish_Button.__init__(self,x,y,w,h)
	def fish_signal(self):
		return 'quit' 
		
if __name__=='__main__':
	main=Fish_Main((800,600),u'測試視窗')
	main.fish_run()
