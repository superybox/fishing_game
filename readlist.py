#!/usr/bin/env python

import csv

list=csv.reader(open('data/fish_list.csv','r'),delimiter='	')
f=open('fishname','w+')
fishlist=[]
test=0
for l in list:
	for t in fishlist:
		if l[16]==t:
			#print l[16]
			test+=1
	if test==0:
		fishlist.append(l[16])
	else:
		test=0
for name in fishlist:
	f.write(name+'\n')
