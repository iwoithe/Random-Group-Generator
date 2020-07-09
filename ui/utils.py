import os
import glob

from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication

# Thanks to Alexander Huszagh for the solution of loading stylesheets
# https://stackoverflow.com/questions/48256772/dark-theme-for-qt-widgets
def load_style_from_file(file_path):
    file = QFile(file_path)
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    return stream.readAll()


def apply_style(style_stream):
    app = QApplication.instance()
    if app is None:
        raise SystemExit("Error: No QApplication is running")

    app.setStyleSheet(style_stream)


def load_styles_list_from_directory() -> list:
    styles = []
    # TODO: Find and also include .css files as well ("data/styles/*.css")
    valid_file_types = ["data/styles/*.qss"]
    for file_type in valid_file_types:
        files = glob.glob(file_type)
        for file in files:
            file = os.path.basename(file)
            file = file.rstrip(".csq").replace("_", " ").title()
            styles.append(file)

    styles.sort()

    return styles
