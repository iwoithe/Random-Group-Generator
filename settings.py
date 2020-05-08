#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  settings.py
#  
#  Copyright 2020 iwoithe <iwoithe@just42.net>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
import json

import tkinter as tk
import tkinter.ttk as ttk

from ttkthemes import ThemedTk, THEMES
from tkinter.constants import *

class Settings():
    def __init__(self):
        self.file = 'settings.json'
        self.load_settings(self.file)

        self.theme = self.settings['theme']

    def load_settings(self, file):
        with open(file) as f:
            self.settings = json.load(f)

    def save_settings(self, file):
        settings = {"theme": self.theme}
        with open(file, 'w') as f:
            json.dump(settings, f, indent=4)

class Preferences(ThemedTk, Settings):
    def __init__(self):
        ThemedTk.__init__(self, themebg=True)
        Settings.__init__(self)

        self.title("Random Group Generator - Preferences")
        self.resizable(0, 0)

        if self.theme != 'None':
            self.set_theme(self.theme)

        self.set_vars()
        self.set_widgets()
        self.layout_widgets()

    def set_vars(self):
        self.varTheme = tk.StringVar()
        self.varTheme.set(self.theme)

    def set_widgets(self):
        # Frames
        self.frameBase = ttk.Frame(self)
        self.frameNtbook = ttk.Frame(self.frameBase)
        # Notebook
        self.ntbookOptions = ttk.Notebook(self.frameNtbook, width=300, height=300)
        # Notebook Tabs
        self.tabAppearance = ttk.Frame(self.ntbookOptions)
        self.ntbookOptions.add(self.tabAppearance, padding=3)
        self.ntbookOptions.tab(0, text="Appearance", compound="none")
        # Labels
        self.lblTheme = ttk.Label(self.tabAppearance, text="Theme:")
        self.lblInfo = ttk.Label(self.tabAppearance, text="Please note that you have to\nrestart Random Group Generator for \nchanges to be implemented.", font=("TkMixedFont", 6, "italic"))
        # Comboboxes
        self.cmoboxTheme = ttk.Combobox(self.tabAppearance, textvar=self.varTheme, state='readonly', values=(['None', 'default'] + THEMES))
        # Buttons
        self.btnSave = ttk.Button(self.frameBase, text="Save", command=self.save)
        self.btnCancel = ttk.Button(self.frameBase, text="Cancel", command=self.cancel)

    def layout_widgets(self):
        # Frames
        self.frameBase.grid(row=1, column=1)
        self.frameNtbook.grid(row=1, column=1)
        # Notebook
        self.ntbookOptions.grid(row=1, column=1, padx=5, pady=5)
        # Labels
        self.lblTheme.grid(row=1, column=1, padx=5, pady=5)
        self.lblInfo.grid(row=2, column=2, padx=5, pady=5)
        # Comboboxes
        self.cmoboxTheme.grid(row=1, column=2, padx=5, pady=5)
        # Buttons
        self.btnSave.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        self.btnCancel.grid(row=2, column=1, padx=5, pady=5, sticky='e')

    def save(self):
        self.theme = self.get_current_theme()
        self.save_settings(self.file)
        self.cancel()

    def cancel(self):
        self.destroy()

    def get_current_theme(self):
        return self.cmoboxTheme.get()



if __name__ == '__main__':
    preferences = Preferences()
    preferences.mainloop()
