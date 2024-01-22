#!/usr/bin/env python
import math

file1="LA_LB_dist2"
file2="LA_LB_coords2.txt"
coord=open(file2,'r')
dist=open(file1,'w')

for line in coord:
            ls=line.split()
            mol=ls[0]
            x1=float(ls[1])
            y1=float(ls[2])
            z1=float(ls[3])
            x2=float(ls[4])
            y2=float(ls[5])
            z2=float(ls[6])
            pt1=(x1-x2)**2+(y1-y2)**2+(z1-z2)**2
            d=math.sqrt(pt1)
            #print >> dist,  mol,d
            print(mol,d,file=dist)


