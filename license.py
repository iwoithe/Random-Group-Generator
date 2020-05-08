#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  license.py
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

import tkinter as tk
import tkinter.ttk as ttk

from ttkthemes import ThemedTk

from settings import Settings

from tkinter.constants import *
from tkinter.scrolledtext import *

class License(ThemedTk):
    def __init__(self):
        super().__init__(themebg=True)

        self.settings = Settings()

        self.title("Random Group Generator - License")
        self.resizable(0, 0)

        if self.settings.theme != 'None':
            self.set_theme(self.settings.theme)

        self.set_widgets()
        self.layout_widgets()
        self.add_text()

    def set_widgets(self):
        # Frames
        self.frameLicense = ttk.Frame(self)
        # Scrolled Text
        self.scrlTextLicense = ScrolledText(self.frameLicense)
        self.scrlTextLicense.configure(state=DISABLED)

    def layout_widgets(self):
        # Frames
        self.frameLicense.grid(row=1, column=1, padx=5, pady=5)
        # Scrolled Text
        self.scrlTextLicense.grid(row=1, column=1, padx=5, pady=5)

    def add_text(self):
        self.scrlTextLicense.configure(state=NORMAL)
        with open('LICENSE') as f:
            for line in f:
                self.scrlTextLicense.insert(END, line)

        self.scrlTextLicense.configure(state=DISABLED)

if __name__ == '__main__':
    license = License()
    license.mainloop()
