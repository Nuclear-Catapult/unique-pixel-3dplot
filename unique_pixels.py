# https://stackoverflow.com/a/1109747

import matplotlib.pyplot as plt
from PIL import Image

im = Image.open('pic0000.bmp')

pixels = list(im.getdata())
width, height = im.size

pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

# filter every unique pixel
pixels = set([j for sub in pixels for j in sub])

x = [j[0] for j in pixels]
y = [j[1] for j in pixels]
z = [j[2] for j in pixels]

colors = ['#{0:0{1}X}'.format(pixel[0]*65536+pixel[1]*256+pixel[2], 6) for pixel in pixels]

# Creating figure 
fig = plt.figure() 
ax = fig.add_subplot(projection='3d') 

ax.set_xlim3d(0, 255)
ax.set_ylim3d(0, 255)
ax.set_zlim3d(0, 255)

# Creating plot 
ax.scatter(x, y, z, c = colors); 
plt.title("simple 3D scatter plot", ) 
plt.show()
