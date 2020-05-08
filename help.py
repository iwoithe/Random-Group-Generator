#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  help.py
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

class Help(ThemedTk):
    def __init__(self):
        super().__init__(themebg=True)

        self.settings = Settings()

        self.title("Random Group Generator - Help")
        self.resizable(0, 0)

        if self.settings.theme != 'None':
            self.set_theme(self.settings.theme)

        self.set_widgets()
        self.layout_widgets()

    def set_widgets(self):
        pass

    def layout_widgets(self):
        pass

if __name__ == '__main__':
    help = Help()
    help.mainloop()
