"""
Entry point for PyMandel Application.

Created on 12 Sep 2020

@author: semuadmin
"""

from tkinter import Tk
from pymandel.app import App

if __name__ == "__main__":
    ROOT = Tk()
    APP = App(ROOT)
    ROOT.mainloop()
