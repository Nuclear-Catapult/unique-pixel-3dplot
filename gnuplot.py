import sys
import subprocess

from PIL import Image

im = Image.open(sys.argv[1])

pixels = set(im.getdata())

print(str(len(pixels))+" Unique Pixels", ) 

f = open("pixels.data", "w")

for pixel in pixels:
    f.write(str(pixel[0])+" "+str(pixel[1])+" "+str(pixel[2])+"\n")
f.close()

bashCommand = 'gnuplot script.plg'
print(bashCommand)

# https://stackoverflow.com/a/4256153
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print(output)
print(error)
