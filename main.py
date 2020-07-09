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
import json

import ui.about.about as about

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QHBoxLayout, QMenuBar, QFileDialog,
                             QTabWidget, QAction)

import ui.utils

from ui.panels.editor import Editor
from ui.panels.groups import Groups
from ui.panels.options import Options

from ui.about.about import AboutDialog
from ui.preferences.preferences import PreferencesDialog

import core.generator as generator

# TODO: Check if a file has been modified and display an asterix
#       (*) next to the filename
# TODO: When closing, if a file has been modified, ask if you
#       want to save the files
# TODO: Use panes (like Atoms) instead of using QDockWidget


class RandomGroupGenerator(QMainWindow):

    settings_file = "data/settings.json"
    with open(settings_file) as f:
        settings = json.loads(f.read())

    def __init__(self):
        super().__init__()

        self.save_file_path = ''
        self.open_files_path = ''
        self.import_files_path = ''
        self.export_files_path = ''

        style = ui.utils.load_style_from_file(os.path.join("data/styles/", self.settings["style"] + ".qss"))
        ui.utils.apply_style(style)

        self.setup_ui()

    def setup_ui(self):
        # Editor
        self.editor = Editor()

        # Groups
        self.groups = Groups()

        # Options
        self.options = Options(self.editor, self.groups, generator)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.editor)
        self.addDockWidget(Qt.RightDockWidgetArea, self.options)
        self.addDockWidget(Qt.RightDockWidgetArea, self.groups)

        self.setTabPosition(Qt.AllDockWidgetAreas, QTabWidget.North)

        self.setDockOptions(self.AnimatedDocks | self.AllowNestedDocks | self.AllowTabbedDocks | self.GroupedDragging)

        self.setWindowTitle("Random Group Generator")
        menu_bar = self.create_menu_bar()
        self.setMenuBar(menu_bar)
        self.setWindowIcon(QIcon("icon.png"))

    def create_menu_bar(self):
        # Menu Bar
        menu_bar = QMenuBar()
        # File
        action_file = menu_bar.addMenu("&File")
        action_file.addAction("New", self.new_file, QKeySequence.New)
        action_file.addAction("Open", self.open_files, QKeySequence.Open)
        action_file.addAction("Save", self.save_file, QKeySequence.Save)
        action_file.addSeparator()
        action_file.addAction("Import", self.import_file)
        action_file.addAction("Export", self.export_file)
        action_file.addSeparator()
        action_file.addAction("Quit", self.quit, QKeySequence.Quit)
        # Edit
        action_edit = menu_bar.addMenu("&Edit")
        action_edit.addAction("Preferences", self.show_preferences)
        # View
        action_view = menu_bar.addMenu("&View")
        view_panels = action_view.addMenu("Panels")
        view_panels.addAction(self.editor.toggleViewAction())
        view_panels.addAction(self.options.toggleViewAction())
        view_panels.addAction(self.groups.toggleViewAction())
        # Help
        action_help = menu_bar.addMenu("&Help")
        action_help.addAction("About", self.show_about)
        action_help.addAction("About Qt", QApplication.instance().aboutQt)

        return menu_bar

    def new_file(self):
        self.editor.new_file()

    def save_file(self):
        # Options for the save dialog
        options = QFileDialog.Options()

        # The variable _ is not used, hence its name
        file, _ = QFileDialog.getSaveFileName(self,
                "Save File",
                self.save_file_path,
                "Random Group Generator (*.rgg)", options=options)

        if file:
            if ('.rgg' in file):
                pass
            else:
                file += ".rgg"

            self.save_files_path = file
            self.editor.save_file(file)

    def open_files(self):
        open_files_path = ''

        # Options for the open dialog
        options = QFileDialog.Options()

        # The variable _ is not used, hence its name
        files, _ = QFileDialog.getOpenFileNames(self,
                "Open File/s", open_files_path,
                "Random Group Generator Files (*.rgg)", options=options)

        if files:
            self.open_files_path = files[0]
            self.editor.load_files(files)

    def import_file(self):
        # Options for the open dialog
        options = QFileDialog.Options()

        files, type = QFileDialog.getOpenFileNames(self,
                "Import File/s", self.import_files_path,
                "Comma Seperated Values (*.csv);;Microsoft Excel Spreadsheets (*.xlsx)",
                options=options)

        if files:
            self.import_files_path = files[0]
            self.editor.import_files(files, type)

    def export_file(self):
        # Options for the open dialog
        options = QFileDialog.Options()

        file, file_type = QFileDialog.getSaveFileName(self,
                "Export Groups", self.export_files_path,
                "Comma Seperated Values (*.csv);;Microsoft Excel Spreadsheets (*.xlsx)",
                options=options)

        if file:
            self.export_files_path = file

            self.editor.export_file(self.options.groups_list, file, file_type)

    def show_preferences(self):
        preferences_dialog = PreferencesDialog(self)
        preferences_dialog.exec_()

    def show_about(self):
        about_dialog = AboutDialog(self)
        about_dialog.exec_()

    def quit(self):
        self.destroy()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Temporarily set the style, until I've written my own styles
    app.setStyle("fusion")
    rgg = RandomGroupGenerator()
    rgg.show()
    sys.exit(app.exec_())
