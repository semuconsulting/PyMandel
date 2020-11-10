"""
Menubar class for tkinter application.

This handles the menu bar.

Created on 27 Mar 2020

@author: semuadmin
"""

from tkinter import Menu

from .strings import (
    MENUFILE,
    MENUOPTIONS,
    MENUSAVE,
    MENUEXPORT,
    MENUIMPORT,
    MENUEXIT,
    MENUPLOT,
    MENUZOOM,
    MENUSPIN,
    MENUCAN,
    MENURST,
    MENUHIDESE,
    MENUHIDESB,
    MENUSHOWAX,
    MENUHOWTO,
    MENUABOUT,
    MENUHELP,
)


class MenuBar(Menu):
    """
    Menu inheritance class for menu bar.
    """

    def __init__(self, app, *args, **kwargs):
        """
        Constructor
        """

        self.__app = app  # Reference to main application class
        self.__master = self.__app.get_master()  # Reference to root class (Tk)
        Menu.__init__(self, self.__master, *args, **kwargs)

        # Create a pull-down menu for file operations
        self.file_menu = Menu(self, tearoff=False)
        self.file_menu.add_command(
            label=MENUSAVE, underline=1, command=self.__app.frm_settings.save_image
        )
        self.file_menu.add_command(
            label=MENUEXPORT, underline=1, command=self.__app.frm_settings.save_metadata
        )
        self.file_menu.add_command(
            label=MENUIMPORT,
            underline=1,
            command=self.__app.frm_settings.import_metadata,
        )
        self.file_menu.add_command(
            label=MENUEXIT, underline=1, accelerator="Ctrl-Q", command=self.__app.exit
        )
        self.add_cascade(menu=self.file_menu, label=MENUFILE)

        # Create a pull-down menu for options
        self.option_menu = Menu(self, tearoff=False)
        self.option_menu.add_command(
            label=MENUPLOT, underline=1, command=self.__app.frm_fractal.plot
        )
        self.option_menu.add_command(
            label=MENUZOOM, underline=1, command=self.__app.frm_fractal.animate_zoom
        )
        self.option_menu.add_command(
            label=MENUSPIN, underline=1, command=self.__app.frm_fractal.animate_spin
        )
        self.option_menu.add_command(
            label=MENUCAN, underline=1, command=self.__app.frm_fractal.cancel_press
        )
        self.option_menu.add_command(
            label=MENURST, underline=1, command=self.__app.frm_settings.reset
        )
        self.option_menu.add_command(
            label=MENUHIDESE, underline=1, command=self.__app.toggle_settings
        )
        self.option_menu.add_command(
            label=MENUHIDESB, underline=1, command=self.__app.toggle_status
        )
        self.option_menu.add_command(
            label=MENUSHOWAX, underline=1, command=self.__app.toggle_axes
        )
        self.add_cascade(menu=self.option_menu, label=MENUOPTIONS)

        # Create a pull-down menu for help operations
        self.help_menu = Menu(self, tearoff=False)
        self.help_menu.add_command(
            label=MENUHOWTO, underline=1, command=self.__app.howto
        )
        self.help_menu.add_command(
            label=MENUABOUT, underline=1, command=self.__app.about
        )
        self.add_cascade(menu=self.help_menu, label=MENUHELP)
