#!/usr/bin/env python
#combine and tile multi image for one

import os
import re

def imcombine(fheadname,path):
	#count is used to look for how many file
	count=0
	for dirpath,dirnames,filenames in os.walk(path):
		for ifile in filenames:
			pattern=fheadname+'[0-9]*'
			match=re.match(pattern,ifile)
			if match!=None:
				print(ifile,':match')
			else:
				print(ifile,':nomatch')
if __name__=='__main__':
	path=os.getcwd()+'/data'
	print(path)
	imcombine('chief-',path)

