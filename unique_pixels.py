#!/usr/bin/python3

import sys
import matplotlib.pyplot as plt

from PIL import Image

im = Image.open(sys.argv[1])

pixels = set(im.getdata())

x = [j[0] for j in pixels]
y = [j[1] for j in pixels]
z = [j[2] for j in pixels]

colors = ['#{0:0{1}X}'.format(pixel[0]*65536+pixel[1]*256+pixel[2], 6) for pixel in pixels]

# Creating figure 
fig = plt.figure() 
ax = fig.add_subplot(projection='3d') 

# set axis lengths
ax.set_xlim3d(0, 255)
ax.set_ylim3d(0, 255)
ax.set_zlim3d(0, 255)

# set axis labels
ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')

# Creating plot 
ax.scatter(x, y, z, c = colors); 
plt.title(str(len(pixels))+" Unique Pixels", )
plt.show()
