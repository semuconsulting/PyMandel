#!/usr/bin/env python
'''
Command line utility to create numpy color map arrays suitable for use by Mandelpy
from image files containing suitable color gradients e.g. created using GIMP's gradient tool.
It currently only handles RGB or RGBA formats.

python make_colormap.py mapname=mymap input=mymap.png output=mymap_colormap.py levels=256

Created on 24 Apr 2020

@author: semuadmin
'''

import sys

from PIL import Image

def make_colormap(**kwargs):
    '''
    Scan image file and create array of rgb values
    '''

    print("Parameters passed: ", kwargs)

    mapname = kwargs.get('mapname', 'mymap')
    infile = kwargs.get('input', mapname + '.png')

    image = Image.open(infile)
    mode = image.mode
    if mode not in ("RGB", "RGBA"):
        print("Image must be RGB or RGBA")

    levels = int(kwargs.get('levels', image.width))
    if levels > image.width:
        levels = image.width
    outfile = kwargs.get('output', mapname + str(levels) + "_colormap.py")

    file = open(outfile, 'a')
    file.write("from numpy import array\n\n")
    file.write("'''\n" + str(levels) + "-level colormap created by gen_colormap" \
               + " utility from file " + infile + "\n'''\n")
    file.write(mapname + " = array([ \\\n")

    for x_axis in range(levels):
        pix = int(x_axis * image.width / levels)
        if x_axis == levels - 1:
            end = "]])\n"
        elif x_axis % 4 == 3:
            end = "],\n"
        else:
            end = "],"
        if mode == "RGBA":
            red, grn, blu, alpha = image.getpixel((pix, 0))  # pylint: disable=W0612
        else:
            red, grn, blu = image.getpixel((pix, 0))
        file.write("[" + str(red) + "," + str(grn) + "," + str(blu) + end)

    image.close()
    file.write("'''\nEnd of colormap from file " + infile + "\n'''\n")
    file.close()

    print(str(levels) + "-level colormap file " + outfile + " created")

if __name__ == "__main__":

    make_colormap(**dict(arg.split('=') for arg in sys.argv[1:]))
