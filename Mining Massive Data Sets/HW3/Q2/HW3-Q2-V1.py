# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:21:00 2016

@author: mravi
"""

from collections import defaultdict
import numpy as np


    
#count
n_cou=100
beta=0.8

mat=[]
for x in range(n_cou):
    mat.append([0 for y in range(n_cou)])
    
#creating an edge list map    
graph_file=open("/Users/mravi/Desktop/C/MMDS - Sta/HW/HW3/Q2/graph.txt",'r')
n_ma=defaultdict(list)
for l in graph_file:
    e=l.strip().split("\t")
    n_ma[int(e[0])].append(int(e[1]))
    
graph_file_re=open("/Users/mravi/Desktop/C/MMDS - Sta/HW/HW3/Q2/graph.txt",'r')
for l in graph_file_re:   
    m=l.strip().split("\t")
    mat[int(m[1])-1][int(m[0])-1]=1.0/len(n_ma[int(m[0])])

mat_final=np.matrix(mat)

#initializing
r=np.matrix([1.0/n_cou for x in range(n_cou)]).transpose()

for i in range(40):
    one_v=np.matrix([1 for i in range(n_cou)]).transpose()
    r=((1-beta)/n_cou)*one_v + beta*mat_final*r

A = np.squeeze(np.asarray(r))
#print np.argsort(A)
print np.argsort(A)[-5:]+1
print np.argsort(A)[:5]+1
#[27  1 14 40 53]
#[85 59 81 23 37]
print np.sort(A)[-5:]
print np.sort(A)[:5]
#[ 0.02226321  0.02233271  0.02474559  0.02505707  0.02608162]
#[ 0.00309996  0.00328665  0.00333862  0.00337468  0.00344609]

L=[]
for x in range(n_cou):
    L.append([0 for y in range(n_cou)])

graph_file_re_re=open("/Users/mravi/Desktop/C/MMDS - Sta/HW/HW3/Q2/graph.txt",'r')
for l in graph_file_re_re:   
    m=l.strip().split("\t")
    L[int(m[0])-1][int(m[1])-1]=1.0
L_final=np.matrix(L)

hu=np.matrix([1 for i in range(n_cou)]).transpose()

for i in range(40):
    au=L_final.transpose()*hu
    au=au/np.amax(au)
    hu=L_final*au
    hu=hu/np.amax(hu)

A_hu = np.squeeze(np.asarray(hu))    
#print np.argsort(A)
print np.argsort(A_hu)[-5:]+1
print np.argsort(A_hu)[:5]+1
#[58 11 22 39 59]
#[ 9 35 15 95 53]
print np.sort(A_hu)[-5:]
print np.sort(A_hu)[:5]
#[ 0.9574262   0.95742826  0.97411071  0.98107991  1.        ]
#[ 0.20936883  0.21233808  0.22106736  0.22976127  0.23548213]


A_au = np.squeeze(np.asarray(au))    
#print np.argsort(A)
print np.argsort(A_au)[-5:]+1
print np.argsort(A_au)[:5]+1
#[ 1 53 27 40 66]
#[54 33 24 67 50]
print np.sort(A_au)[-5:]
print np.sort(A_au)[:5]
#[ 0.82154886  0.89517958  0.95670223  0.98253375  1.        ]
#[ 0.04859676  0.05560434  0.06366925  0.0676041   0.06971236]