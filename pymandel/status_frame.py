"""
Status Bar frame class for tkinter application.

This handles the status bar notifications.

Created on 7 Apr 2020

@author: semuadmin
"""

from tkinter import Frame, Label, StringVar, W, E


class StatusFrame(Frame):
    """
    Frame inheritance class for _status bar.
    """

    def __init__(self, app, *args, **kwargs):
        """
        Constructor
        """

        self.__app = app  # Reference to main application class
        self.__master = self.__app.get_master()  # Reference to root class (Tk)
        Frame.__init__(self, self.__master, *args, **kwargs)
        self._status = StringVar()

        self.body()

    def body(self):
        """
        Set up frame and widgets.
        """

        self.lbl_status = Label(self, textvariable=self._status, anchor=W)
        self.lbl_status.grid(column=0, row=0, sticky=(W, E))

    def set_status(self, message, color="black"):
        """
        Sets text of status bar.
        """

        self.lbl_status.config(fg=color)
        self._status.set("  " + message)

    def clear_status(self):
        """
        Clears text of status bar.
        """

        self._status.set("")
