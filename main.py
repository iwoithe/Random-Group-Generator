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

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QHBoxLayout, QMenuBar, QFileDialog,
                             QStyle)

from ui.panels.editor import Editor
from ui.panels.groups import Groups
from ui.panels.options import Options

import core.generator as generator

# TODO: Check if a file has been modified and display an asterix
#       (*) next to the filename
# TODO: When closing, if a file has been modified, ask if you
#       want to save the files
# TODO: Add toggle features to toggle the views of some docks/panes.
#       Add toggle feature menu inside the view
# TODO: Use panes (like Atoms) instead of using QDockWidget

class RandomGroupGenerator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        # Menu Bar
        menu_bar = QMenuBar()
        # File
        action_file = menu_bar.addMenu("&File")
        action_file.addAction("New", self.new_file, QKeySequence.New)
        action_file.addAction("Open", self.open_files, QKeySequence.Open)
        action_file.addAction("Save", self.save_file, QKeySequence.Save)
        action_file.addSeparator()
        action_file.addAction("Quit", self.quit, QKeySequence.Quit)
        # Edit
        action_edit = menu_bar.addMenu("&Edit")
        action_edit.addAction("Preferences")
        # Help
        action_help = menu_bar.addMenu("&Help")
        action_help.addAction("Manual")
        action_help.addSeparator()
        action_help.addAction("About")
        action_help.addAction("About Qt", QApplication.instance().aboutQt)

        # Editor
        self.editor = Editor()

        # Groups
        groups = Groups()

        # Options
        options = Options(self.editor, groups, generator)

        editor_dock = self.addDockWidget(Qt.LeftDockWidgetArea, self.editor)
        options_dock = self.addDockWidget(Qt.RightDockWidgetArea, options)
        groups_dock = self.addDockWidget(Qt.RightDockWidgetArea, groups)

        self.setWindowTitle("Random Group Generator")
        self.setMenuBar(menu_bar)

    def new_file(self):
        self.editor.new_file()

    def save_file(self):
        open_files_path = ''
        # Options for the open dialog
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        # The variable _ is not used, hence its name
        file_name, _ = QFileDialog.getSaveFileName(self,
                "Save File",
                "",
                "Random Group Generator (*.rgg)", options=options)

        if file_name:
            if ('.rgg' in file_name):
                pass
            else:
                file_name += ".rgg"

            self.editor.save_file(file_name)

    def open_files(self):
        open_files_path = ''
        # Options for the open dialog
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        # The variable _ is not used, hence its name
        files, _ = QFileDialog.getOpenFileNames(self,
                "Open File/s", open_files_path,
                "Random Group Generator Files (*.rgg)", options=options)

        if files:
            self.openFilesPath = files[0]
            self.editor.load_files(files)

    def quit(self):
        self.destroy()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Temporarily set the style, until I've written my own styles
    if sys.platform == 'win32':
        app.setStyle("fusion")
    rgg = RandomGroupGenerator()
    rgg.show()
    sys.exit(app.exec_())
