"""
Entry point for PyMandel Application.

Created on 12 Sep 2020

@author: semuadmin
"""

import sys
from tkinter import Tk
from pymandel.app import App


def main():
    """The main tkinter loop."""

    ROOT = Tk()
    APP = App(ROOT)
    ROOT.mainloop()


if __name__ == "__main__":
    sys.exit(main())
