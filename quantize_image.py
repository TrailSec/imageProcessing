#!/usr/bin/python
import sys
import os
from PIL import Image

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
img = Image.open(sys.argv[1])
outputImg = img.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=paletteSize)
outputImg.save(filename + '-quantized-' + str(paletteSize) + '-colors' + file_extension)

