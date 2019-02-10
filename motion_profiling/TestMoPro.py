# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:52:57 2018

@author: Noah
"""

import MoPro_fixed
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.cm as cmx

points = []
tangents = []
resolution = .1
points.append([0.,0.]); tangents.append([0,2])
points.append([122.,228.]); tangents.append([2,0])
#points.append([300.,200.]); tangents.append([2,0])
#points.append([350.,100.]); tangents.append([0,-1])
points = np.asarray(points)
tangents = np.asarray(tangents)
scale = 1.25
num_points = 1200
trackwidth = 30.0
max_velocity = 205
max_accel = 100.0
max_decel = -100.0
starting_velocity = 0
end_velocity = 0

plt.figure(0)
CV,RV,LV,TE,CenP,RP,LP,RR,RL = MoPro_fixed.trajectory(points,tangents,scale,resolution,trackwidth,max_velocity,max_accel,max_decel,num_points,starting_velocity,end_velocity)

plt.figure(1)

plt.scatter(points[:,0],points[:,1],s=400,c='k',marker='o',label='input')
plt.scatter(CenP[:,0],CenP[:,1],c=None,marker= 'o',label='centerpath')
plt.scatter(RP[:,0],RP[:,1],c=None,marker='o',label='rightpath')
plt.scatter(LP[:,0],LP[:,1],c=None,marker='o',label='leftpath')
#plt.xlim(0,300)
plt.axis('equal')
plt.title('Path')
plt.legend()





Righty=RV
Lefty=LV

plt.figure(2)
plt.scatter(TE,CV,c=None,marker='o',label='centervelocity')
plt.scatter(TE,RV,c=None,marker='o',label='rightvelocity')
plt.scatter(TE,LV,c=None,marker='o',label='leftvelocity')
plt.title('Velocity')
plt.ylim(0,max_velocity*1.2)
plt.legend()
plt.show()
plt.figure(3)
plt.scatter(TE,RR,c=None,marker='o',label='radius_right')
plt.scatter(TE, RL,c=None,marker='o',label='radius_left')
plt.title('radii')
plt.legend()
plt.show()
'''
fig = plt.figure(3)
ax = Axes3D(fig)
'''
x = [0 for i in range(num_points-1)]
y = [0 for i in range(num_points-1)]

for i in range(num_points-1):
    x[i] = CenP[i][0]
    y[i] = CenP[i][1]
'''
ax.plot(x,y,zs=Time,zdir='z',color = Center_Velocity, label='path')
ax.legend()
'''
def scatter3d(x,y,z, cs, colorsMap='jet'):
    cm = plt.get_cmap(colorsMap)
    cNorm = matplotlib.colors.Normalize(vmin=min(cs), vmax=max(cs))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x, y, z, c=scalarMap.to_rgba(cs))
    scalarMap.set_array(cs)
    fig.colorbar(scalarMap)
    plt.show()
    
scatter3d(x,y,TE,CV)
plt.figure(4)
def color2d(x,y,cs, colorsMap='jet'):
    cm = plt.get_cmap(colorsMap)
    cNorm = matplotlib.colors.Normalize(vmin=min(cs), vmax=max(cs))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    plt.scatter(x, y, c=scalarMap.to_rgba(cs))
    #scalarMap.set_array(cs)
    #figure(4).colorbar(scalarMap)
    plt.show()
color2d(x,y,CV)


