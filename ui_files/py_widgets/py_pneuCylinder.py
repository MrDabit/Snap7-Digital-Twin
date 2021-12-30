# --------------------------------------------------------------------------------------
# | Py module: py_pneuCylinder.py                                                            |
# | Author: David García Rincón                                                        |
# | Date: 20211124                                                                     |
# | Version: 1.0 x64                                                                   |
# | Purpose: free software for testing and developing. Right working is not guarantied |
# --------------------------------------------------------------------------------------
# |                                        description                                 |
# --------------------------------------------------------------------------------------
# | Custom QTwidget                                                                    |
# | Definition of a pneumatic cilider model                                            |
# |                                                                                    |
# --------------------------------------------------------------------------------------

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class pyPneuCylinder(QLabel):
    def __init__(self, extended, retracted, position, orderExtend, orderRetract):
        super(pyPneuCylinder, self).__init__()
        self.extended = extended
        self.retracted = retracted
        self.position = position
        self.orderExtend = orderExtend
        self.orderRetract = orderRetract
        self.barrelColor = "#0000ff"
        self.pistonColor = "#BCBCBC"

        self.cylinder = QLabel(self)
        self.cylinder.setGeometry(QRect(0, 0, 30, 20))
        self.cylinder.setText("c1")

    # Create a standar Widget label.

    # draw new items

    def paintEvent(self, e):
        # set painter
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)

        """rect = QRect(0, 0, self.cylinder.width(), self.cylinder.height())
        p.setBrush(QColor(self._barrelColor))
        p.drawRoundedRect(0, 0, rect.width(), self.cylinder.height(),
                          self.height()/2, 14)"""
        #rect = QRect(0, 0, 50, 10)
        p.setBrush(QColor(self.barrelColor))
        p.drawRoundedRect(0, 0, 30, 20, 4, 4)
        p.setBrush(QColor(self.pistonColor))
        p.drawRoundedRect(5, 5, 25, 10, 4, 4)

        p.end()
