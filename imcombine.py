#!/usr/bin/env python
#combine and tile multi image for one

import os
import re
from PIL import Image
import pygame

#image file name must be combined for 'XXX00,XXX01...',giving XXX to this function and it will combined them to one tile image object
def imcombine(fheadname,path):
	#count is used to looking for how many file
	count=0
	filelist=[]
	for dirpath,dirnames,filenames in os.walk(path):
		for ifile in filenames:
			pattern=fheadname+'[0-9]*'
			match=re.match(pattern,ifile)
			if match!=None:
				print(ifile,':match')
				count+=1
				filelist.append(ifile)
			else:
				print(ifile,':nomatch')
	filelist.sort()
	print(filelist)
	im=Image.open(path+'/'+filelist[0])
	w=im.size[0]
	h=im.size[1]
	background=Image.new('RGBA',(w*count,h))
	i=0
	for f in filelist:
		image=Image.open(path+'/'+f)
		background.paste(image,(w*i,0))
		i+=1
	bgw,bgh=background.size
	bgstring=background.tostring()
	bg=pygame.image.fromstring(bgstring,(bgw,bgh),'RGBA')
	anim=[]
	bgw,bgh=bg.get_size()
	for i in xrange(int(bgw/w)):
		anim.append(bg.subsurface((i*w,0,w,h)))
	return anim
			
	
	
	
if __name__=='__main__':
	path=os.getcwd()+'/data'
	print(path)
	imcombine('chief-',path)

