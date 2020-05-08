#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  about.py
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

from settings import Settings

from ttkthemes import ThemedTk
from tkinter.constants import *

class About(ThemedTk):
    def __init__(self):
        super().__init__(themebg=True)

        self.settings = Settings()

        self.title("Random Group Generator - About")
        self.resizable(0, 0)

        if self.settings.theme != 'None':
            self.set_theme(self.settings.theme)

        self.set_widgets()
        self.layout_widgets()

    def set_widgets(self):
        # Frames
        self.frame = ttk.Frame(self)
        # Labels
        self.lblTitle = ttk.Label(self.frame, text="Random Group Generator", foreground='black', font=('TkFixedFont', 36, 'bold underline'))
        self.lblVersion = ttk.Label(self.frame, text="Version 0.2.1", foreground='black', font=('TkFixedFont', 18))
        self.lblAuthor = ttk.Label(self.frame, text="Created by iwoithe", foreground='black', font=('TkFixedFont', 28))
        self.lblLicense = ttk.Label(self.frame, text="Released under the GPL V3.0 license", foreground='black', font=('TkMixedFont', 24))
        self.lblIdeas = ttk.Label(self.frame, text="For any issures, bugs or improvements, \n\t      please e-mail:", foreground='black', font=('TkMixedFont', 20))
        self.lblEmail = ttk.Label(self.frame, text="iwoithe@just42.net", foreground='black', font=('TkMixedFont', 24, 'bold italic'))
        self.lblCopyright = ttk.Label(self.frame, text="Copyright © iwoithe 2020", foreground='black', font=('TkMixedFont', 12))
        

    def layout_widgets(self):
        # Frames
        self.frame.grid(row=1, column=1, padx=5, pady=5)
        # Labels
        self.lblTitle.grid(row=1, column=1, padx=5, pady=5)
        self.lblVersion.grid(row=2, column=1, padx=5, pady=5)
        self.lblAuthor.grid(row=3, column=1, padx=5, pady=5)
        self.lblLicense.grid(row=4, column=1, padx=5, pady=5)
        self.lblIdeas.grid(row=5, column=1, padx=5, pady=5)
        self.lblEmail.grid(row=6, column=1, padx=5, pady=5)
        self.lblCopyright.grid(row=7, column=1, padx=5, pady=(100, 5))

if __name__ == '__main__':
    about = About()
    about.mainloop()
