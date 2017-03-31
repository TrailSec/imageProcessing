#!/usr/bin/python
import sys
import os
from PIL import Image

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def rgb2int(r, g, b):
    return (int(r) << 16) + (int(g) << 8) + int(b)

# Check if user input matches what we want
if len(sys.argv) < 3:
    print 'ERROR: Missing input param! (eg. "python ' + sys.argv[0] + ' <filename_of_image> <palette_size>")'
    sys.exit(0)

# Check if input (filename_of_image) is a valid PATH
if not os.path.isfile(sys.argv[1]):
    print 'ERROR: "' + sys.argv[1] + '" is an invalid file path!'
    sys.exit(0)

# Check if input (palette_size) is a valid integer
try:
   paletteSize = int(sys.argv[2])
except ValueError:
   print 'ERROR: "' + sys.argv[2] + '" is not an integer!'
   sys.exit(0)

# Check if input (filename_of_image) is a valid file type
filename, file_extension = os.path.splitext(sys.argv[1])
if file_extension not in ['.png', '.jpeg']:
   print 'ERROR: "' + sys.argv[2] + '" is not a .PNG or .JPEG image!'
   sys.exit(0)

########################################
# Start converting image >_<
########################################

# Reduce color depth of image
img = Image.open(sys.argv[1])
outputImg = img.convert('P', palette=Image.ADAPTIVE, colors=paletteSize).convert('RGB')
outputImg.save(filename + '-quantized-' + str(paletteSize) + '-colors' + file_extension)

# Output one dimensional pixel array of the converted image in raster order
pixelList = list(outputImg.getdata())
outputImg2 = [rgb2int(pixel[0], pixel[1], pixel[2]) for pixel in pixelList]
f = open(filename + '-outputBinary.txt', 'w')
f.write('{' + ','.join(str(e) for e in outputImg2) + '}\n')
f.close()

# Output list of all colors used in converted image
paletteList = [rgb2int(c[0], c[1], c[2]) for a, c in list(outputImg.getcolors())]
f = open(filename + '-palette.txt', 'w')
f.write('{' + ','.join(str(e) for e in paletteList) + '}\n')
f.close()
