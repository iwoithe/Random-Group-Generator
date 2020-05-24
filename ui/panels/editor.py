#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  editor.py
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
from PyQt5.QtWidgets import (QApplication, QWidget, QDockWidget,
                             QHBoxLayout, QVBoxLayout, QTabWidget,
                             QPlainTextEdit)

class Editor(QDockWidget):

    files_open = []

    def __init__(self):
        super().__init__("Editor")
        self.setFeatures(self.DockWidgetMovable)

        self.setup_ui()

    def setup_ui(self):
        self.tabs = QTabWidget()
        self.tabs.setMovable(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        # Load Files
        if (len(self.files_open) > 0):
            self.load_files(self.files_open)
        else:
            self.new_file()

        # Main Layout
        widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(self.tabs)

        widget.setLayout(layout)
        self.setWidget(widget)

    def close_tab(self, i):
        self.tabs.removeTab(i)

    def new_file(self):
        file_tab = QWidget()
        layout = QHBoxLayout()

        file_tab.editor = QPlainTextEdit()

        layout.addWidget(file_tab.editor)
        file_tab.setLayout(layout)
        self.tabs.addTab(file_tab, "untitled.rgg")

    def save_file(self, file):
        current_file = self.tabs.currentWidget()
        text = current_file.editor.toPlainText()

        with open(file, 'w') as f:
            f.write(text)

        self.tabs.setTabText(self.tabs.indexOf(current_file), os.path.basename(file))

    def load_files(self, files):
        for file in files:
            file_tab = QWidget()
            layout = QHBoxLayout()

            file_tab.editor = QPlainTextEdit()

            with open(file) as f:
                for line in f:
                    file_tab.editor.insertPlainText(line)

            layout.addWidget(file_tab.editor)

            file_tab.setLayout(layout)
            self.tabs.addTab(file_tab, os.path.basename(file))

            self.tabs.setCurrentWidget(file_tab)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = Editor()
    editor.show()
    sys.exit(app.exec_())
