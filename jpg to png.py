import os
import sys
from PIL import Image
from pathlib import Path

out = "C:\\Users\\tyagi\PycharmProjects\Image\\"
folder = (out + sys.argv[1])
new_folder = (out + sys.argv[2])

os.mkdir(new_folder)

for image in (os.listdir(folder)):
    filepath = folder + '{}'.format(image)
    filepath2 = new_folder + '{}.png'.format(image)
    im = Image.open(filepath)
    im.save(filepath2,'png')
    print('Done')