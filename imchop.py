#/usr/bin/env python3
#file:chop image

import sys
from PIL import Image

#vsp:verical splite for width;sp:horizontal splite for height
def imchrop(fname,vsp,sp):
	im=Image.open(fname)
	im=im.convert('RGBA')
	print(im.mode)
	w,h=im.size
	cw=w/vsp
	ch=h/sp
	for top in range(0,sp):
		for left in range(0,vsp):
			le=cw*left
			to=ch*top
			width=cw
			height=ch
			box=(le,to,le+width,to+height)
			print(box)
			area=im.crop(box)
			fname=fname.split('.')[0]
			f=fname+'-'+str(left)+str(top)+'.png'
			area.save(f,'png')


if __name__=="__main__":
	imchrop('chief.png',3,4)
