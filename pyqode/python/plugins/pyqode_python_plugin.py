# -*- coding: utf-8 -*-
"""
This file contains all the pyQode QtDesigner plugins.

Installation:
==================

run designer.pyw (Qt Designer must be installed on your system and must be
in your path on Windows)
"""
# This only works with PyQt, PySide does not support the QtDesigner module
from pyqode.python.editor import QPythonCodeEdit

PLUGINS_TYPES = {'QPythonCodeEdit': QPythonCodeEdit}

try:
    from pyqode.core.plugins.pyqode_core_plugin import QCodeEditPlugin

    class QPythonCodeEditPlugin(QCodeEditPlugin):
        _module = 'pyqode.python'        # path to the widget's module
        _class = 'QPythonCodeEdit'    # name of the widget class
        _name = "QPythonCodeEdit"
        _icon = None
        _type = QPythonCodeEdit

        def createWidget(self, parent):
            return QPythonCodeEdit(parent)
except ImportError:
    print("Cannot use pyQode plugins without PyQt4")
