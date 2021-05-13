#!/usr/bin/env python
"""
Command line utility to create numpy color map arrays suitable for use by PyMandel
from image files containing suitable color gradients e.g. created using GIMP's gradient tool.
It currently only handles RGB or RGBA formats.

make_colormap mapname=mymap input=mymap.png output=mymap_colormap.py levels=256

Created on 24 Apr 2020

:author: semuadmin
:copyright: SEMU Consulting 2020
:license: BSD 3-Clause
"""

import sys

from PIL import Image


def make_colormap(**kwargs):
    """
    Scan image file and create array of rgb values

    :param kwargs: optional keyword args
    """

    print("Parameters passed: ", kwargs)

    mapname = kwargs.get("mapname", "mymap")
    infile = kwargs.get("input", mapname + ".png")

    try:
        image = Image.open(infile)
    except FileNotFoundError as err:
        print(f"Input file {infile} not found \n{err}")
        return

    mode = image.mode
    if mode not in ("RGB", "RGBA"):
        print(f"Invalid image mode {mode} - must be RGB or RGBA")

    levels = int(kwargs.get("levels", image.width))
    if levels > image.width:
        levels = image.width
    outfile = kwargs.get("output", mapname + str(levels) + "_colormap.py")

    file = open(outfile, "a")
    file.write("from numpy import array\n\n")
    file.write(
        "#****************************************************************************************\n"
        f"# {str(levels)}-level colormap created by make_colormap utility from file {infile}\n"
        "#****************************************************************************************\n"
    )
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
            red, grn, blu, alpha = image.getpixel((pix, 0))
        else:
            red, grn, blu = image.getpixel((pix, 0))
        file.write("[" + str(red) + "," + str(grn) + "," + str(blu) + end)

    image.close()
    file.close()

    print(str(levels) + "-level colormap file " + outfile + " created")


def main(args=None):
    """ CLI entry point. """

    if len(sys.argv) > 1:
        if sys.argv[1] in {"-h", "--h", "help", "-help", "--help", "-H"}:
            print(
                " make_colormap.py is a simple command line utility to create",
                "a numpy RGB colormap suitable for importing into PyMandel.\n\n",
                "Usage: make_colormap mapname=mymap input=mymap.png output=mymap_colormap.py levels=256",
            )
            sys.exit()

    make_colormap(**dict(arg.split("=") for arg in sys.argv[1:]))


if __name__ == "__main__":
    sys.exit(main())
