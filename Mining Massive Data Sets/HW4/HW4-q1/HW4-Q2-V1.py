# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 19:27:10 2016

@author: mravi
"""
import os
import math
import numpy as np
import time

def cost(w,b,x,y):
    nrow=6414
    Smax=0
    Sw=0
    for p in range(len(w)):
        Sw=Sw+math.pow(w[p],2)
    for p in range(nrow):
        Swx=0
        for q in range(len(w)):
            Swx=Swx+w[q]*x[p][q]
        temp_val=1-(y[p]*(Swx+b))
        if temp_val>0:
            Smax=Smax+temp_val
    final_f=0.5*Sw+100*Smax
    return final_f
    

def batch_gradient(x,y):
    eta_val=0.0000003
    eps_val=0.25
    nrow=6414
    ncol=122
    k,b=0,0
    w0=[0.0 for ab in range(122)]
    w=w0
    while(1):
        fk_minus1=cost(w,b,x,y)
        with open('batch.txt','a') as op:
            op.write(str(k)+' '+str(fk_minus1)+'\n')
        indicator=[0 for p in range(nrow)]
        for p in range(nrow):
            temp_val=1-y[p]*(np.dot(x[p],w)+b)
            if temp_val>0:
                indicator[p]=1
        for j in range(len(w)):
            wnew,Sm=w,0
            for p in range(nrow):
                if indicator[p]!=0:
                    Sm=Sm-y[p]*x[p][j]
            del_fw=w[j]+100*Sm
            wnew[j]=w[j]-eta_val*del_fw
        w,del_fb=wnew,0
        for p in range(nrow):
            if indicator[p]!=0:
                del_fb=del_fb-y[p]
        b=b-eta_val*100*del_fb
        k=k+1
        fk=cost(w,b,x,y)
        if math.fabs(fk-fk_minus1)*100/fk_minus1<eps_val:
            with open('batch.txt','a') as op:
                op.write(str(k)+' '+str(fk)+'\n')
            break
    return b,w
            
def stochastic_gradient(x,y):
    cost_val=0
    eta_val=0.0001
    eps_val=0.001
    nrow=6414
    ncol=122
    k,b,i=0,0,1
    w0=[0.0 for ab in range(122)]
    w=w0
    for a in range(nrow):
        x[a].append(y[a])
    np.random.shuffle(x)
    for kx in range(nrow):
        y[kx]=x[kx][-1]
        del x[kx][-1]
        
    while(1):
        fk_minus1=cost(w,b,x,y)
        with open('stoch.txt','a') as op:
            op.write(str(k)+' '+str(fk_minus1)+'\n')
        indicator=[0 for p in range(nrow)]
        for p in range(nrow):
            temp_val=1-y[p]*(np.dot(x[p],w)+b)
            if temp_val>0:
                indicator[p]=1
        for j in range(len(w)):
            wnew,jus_m=w,0
            if indicator[i-1]!=0:
                jus_m=jus_m-y[i-1]*x[i-1][j]
        del_fw=w[j]+100*jus_m
        wnew[j]=w[j]-eta_val*del_fw
        w,jus_b=wnew,0
        if indicator[i-1]!=0:
            jus_b=jus_b-y[i-1]
        b=b-eta_val*100*jus_b
        i=i%nrow+1
        k=k+1
        fk=cost(w,b,x,y)
        cost_val=0.5 *cost_val+0.5*math.fabs(fk-fk_minus1)*100/fk_minus1
        if cost_val<eps_val:
            with open('stoch.txt','a') as op:
                op.write(str(k)+' '+str(fk)+'\n')
            break
    return b,w

def minibatch_gradient(x,y):
    cost_val=0
    eta_val=0.00001
    eps_val=0.01
    nrow=6414
    ncol=122
    k,b=0,0
    batch_size=20
    jus_l=0
    w0=[0.0 for ab in range(122)]
    w=w0
    for a in range(nrow):
        x[a].append(y[a])
    np.random.shuffle(x)
    for kx in range(nrow):
        y[kx]=x[kx][-1]
        del x[kx][-1]
    while(1):
        fk_minus1=cost(w,b,x,y)
        with open('minibatch.txt','a') as op:
            op.write(str(k)+' '+str(fk_minus1)+'\n')
        indicator=[0 for p in range(nrow)]
        for p in range(nrow):
            temp_val=1-y[p]*(np.dot(x[p],w)+b)
            if temp_val>0:
                indicator[p]=1
        for j in range(len(w)):
            wnew,Sm=w,0
            for p in range(batch_size*jus_l,min(nrow,(jus_l+1)*batch_size)):
                if indicator[p]!=0:
                    Sm=Sm-y[p]*x[p][j]
            del_fw=w[j]+100*Sm
            wnew[j]=w[j]-eta_val*del_fw
        w,del_fb=wnew,0
        for p in range(batch_size*jus_l,min(nrow,(jus_l+1)*batch_size)):
            if indicator[p]!=0:
                del_fb=del_fb-y[p]
        b=b-eta_val*100*del_fb
        jus_l=(jus_l+1)%((nrow+batch_size-1)/batch_size)
        k=k+1
        fk=cost(w,b,x,y)
        cost_val=0.5 *cost_val+0.5*math.fabs(fk-fk_minus1)*100/fk_minus1
        if cost_val<eps_val:
            with open('minibatch.txt','a') as op:
                op.write(str(k)+' '+str(fk)+'\n')
            break
    return b,w
        
    
    
    
    
def main():
    os.chdir(os.path.dirname(os.path.realpath("/Users/mravi/Desktop/C/MMDS - Sta/HW/HW4/Q1/HW4-q1/HW4-Q2-V1.py")))
    x,y=[],[]
    C=100
    t=open("target.txt", "r")
    for l in t:
        y.append(int(l.strip()))
    f=open("features.txt", "r")
    for l in f:
        fea=l.strip().split(",")
        temp=[]
        for item in fea:
            temp.append(int(item))
        x.append(temp)
    st=time.clock()    
    batch_gradient(x,y)
    en=time.clock()
    print en-st
    st=time.clock()
    stochastic_gradient(x,y)
    en=time.clock()
    print en-st
    st=time.clock()
    minibatch_gradient(x,y)
    en=time.clock()
    print en-st
    #batch = 21.686964s
    #sgd = 155.182356s
    #minibatch =226.572353s



if __name__ == "__main__":
    main()
    

#MATLAB Code

#bat=importdata('batch.txt');
#stoch=importdata('stoch.txt');
#mini=importdata('minibatch.txt');
#plot(bat(:,1),bat(:,2),'r',stoch(:,1),stoch(:,2),'g',mini(:,1),mini(:,2),'b')
#legend('batch','stochastic','mini batch')