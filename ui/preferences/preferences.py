#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  preferences.py
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

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .. import utils

class SettingsView(QListWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setup_ui()

    def setup_ui(self):
        settings = ["Customisation"]
        for setting in settings:
            setting_item = QListWidgetItem(setting, self)
            self.insertItem(settings.index(setting), setting_item)


class CustomisationLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        style_layout = QHBoxLayout()
        label_style = QLabel("Style:")
        self.combo_style = QComboBox()
        style_layout.addWidget(label_style)
        style_layout.addWidget(self.combo_style)

        # Main Layout
        widget = QWidget()
        layout = QVBoxLayout()

        layout.addLayout(style_layout)

        self.setLayout(layout)


class PreferencesDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.app = QApplication.instance()

        self.parent = parent

        self.setup_ui()

        self.setWindowTitle("Preferences")
        self.setWindowIcon(QIcon(".../../icon.png"))

    def setup_ui(self):
        # Settings
        settings_layout = QHBoxLayout()
        self.settings_view = SettingsView()
        self.settings_view.currentItemChanged.connect(self.update_stacked_settings)

        self.customisation_settings = CustomisationLayout()
        self.load_available_styles()

        self.stacked_settings = QStackedLayout()
        self.stacked_settings.addWidget(self.customisation_settings)

        self.stacked_settings.setCurrentIndex(0)

        settings_layout.addWidget(self.settings_view)
        settings_layout.addLayout(self.stacked_settings)

        # The button box
        btn_ok = QDialogButtonBox.Ok
        btn_apply = QDialogButtonBox.Apply
        btn_cancel = QDialogButtonBox.Cancel

        # IMPORTANT: Ok only exits the window, you need to click apply to save
        #            the settings
        button_box = QDialogButtonBox(btn_ok | btn_apply)
        button_box.accepted.connect(self.accept)
        button_box.clicked.connect(self.apply_settings)
        button_box.rejected.connect(self.reject)

        # Main Layout
        layout = QVBoxLayout()
        layout.addLayout(settings_layout)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def load_available_styles(self):
        styles = utils.load_styles_list_from_directory()
        self.customisation_settings.combo_style.addItems(styles)
        self.customisation_settings.combo_style.setCurrentText(self.parent.settings["style"])

    def save_settings(self):
        # Update the settings dictionary
        current_style = self.customisation_settings.combo_style.currentText().replace(" ", "_")
        self.parent.settings["style"] = current_style
        # Save the changes
        with open("data/settings.json", "w") as f:
            json.dump(self.parent.settings, f, indent=4)

    def apply_settings(self):
        # Apply the style
        new_style_name = self.customisation_settings.combo_style.currentText().replace(" ", "_")
        new_style = utils.load_style_from_file(os.path.join("data/styles/", new_style_name + ".qss"))
        utils.apply_style(new_style)

        self.save_settings()

    @pyqtSlot()
    def update_stacked_settings(self):
        self.stacked_settings.setCurrentIndex(self.settings_view.currentRow())
