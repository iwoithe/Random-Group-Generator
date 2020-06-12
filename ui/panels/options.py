#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  options.py
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
                             QHBoxLayout, QVBoxLayout, QRadioButton,
                             QPushButton, QSpinBox, QTableWidgetItem,
                             QMessageBox, QErrorMessage)

class Options(QDockWidget):
    def __init__(self, editor, groups, generator):
        super().__init__("Options")
        self.setFeatures(self.DockWidgetMovable)

        self.editor = editor
        self.groups = groups
        self.generator = generator

        self.generate_option = 'num_groups'

        self.groups_list = [[1, ['']]]

        self.setup_ui()

    def setup_ui(self):
        # Number of Groups
        layout_num_groups = QHBoxLayout()

        rbtn_num_groups = QRadioButton("Number of Groups:")
        rbtn_num_groups.option = 'num_groups'
        rbtn_num_groups.setChecked(True)
        rbtn_num_groups.toggled.connect(self.set_generate_option)

        self.spin_num_groups = QSpinBox()
        self.spin_num_groups.setMinimum(1)
        self.spin_num_groups.setSingleStep(1)

        layout_num_groups.addWidget(rbtn_num_groups)
        layout_num_groups.addWidget(self.spin_num_groups)

        # People per Group
        layout_people_per_group = QHBoxLayout()

        rbtn_num_groups = QRadioButton("People per Group:")
        rbtn_num_groups.option = 'people_per_group'
        rbtn_num_groups.toggled.connect(self.set_generate_option)

        self.spin_people_per_group = QSpinBox()
        self.spin_people_per_group.setMinimum(1)
        self.spin_people_per_group.setSingleStep(1)

        layout_people_per_group.addWidget(rbtn_num_groups)
        layout_people_per_group.addWidget(self.spin_people_per_group)

        # Generate Button
        btn_generate = QPushButton("Generate!")
        btn_generate.clicked.connect(self.generate_groups)

        # Main Layout
        widget = QWidget()
        layout = QVBoxLayout()

        layout.addLayout(layout_num_groups)
        layout.addLayout(layout_people_per_group)
        layout.addWidget(btn_generate)

        widget.setLayout(layout)
        self.setWidget(widget)

    def set_generate_option(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.generate_option = radio_button.option

    def generate_groups(self):
        names = []

        try:
            current_file = self.editor.tabs.currentWidget()
            text = current_file.editor.toPlainText()
        except AttributeError as e:
            error = QMessageBox()
            error.warning(self.parentWidget(), "Error", ("Please have a file open. The original error: \n\n" + str(e)))
            return


        for name in text.split("\n"):
            if name != '':
                names.append(name)

        if (self.generate_option == 'num_groups'):
            groups = self.generator.generate_groups(names, num_groups=self.spin_num_groups.value())
        elif (self.generate_option == 'people_per_group'):
            groups = self.generator.generate_groups(names, people_per_group=self.spin_people_per_group.value())
        else:
            groups = [[1, ['']]]

        self.groups_list = groups

        self.groups.table_groups.setRowCount(len(groups))

        str_groups = []

        for group in groups:
            str_people = ''
            index = 0
            for person in group[1]:
                if index < (len(group[1]) - 1):
                    str_people += person + " , "
                else:
                    str_people += person

                index += 1

            str_groups.append(str_people)

        for str_group in str_groups:
            self.groups.table_groups.setItem(0, str_groups.index(str_group), QTableWidgetItem(str_group))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    options = Options()
    options.show()
    sys.exit(app.exec_())
