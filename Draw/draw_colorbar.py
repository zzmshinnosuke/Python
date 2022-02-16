#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on 2022-02-16 16:11:17
# @Author: zzm

import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
  
# # Dataset 
# # List of total number of items purchased  
# # from each products 
# purchaseCount = [100, 200, 150, 23, 30, 50, 
#                  156, 32, 67, 89] 
  
# # List of total likes of 10 products 
# likes = [50, 70, 100, 10, 10, 34, 56, 18, 35, 45] 
  
# # List of Like/Dislike ratio of 10 products 
# ratio = [1, 0.53, 2, 0.76, 0.5, 2.125, 0.56,  
#          1.28, 1.09, 10] 
  
# # scatterplot 
# plt.scatter(x=purchaseCount, y=likes, c=ratio, cmap="summer") 
  
# plt.colorbar(label="Like/Dislike Ratio", orientation="horizontal") 
# plt.show()


  
x = np.linspace(0, 5, 100) 
N = 100
  
# colormap 
cmap = plt.get_cmap('jet', 100) 
  
fig, ax1 = plt.subplots(1, 1, figsize=(8, 6)) 
  
for i, n in enumerate(np.linspace(0, 2, N)):
    y = x*i+n 
    ax1.plot(x, y, c=cmap(i)) 
  
plt.xlabel('x-axis') 
plt.ylabel('y-axis') 
  
# Normalizer 
norm = mpl.colors.Normalize(vmin=0, vmax=100) 
  
# creating ScalarMappable 
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm) 
sm.set_array([]) 
  
plt.colorbar(sm, ticks=np.linspace(0, 100, 11)) 
  
plt.show()