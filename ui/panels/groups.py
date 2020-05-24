#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  groups.py
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
from PyQt5.QtWidgets import (QApplication, QWidget, QDockWidget,
                             QVBoxLayout, QTableWidget, QHeaderView)

class Groups(QDockWidget):
    def __init__(self):
        super().__init__("Groups")
        self.setFeatures(self.DockWidgetMovable)

        self.setup_ui()

    def setup_ui(self):
        # Groups are displayed in this table
        self.table_groups = QTableWidget()
        self.table_groups.setRowCount(1)
        self.table_groups.setColumnCount(1)

        self.table_groups.setHorizontalHeaderLabels(["People"])

        header = self.table_groups.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)

        # Main Layout
        widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(self.table_groups)

        widget.setLayout(layout)
        self.setWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    groups = Groups()
    groups.show()
    sys.exit(app.exec_())
