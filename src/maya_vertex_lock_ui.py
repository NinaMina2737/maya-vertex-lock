#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import traceback

import maya.cmds as cmds
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2 import QtCore, QtWidgets

import maya_vertex_lock as mvl
reload(mvl)

WINDOW_TITLE = "Vertex Lock"


class VertexLockUI(MayaQWidgetBaseMixin, QtWidgets.QWidget):
    """
    The UI class for the Vertex Lock tool.
    """
    def __init__(self, *args, **kwargs):
        super(VertexLockUI, self).__init__(*args, **kwargs)

        self.setWindowTitle(WINDOW_TITLE)

        self.create_widget()
        self.create_layout()
        self.resize(250, 100)

    def create_widget(self):
        self.requirement_label = QtWidgets.QLabel()
        self.requirement_label.setObjectName("requirement_label")
        self.requirement_label.setText("Requirement: Select Vertex.")
        self.requirement_label.setAlignment(QtCore.Qt.AlignCenter)
        self.requirement_label.setWordWrap(True)

        self.toggle_button = QtWidgets.QPushButton()
        self.toggle_button.setObjectName("toggle_button")
        self.toggle_button.setText("Toggle Lock")
        self.toggle_button.clicked.connect(self.on_toggle_button_clicked)

        self.lock_button = QtWidgets.QPushButton()
        self.lock_button.setObjectName("lock_button")
        self.lock_button.setText("Lock Vertex")
        self.lock_button.clicked.connect(self.on_lock_button_clicked)

        self.unlock_button = QtWidgets.QPushButton()
        self.unlock_button.setObjectName("unlock_button")
        self.unlock_button.setText("Unlock Vertex")
        self.unlock_button.clicked.connect(self.on_unlock_button_clicked)

    def create_layout(self):
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.requirement_label)
        layout.addWidget(self.toggle_button)
        layout.addWidget(self.lock_button)
        layout.addWidget(self.unlock_button)
        self.setLayout(layout)

    def on_toggle_button_clicked(self):
        mvl.toggle_lock_vertex()

    def on_lock_button_clicked(self):
        mvl.lock_vertex_lock()

    def on_unlock_button_clicked(self):
        mvl.unlock_vertex_lock()


def execute():
    """
    Executes the UI.

    Raises:
        Exception: An error occurred.
    """
    try:
        # Check if the window already exists
        if cmds.window(WINDOW_TITLE, exists=True):
            cmds.deleteUI(WINDOW_TITLE)

        # Create the window
        window = VertexLockUI()
        window.show()
    except Exception as e:
        # Print the error message
        cmds.warning("An error occurred: {}".format(str(e)))
        # Print the traceback
        cmds.warning(traceback.format_exc())


if __name__ == "__main__":
    execute()
