# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:41:46 2019

@author: mbgnwlr2
"""
import os
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import lfilter




scan_id = 83578

#Fibre stiffness
E = 410000 #Fibre stiffnes, MPa

#Fibre radius
r = 70E-3 #mm

#Unstrained, RTP fibre d-spacing
d_o = 1.5434769262199129498473 #Angstrom





os.chdir("D:/PhD Synchrotron Stuff/Winter19_beamtime")

data = np.genfromtxt(str(scan_id) + "_FittingResults.txt",
                     dtype = None,
                     delimiter = "\t"
                     )

x = data[1:data.shape[0] , 0]
y = data[0 , 1:data.shape[1]]

grid = data[1:data.shape[0], 1:data.shape[1]]

##parameters for signal smoothing
N = 15
B = [1.0/N]*N
A = 1


for i in np.arange(len(x)):
    
    d = (grid[i,:])
    
    e = (d-d_o)/d_o
    
    grad = np.gradient(e, 0.025)
    
    grad_smooth = lfilter(B, A, grad)
    
    tau = ((E*r)/2)*grad_smooth
    
    
    plt.figure(i, figsize = (10, 5))
    plt.scatter(y, d, label = x[i])                  ##Change the second variable to change what is plotted: d = d-spacing, e = strain, tau = ISS
    plt.legend()
#    plt.savefig(str(scan_id)+str(y[i])+".png")      ##<-- remove this comment if you wish to save each line plot

grid = np.clip(grid, 1.533, 1.547)

plt.figure((i+1), figsize = (6, 6))
plt.imshow(grid, interpolation='nearest', origin='lower', cmap='viridis')
