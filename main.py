#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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

import os
import sys
import random
import tkinter as tk
import tkinter.ttk as ttk

from help import Help
from about import About
from license import License
from settings import Settings, Preferences

from ttkthemes import ThemedTk
from tkinter.constants import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *

class MainWindow(ThemedTk):
    def __init__(self):
        super().__init__(themebg=True)

        self.settings = Settings()

        self.title("Random Group Generator")
        self.resizable(0, 0)

        self.iconImage = tk.PhotoImage(file="icon.png")
        self.iconphoto(True, self.iconImage)

        self.update_theme()
        self.set_variables()
        self.set_widgets()
        self.layout_widgets()
        self.setup_treeview()
        self.bind_shortcuts()
        self.update_entries()

    def set_variables(self):
        self.enteredNum = tk.StringVar()
        self.enteredNum.set("numberOfGroups")

    def set_widgets(self):
        # Frames
        self.frameNames = ttk.Frame(self)
        self.frameGroups = ttk.Frame(self)
        self.frameOptions = ttk.LabelFrame(self, text="Options")
        # Radiobuttons
        self.rbtnNumGroups = ttk.Radiobutton(self.frameOptions, text="Number of Groups:", value="numberOfGroups", variable=self.enteredNum)
        self.rbtnPeoplePerGroup = ttk.Radiobutton(self.frameOptions, text="People per Group:", value="peoplePerGroup", variable=self.enteredNum)
        # Entries
        self.entryNumGroups = ttk.Entry(self.frameOptions)
        self.entryPeoplePerGroup = ttk.Entry(self.frameOptions)
        # Buttons
        self.btnGenGroups = ttk.Button(self.frameOptions, text="Generate Groups", command=self.generate_groups)
        # Scrolled Text Areas
        # If you want a dark theme, bg="#5A5A5A" and fg="white"
        self.scrlTextNames = ScrolledText(self.frameNames, bg="white", fg="black", width=40, height=35, undo=True)
        # Scrolled Treeviews
        self.stvGroups = ttk.Treeview(self.frameGroups, height=20)
        self.stvGroups.configure(columns="Col1")
        self.stvGroups.heading("#0",text="")
        self.stvGroups.heading("#0",anchor="center")
        self.stvGroups.column("#0",width="30")
        self.stvGroups.column("#0",minwidth="20")
        self.stvGroups.column("#0",stretch="1")
        self.stvGroups.column("#0",anchor="w")
        self.stvGroups.heading("Col1",text="Group")
        self.stvGroups.heading("Col1",anchor="center")
        self.stvGroups.column("Col1",width="500")
        self.stvGroups.column("Col1",minwidth="100")
        self.stvGroups.column("Col1",stretch="1")
        self.stvGroups.column("Col1",anchor="w")
        # Menubar
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        self.mnuFile = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.mnuFile)
        self.mnuFile.add_command(label="Open", command=self.open_file)
        self.mnuFile.add_command(label="Save", command=self.save)
        self.mnuFile.add_separator()
        self.mnuFile.add_command(label="Preferences", command=self.preferences)
        self.mnuFile.add_separator()
        self.mnuFile.add_command(label="Quit", command=self.quit)

        self.mnuHelp = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.mnuHelp)
        self.mnuHelp.add_command(label="About", command=self.about)
        self.mnuHelp.add_command(label="License", command=self.license)
        self.mnuHelp.add_command(label="Open Manual (Coming Soon!)", state=DISABLED, command=self.help)

    def layout_widgets(self):
        # Frames
        self.frameNames.pack(padx=5, pady=5, side='left', expand=1)
        self.frameOptions.pack(padx=5, pady=5, side='top', expand=1)
        self.frameGroups.pack(padx=5, pady=5, side='bottom', expand=1)
        # Radiobuttons
        self.rbtnNumGroups.grid(row=1, column=1, padx=5, pady=5)
        self.rbtnPeoplePerGroup.grid(row=2, column=1, padx=5, pady=5)
        # Entries
        self.entryNumGroups.grid(row=1, column=2, padx=5, pady=5)
        self.entryPeoplePerGroup.grid(row=2, column=2, padx=5, pady=5)
        # Buttons
        self.btnGenGroups.grid(row=3, column=1, columnspan=2, padx=5, pady=5)
        # Scrolled Text Areas
        self.scrlTextNames.grid(row=1, column=1, rowspan=2, padx=5, pady=5)
        # Scrolled Treeviews
        self.stvGroups.grid(row=1, column=1, padx=5, pady=5)

    def generate_groups(self):
        groups = self.return_groups()
        self.display_groups(groups)

    def read_names(self):
        ''' Read the boxNameEntry widget '''
        names = []
        text = self.scrlTextNames.get(0.0, index2=END)
        string = ''

        for char in text:
            if str(char) != '\n':
                string += str(char)
            else:
                names.append(string)
                string = ''

        for name in names:
            if name == '':
                del names[names.index(name)]

        self.num_students = len(names)

        return names

    def get_names_string(self):
        names = self.read_names()
        names_string = ""
        for name in names:
            names_string += name + "\n"

        return names_string

    def get_num_groups(self):
        try:
            if ((int(self.entryNumGroups.get()) * -1) == abs(int(self.entryNumGroups.get()))):
                showwarning("Error", "Please enter a positve number")
                return 1
        except:
            showwarning("Error", "Please enter a positive number")
            return 1

        try:
            return int(self.entryNumGroups.get())
        except:
            showwarning("Error", "Please enter a positive number")
            return 1

    def get_people_per_group(self):
        try:
            if ((int(self.entryPeoplePerGroup.get()) * -1) == abs(int(self.entryPeoplePerGroup.get()))):
                showwarning("Error", "Please enter a positve number")
                return 1
        except:
            showwarning("Error", "Please enter a positive number")
            return 1
        try:
            return int(self.entryPeoplePerGroup.get())
        except:
            showwarning("Error", "Please enter a positive number")
            return 1

    def return_groups(self):
        ''' Return the groups

            The groups raw data are based on the form of an array:

            groups = [[1, 4, ['Amanda', 'Nolak', 'GNU', 'Tux']],
                      [2, 4, ['Emule', 'Suzanne', 'Wilber', 'Beastie']],
                      [3, 4, ['Sara the Wizard', 'Sara the Racer', 'Adiumy']],
                      [4, 3, ['Pidgen', 'Puffy', 'Kiki']]]

            The first number is the group number, the second number is how many
            people are in that group and the array is for the list of people [names]
            in that group. You can optionally take out the second number (the default)'''

        names = self.read_names()
        random.shuffle(names)

        if self.enteredNum.get() == "numberOfGroups":
            num_groups = self.get_num_groups()
            try:
                people_per_group = int(self.num_students / int(num_groups))
            except ZeroDivisionError:
                showwarning("Error", "Please enter a number greater than 0...")

        if self.enteredNum.get() == "peoplePerGroup":
            people_per_group = self.get_people_per_group()
            try:
                num_groups = int(self.num_students / int(people_per_group))
            except ZeroDivisionError:
                showwarning("Error", "Please enter a number greater than 0")

        groups = []
        group_num = 1

        while len(names) > 0:
            people_names = []
            if len(names) > people_per_group:
                people_names = names[:people_per_group]
                del names[:people_per_group]
                #groups.append([group_num, people_per_group, people_names])
                groups.append([group_num, people_names])
                group_num += 1
            else:
                people_names = names.copy()
                del names[:len(people_names)]
                groups.append([group_num, people_names])

        return groups

    def setup_treeview(self):
        self.ColHeads = ['', 'Group']
        self.stvGroups.configure(columns=self.ColHeads, show="headings")
        for col in self.ColHeads:
            self.stvGroups.heading(col, text=col.title())
            if col == '':
                self.stvGroups.column(col, width=30)
            if col == 'Group':
                self.stvGroups.column(col, width=500)

    def clear_data_grid(self):
        for c in self.stvGroups.get_children(''):
            self.stvGroups.delete(c)

    def display_groups(self, groups):
        self.clear_data_grid()
        for group in groups:
            self.stvGroups.insert('', 'end', values=group, tags=('font'))
            self.stvGroups.tag_configure('font', font=(None, 12))

    def preferences(self):
        preferences = Preferences()
        preferences.mainloop()
        #self.update_theme()

    def update_theme(self):
        if self.settings.theme != 'None':
            self.set_theme(self.settings.theme)

    def update_entries(self):
        if self.enteredNum.get() == "numberOfGroups":
            self.entryNumGroups.configure(state=NORMAL)
            self.entryPeoplePerGroup.configure(state=DISABLED)
        elif self.enteredNum.get() == "peoplePerGroup":
            self.entryNumGroups.configure(state=DISABLED)
            self.entryPeoplePerGroup.configure(state=NORMAL)
        else:
            self.entryNumGroups.configure(state=NORMAL)
            self.entryPeoplePerGroup.configure(state=NORMAL)

        self.after(1, self.update_entries)

    def bind_shortcuts(self):
        self.bind_all('<Control-o>', self.open_file)
        self.bind_all('<Control-s>', self.save)
        self.bind_all('<Control-q>', self.quit)

    def open_file(self, event=None):
        ''' The code that opens a class list '''
        # May have to change the asksaveasfilename to askdirectory
        # The file extention of group lists is .rgg
        file = askopenfilename(filetypes=[("Random Group Generator files", ".rgg")])
        if file != '':
            with open(file) as f:
                for name in f:
                    self.scrlTextNames.insert(END, name)

    def save(self, event=None):
        ''' The code that saves the class list '''
        # May have to change the asksaveasfilename to askdirectory
        # The file extention of group lists is .rgg

        savefilename = asksaveasfilename(filetypes=[("Random Group Generator files", ".rgg")])
        if savefilename != '':
            names = self.get_names_string()
            if ('.rgg' in savefilename):
                file = savefilename
                with open(file, mode='w') as f:
                    f.write(names)
            else:
                file = os.path.join(savefilename + ".rgg")
                with open(file, mode='w') as f:
                    f.write(names)

    def about(self):
        about = About()
        about.mainloop()

    def license(self):
        license = License()
        license.mainloop()

    def help(self):
        help = Help()
        help.mainloop()

    def quit(self, event=None):
        self.destroy()
        sys.exit()

if __name__ == '__main__':
    rgg = MainWindow()
    rgg.mainloop()
