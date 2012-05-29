#!/usr/bin/env python
#coding=utf-8

import pygame
import os
from pygame.locals import *
from play import StaticAniSprite
from imcombine import imcombine

class main():
	def __init__(self,size=(800,600),title=u'pygame'):
		pygame.init()	
		self.size=size
		self.title=title.encode('utf-8')
	def run(self,drawlist=None,objlist=None):
		pygame.display.set_caption(self.title)
		#sceen=pygame.display.set_mode(self.size)
		while True:
			for event in pygame.event.get():
				if event.type==QUIT:
					exit()
			if drawlist!=None:
				self.draw(drawlist)
			if objlist!=None:
				self.get_handler()
			pygame.display.update()
	def draw(self,objs):
		for obj in objs:
			obj=obj
			obj.draw()
		
	def get_hanler(self,sign=None):
		if sign==None:
			return self.handler
		else:
			self.shandler=1
		if sign=='open_game':
			open_game
		if sign=='quit_game':
			quit_game
class background():
	def __init__(self,size):
		self.size=size
	def draw(self):
		background=pygame.Surface(self.size)
		screen=pygame.display.set_mode(self.size)
		screen.fill((255,255,255))
		return screen
class bg_image():
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
	def draw(self):
		print('bg_iamg.draw')
		self.screen.blit(self.surface,(0,0))
		sprite=self.sprites[0]
		sprite.render(self.screen)
if __name__=='__main__':
	main=main((800,600),u'測試視窗')
	print main.size
	size=main.size
	#the parameter of main.draw is an object tuple
	drawlist=[]
	drawlist.append(background(main.size))
	drawlist.append(bg_image(size,os.getcwd()+'/data','bg'))
	main.run(drawlist)
