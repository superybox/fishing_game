#!/usr/bin/env python
#coding=utf-8

import pygame
import os
import codecs
from pygame.locals import *
from play import StaticAniSprite
from imcombine import imcombine
from random import randint

class Fish_Main():
	def __init__(self,size,title=u'pygame'):
		#initail pygame
		pygame.init()
		#set title name utf-8 
		self.title=title.encode('utf-8')
		pygame.display.set_caption(self.title)
		#screen size
		self.size=size
		self.screen=pygame.display.set_mode(self.size)
		#button list
		self.S1button=[]
		self.S2button=[]
		self.nothing=0
		self.sensor=0
		self.signal='tmp'
		self.data=os.getcwd()+'/data'
		#object
		self.list=Fish_List((500,100),self.data+'/long.png',self.data+'/list.png',self.data+'/list_frame.png',self.data+'/list_content',self.screen)
		self.bgimage=Fish_BgImage((0,0),self.size,self.data,'bg',self.screen)
		self.whiteimage=Fish_Background(self.size,self.screen)
		self.startbutton=Fish_Button((600,300,150,50),self.data+'/start.png',self.data+'/bstart.png',self.screen,'continue')
		self.closebutton=Fish_Button((600,400,150,50),self.data+'/close.png',self.data+'/bclose.png',self.screen,'quit')
		self.catchbutton=Fish_Button((200,400,150,50),self.data+'/start.png',self.data+'/bstart.png',self.screen,'catch')
		self.message=Fish_Message((20,20),u'開始釣魚中',(0,0,0),self.screen)
		self.catch=Fish_Catch((150,120),(150,150),self.data,'halo',self.screen,'catch')
	def fish_run(self):
		self.fish_getS1Button(self.startbutton)
		self.fish_getS1Button(self.closebutton)
		self.fish_getS2Button(self.catchbutton)
		#self.fish_getS2Button(self.catch)
		#loop
		while True:
			self.fish_handleEvent()
			if self.signal=='tmp':
				self.screen.fill((30,30,30))
				self.bgimage.fish_draw()
				self.startbutton.fish_draw()
				self.closebutton.fish_draw()
			#'''
			#elif self.signal=='start':
			#	self.whiteimage.fish_draw()
			#	self.list.fish_draw()
			#	self.catchbutton.fish_draw()
			#	self.signal='continue'
			#'''
			elif self.signal=='continue':
				self.screen.fill((255,255,255))
				self.message.fish_draw()
				self.list.fish_draw()
				self.catchbutton.fish_draw()
			elif self.signal=='quit':
				exit()
			elif self.signal=='catch':
				self.screen.fill((255,255,255))
				self.list.fish_draw()
				self.catchbutton.fish_draw()
				catch=self.catch.fish_draw()
				#print catch
				if catch=='end':
					if self.catch.catched=='catched':
						rand=randint(0,2)
						if rand==0:
							self.message.fish_setmessage(u'釣到了黃金魚')
							self.list.fish_setquantity(1,0,0,-1,0)
						elif rand==1:
							self.message.fish_setmessage(u'釣到了可食用魚')
							self.list.fish_setquantity(0,1,0,-1,0)
						elif rand==2:
							self.message.fish_setmessage(u'釣到了保育類魚')
							self.list.fish_setquantity(0,0,1,-1,0)
						else:
							self.message.fish_setmessage(u'什麼都沒釣到！')
					#self.message.fish_setmessage(u'沒有釣到魚')
					else:
						self.message.fish_setmessage(u'什麼都沒釣到！')
						self.list.fish_setquantity(0,0,0,-1,0)
					self.catch.catched='none'
					self.signal='continue'
			pygame.display.update()
	def fish_getS1Button(self,button):
		self.S1button.append(button)
	def fish_getS2Button(self,button):
		self.S2button.append(button)
	def fish_handleEvent(self):
		for event in pygame.event.get():
			if event.type==QUIT:
				exit()
			if event.type==MOUSEBUTTONDOWN:
				print self.signal
				if self.signal=='tmp':
					for button in self.S1button:
						if (button.fish_containsPoint(pygame.mouse.get_pos())):
							button.fish_mouseDown()
				elif self.signal=='continue':
					for button in self.S2button:
						if (button.fish_containsPoint(pygame.mouse.get_pos())):
							button.fish_mouseDown()
				elif self.signal=='catch':
					if (self.catch.fish_containsPoint(pygame.mouse.get_pos())):
							self.catch.fish_mouseDown()
				else:
					print 'no down'
			elif event.type==MOUSEBUTTONUP:
				if self.signal=='tmp':
					for button in self.S1button:
						if (button.fish_containsPoint(pygame.mouse.get_pos())):
							button.fish_mouseOver()
							self.signal=button.signal
				elif self.signal=='continue':
					for button in self.S2button:
						if (button.fish_containsPoint(pygame.mouse.get_pos())):
							button.fish_mouseOver()
							self.signal=button.signal
				else:
					print 'no up'
			else:
				for button in self.S1button:
					if (button.fish_containsPoint(pygame.mouse.get_pos())):
						button.fish_mouseOver()
					else:
						button.fish_mouseLeft()
				for button in self.S2button:
					if (button.fish_containsPoint(pygame.mouse.get_pos())):
						button.fish_mouseOver()
					else:
						button.fish_mouseLeft()
class Fish_Background():
	def __init__(self,size,surface):
		self.size=size
		self.surface=surface
	def fish_draw(self):
		self.surface.fill((255,255,255))
class Fish_BgImage():
	def __init__(self,pos,size,path,fname,surface):
		self.size=size
		self.pos=pos
		self.path=path
		self.fname=fname
		self.sprites=[]
		self.screen=surface
		bgcb=imcombine(self.fname,self.path)
		bgim=StaticAniSprite(self.pos,bgcb,15,self.screen)
		self.sprites.append(bgim)
	def fish_draw(self):
		sprite=self.sprites[0]
		sprite.render()
class Fish_Button():
	def __init__(self,pos,image,bimage,surface,signal):
		self.pos=pos
		self.bpos=(self.pos[0]-3,self.pos[1]-3)
		self.image=pygame.image.load(image)
		self.w=self.image.get_width
		self.h=self.image.get_height
		self.bimage=pygame.image.load(bimage)
		self.bw=self.bimage.get_width
		self.bh=self.bimage.get_height
		self.surface=surface
		self.signal=signal
		self.acsign='origin'
	def fish_containsPoint(self,pos):
		left,top,width,height=self.pos
		rect=pygame.Rect(left,top,width,height)
		return rect.collidepoint(pos)
	def fish_mouseOver(self):
		#self.surface.blit(self.bimage,self.bpos)
		self.acsign='mo'
	def fish_mouseLeft(self):
		#self.surface.blit(self.image,self.pos)
		self.acsign='ml'
	def fish_mouseDown(self):
		#self.surface.blit(self.bimage,(self.bpos[0]+20,self.bpos[1]+20))
		self.acsign='md'
	def fish_draw(self):
		if self.signal is True:
			self.surface.blit(self.image,self.pos)
		elif self.acsign=='mo':
			self.surface.blit(self.bimage,self.bpos)
		elif self.acsign=='ml':
			self.surface.blit(self.image,self.pos)
		elif self.acsign=='md':
			self.surface.blit(self.bimage,(self.bpos[0]+8,self.bpos[1]+8))
class Fish_Catch(Fish_BgImage):
	def __init__(self,pos,size,path,fname,surface,catch):
		Fish_BgImage.__init__(self,pos,size,path,fname,surface)
		self.pos=pos
		self.signal=catch
		self.size=size
		self.path=path
		self.fname=fname
		self.screen=surface
		self.bgcb=imcombine(self.fname,self.path)
		self.bgim=StaticAniSprite(self.pos,self.bgcb,90,self.screen)
		self.count=0
		self.catched='none'
	def fish_containsPoint(self,pos):
		left,top=self.pos
		width,height=self.size
		rect=pygame.Rect(left,top,width,height)
		return rect.collidepoint(pos)
	def fish_mouseOver(self):
		pass
	def fish_mouseLeft(self):
		pass
	def fish_mouseUp(self):
		pass
	def fish_mouseDown(self):
		self.catched='catched'
	def fish_random(self):
		self.pos=(randint(30,800/2.0),randint(30,500/2.0))
	def fish_draw(self):
		if self.count<1:
			self.bgim.render()
			if self.bgim._frame==0:
				self.count+=1
		elif self.count>0:
			self.fish_random()
			self.bgim=StaticAniSprite(self.pos,self.bgcb,90,self.screen)
			self.count=0
			return 'end'
#'''
class Fish_List():
	def __init__(self,pos,listimage,baseimage,frameimage,text,surface):
		self.pos=pos
		self.listimage=listimage
		self.baseimage=baseimage
		self.frameimage=frameimage
		self.text=text
		self.surface=surface
		self.flist=[]
		self.offset=25
		self.font=pygame.font.Font('wqy-microhei.ttc',14)
		self.listimage=pygame.image.load(self.listimage)
		self.baseimage=pygame.image.load(self.baseimage)
		self.frameimage=pygame.image.load(self.frameimage)
		self.f=codecs.open(self.text,encoding='utf-8')
		self.count=0
		#set quantity of fish
		self.golden=0
		self.eatable=0
		self.protected=0
		self.hungry=0
		self.money=0
	def fish_setquantity(self,golden,eatable,protected,hungry,money):
		self.golden+=golden
		self.eatable+=eatable
		self.protected+=protected
		self.hungry+=hungry
		self.money+=money
		self.count=0
	#from fish list take a fish name randomly, and give count 1
	def fish_draw(self):
		self.listimage.fill((255,255,255))
		if self.count==0:
			for line in self.f:
				line=line.rstrip('\n')
				list=self.font.render(line,True,(0,0,0))
				self.flist.append(list)
		self.count=1
		lenf=len(self.flist)
		for l in self.flist:
			self.listimage.blit(l,(25,self.offset))
			if lenf*25>self.offset:
				self.offset+=25
			else:
				self.offset=25
		golden=self.font.render(str(self.golden),True,(255,0,0))
		eatable=self.font.render(str(self.eatable),True,(255,0,0))
		protected=self.font.render(str(self.protected),True,(255,0,0))
		hungry=self.font.render(str(self.hungry),True,(255,0,0))
		money=self.font.render(str(self.money),True,(255,0,0))
		self.listimage.blit(golden,(100,75))
		self.listimage.blit(eatable,(100,100))
		self.listimage.blit(protected,(100,125))
		self.listimage.blit(hungry,(100,225))
		self.listimage.blit(money,(100,250))
		#self.offset=25
		#if self.count==0:
		self.baseimage.blit(self.listimage,(25,25))
		self.baseimage.blit(self.frameimage,(0,0))
		self.surface.blit(self.baseimage,self.pos)
		#self.count=1
	#def fish_update(self):
		
		
class Fish_Message():
	def __init__(self,pos,message,color,surface):
		self.pos=pos
		self.color=color
		self.message=message
		self.font=pygame.font.Font('wqy-microhei.ttc',14)
		self.screen=surface
	def fish_setmessage(self,message):
		self.message=message
	def fish_draw(self):
		m=self.font.render(self.message,True,self.color)
		self.screen.blit(m,self.pos)
		
if __name__=='__main__':
	main=Fish_Main((800,514),u'測試視窗')
	main.fish_run()
