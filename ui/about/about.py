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

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QDialog, QWidget,
                             QHBoxLayout, QVBoxLayout,
                             QTabWidget, QTextEdit, QLabel,
                             QDialogButtonBox)


# TODO: Change the icon/logo to the inverted icon/logo
class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setup_ui()

        self.setWindowTitle("About")
        self.setWindowIcon(QIcon(".../../icon.png"))
        self.resize(600, 400)

    def setup_ui(self):
        # Title
        lbl_icon = QLabel()
        lbl_icon.setPixmap(QPixmap(".../../icon.png"))
        lbl_icon.setFixedSize(144, 144)

        lbl_title = QLabel("<h1>Random Group Generator</h1>")

        title_layout = QHBoxLayout()
        title_layout.addWidget(lbl_icon)
        title_layout.addWidget(lbl_title)

        tabs = QTabWidget()
        tabs.setFixedHeight(400)

        # About (Show README)
        about_tab = QWidget()

        readme_text = QTextEdit()
        readme_text.setReadOnly(True)
        with open('.../../README.md') as f:
            markdown_string = ""
            for line in f:
                markdown_string += line

        readme_text.setMarkdown(markdown_string)

        about_layout = QVBoxLayout()
        about_layout.addWidget(readme_text)
        about_tab.setLayout(about_layout)

        tabs.addTab(about_tab, "About")

        # License
        licence_tab = QWidget()

        licence_text = QTextEdit()
        licence_text.setReadOnly(True)
        with open('.../../LICENSE') as f:
            text_string = ""
            for line in f:
                text_string += line

        licence_text.setPlainText(text_string)

        licence_layout = QVBoxLayout()
        licence_layout.addWidget(licence_text)
        licence_tab.setLayout(licence_layout)

        tabs.addTab(licence_tab, "Licence")

        # 3rd Party
        third_party_tab = QWidget()

        third_party_text = QTextEdit()
        third_party_text.setReadOnly(True)

        third_party_libs = '''
        <h2>3rd Party Libraries Used:</h2>
        <ul>
            <li><a href="https://www.riverbankcomputing.com/software/pyqt/download5">PyQt</a> 5.14.1<br>License: GPLv3</li>
            <li><a href="https://pypi.org/project/openpyxl">openpyxl</a> 3.0.3<br>License: MIT</li>
        </ul>'''
        third_party_text.setHtml(third_party_libs)

        third_party_layout = QVBoxLayout()
        third_party_layout.addWidget(third_party_text)
        third_party_tab.setLayout(third_party_layout)

        tabs.addTab(third_party_tab, "3rd Party Libraries")

        # Author
        lbl_author = QLabel("<center><p>Created by iwoithe</p></center>")

        # Either use an Ok button or Close button
        QBtn = QDialogButtonBox.Ok
        button_box = QDialogButtonBox(QBtn)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        # Main Layout
        layout = QVBoxLayout()

        layout.addLayout(title_layout)
        layout.addWidget(tabs)
        layout.addWidget(lbl_author)
        layout.addWidget(button_box)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Temporarily set the style, until I've written my own styles
    app.setStyle("fusion")
    about = AboutDialog()
    about.show()
    sys.exit(app.exec_())
