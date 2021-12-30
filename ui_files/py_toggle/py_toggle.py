# --------------------------------------------------------------------------------------
# | Py module: py_toggle.py                                                            |
# | Author: David García Rincón                                                        |
# | Date: 20211124                                                                     |
# | Version: 1.0 x64                                                                   |
# | Purpose: free software for testing and developing. Right working is not guarantied |
# --------------------------------------------------------------------------------------
# |                                        description                                 |
# --------------------------------------------------------------------------------------
# | Custom QTwidget based on checkbox of QTdesigner                                    |
# | Used as toggle button for on/off purposes                                          |
# | Credit to: Wanderson M.Pimenta                                                     |
# --------------------------------------------------------------------------------------

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class PyToggle(QCheckBox):
    def __init__(
        self,
        width=60,
        bg_color="#777",
        circle_color="#DDD",
        active_color="#00BCff",
        animation_curve=QEasingCurve.OutBounce
    ):
        QCheckBox.__init__(self)

        # set default parameters
        self.setFixedSize(width, 28)
        self.setCursor(Qt.PointingHandCursor)

        # colors
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        # create animation
        self._circle_position = 3
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)  # Time in miliseconds

        # conect state changed
        self.stateChanged.connect(self.start_transition)

    # create new set and get property
    @Property(float)  # get
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()

    def start_transition(self, value):
        self.animation.stop()  # stop animation if running
        if value:
            self.animation.setEndValue(self.width()-26)
        else:
            self.animation.setEndValue(3)

        # start anmiation
        self.animation.start()

        print(f"status: {self.isChecked()}")

    # set new hit area
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

# draw new items
    def paintEvent(self, e):
        # set painter
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        # set as no pen
        p.setPen(Qt.NoPen)

        # draw rectangle
        rect = QRect(0, 0, self.width(), self.height())

        # check if is checked
        if not self.isChecked():
            # draw BG
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(),
                              self.height()/2, 14)

            # draw circle
            p.setBrush(QColor(self._circle_color))
            p.dr0awEllipse(self._circle_position, 3, 22, 22)
        else:
            # draw BG
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(),
                              self.height()/2, 14)

            # draw circle
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 3, 22, 22)
        # end draw
        p.end()
