# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 12:05:19 2016

@author: mravi
"""
import numpy as np
import scipy as sc

from numpy import *
from scipy import *


#M = numpy.zeros(shape=(4,2))
#M[0] = [1,2]
#M[1] = [2,1]
#M[2] = [3,4]
#M[3] = [4,3]

M= np.matrix('1 2; 2 1;3 4;4 3')

[u,s,vT] = sc.linalg.svd(M,full_matrices=False)


MMT =  M.transpose()*M 

[pca_eval,pca_evec] = sc.linalg.eigh(MMT)
pca_eval_reordered=-np.sort(-pca_eval)
pca_eval_desc_index=np.argsort(-pca_eval)
pca_evec_reordered=pca_evec[:,pca_eval_desc_index]

#print pca_eval_reordered
#print pca_evec_reordered