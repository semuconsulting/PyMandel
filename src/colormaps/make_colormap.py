#!/usr/bin/env python
"""
Command line utility to create numpy color map arrays suitable for use by PyMandel
from image files containing suitable color gradients e.g. created using GIMP's gradient tool.
It currently only handles RGB or RGBA formats.

make_colormap --mapname mymap --input mymap.png --output mymap_colormap.py --levels 256

Created on 24 Apr 2020

:author: semuadmin
:copyright: SEMU Consulting 2020
:license: BSD 3-Clause
"""

import sys
from argparse import SUPPRESS, ArgumentDefaultsHelpFormatter, ArgumentParser

from PIL import Image

from pymandel._version import __version__ as VERSION

EPILOG = (
    "© 2021 SEMU Consulting GPLv3 license - https://github.com/semuconsulting/PyMandel/"
)


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
    levels = min(levels, image.width)
    outfile = kwargs.get("output", mapname + str(levels) + "_colormap.py")

    with open(outfile, "a", encoding="utf-8") as file:
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

        print(str(levels) + "-level colormap file " + outfile + " created")


def main():
    """CLI entry point."""

    arp = ArgumentParser(
        epilog=EPILOG,
        formatter_class=ArgumentDefaultsHelpFormatter,
        argument_default=SUPPRESS,
    )
    arp.add_argument("-V", "--version", action="version", version="%(prog)s " + VERSION)
    arp.add_argument("--mapname", help="Map name", default="mymap")
    arp.add_argument("--input", help="Input image filename", default="mymap.png")
    arp.add_argument("--levels", help="Color levels", type=int, default=256)
    arp.add_argument("--output", help="Output filename", default="mymap_colormap.py")

    kwargs = vars(arp.parse_args())
    make_colormap(**kwargs)


if __name__ == "__main__":
    sys.exit(main())
