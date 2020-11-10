"""
How To Dialog Box class for tkinter application.

Created on 19 Apr 2020

@author: semuadmin
"""

from tkinter import Toplevel, Label, Button, LEFT
from webbrowser import open_new_tab

from .strings import HELPTXT, COPYRIGHTTXT, DLGHOWTO, GITHUBURL


class HowtoDialog:
    """
    How To dialog box class
    """

    def __init__(self, app):
        """
        Initialise Toplevel dialog
        """

        self.__app = app  # Reference to main application class
        self.__master = self.__app.get_master()  # Reference to root class (Tk)
        self._dialog = Toplevel()
        self._dialog.title = DLGHOWTO
        self._dialog.geometry(
            "+%d+%d"
            % (self.__master.winfo_rootx() + 50, self.__master.winfo_rooty() + 50)
        )
        self._dialog.attributes("-topmost", "true")

        self.body()

    def body(self):
        """
        Set up widgets
        """

        # Create widgets
        self.lbl_title = Label(self._dialog, text=DLGHOWTO)
        self.lbl_title.config(font=("Verdana", 16))

        self.lbl_desc = Label(self._dialog, justify=LEFT, text=HELPTXT, wraplength=500)

        self.lbl_copyright = Label(
            self._dialog, text=COPYRIGHTTXT, fg="blue", cursor="hand2"
        )
        self.btn_ok = Button(self._dialog, text="OK", width=8, command=self.ok_press)

        # Arrange widgets
        self.lbl_title.grid(column=0, row=0, padx=5, pady=5)
        self.lbl_desc.grid(column=0, row=2, padx=5, pady=5)
        self.lbl_copyright.grid(column=0, row=3, padx=5, pady=5)
        self.btn_ok.grid(column=0, row=5, ipadx=3, ipady=3, padx=5, pady=5)

        # Bind commands and hotkeys
        self.lbl_copyright.bind("<Button-1>", lambda e: open_new_tab(GITHUBURL))
        self.btn_ok.bind("<Return>", self.ok_press)
        self.btn_ok.focus_set()

    def ok_press(self, *args, **kwargs):
        """
        Handle OK button press
        """

        self.__master.update_idletasks()
        self._dialog.destroy()
