# --------------------------------------------------------------------------------------
# | Py module: py_feeder.py                                                            |
# | Author: David García Rincón                                                        |
# | Date: 20211125                                                                     |
# | Version: 1.0 x64                                                                   |
# | Purpose: free software for testing and developing. Right working is not guarantied |
# --------------------------------------------------------------------------------------
# |                                        description                                 |
# --------------------------------------------------------------------------------------
# | Custom QTwidget                                                                    |
# | Definition of a feeder with conveyor, stop cilinder, retain cilinder,              |
# | quantity,cylinder positions                                                        |
# --------------------------------------------------------------------------------------

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class PyFeeder(QWidget):
    def __init__(self, status, quantity, minimum, run, protection, onError, actRunTime):
        super(PyFeeder, self).__init__()
        self.status = status  # 0 iddle, 1 ready, 2 run, 3 fault
        self.quantity = quantity
        self.minimum = minimum
        self.run = run
        self.protection = protection  # False = OK, True=Triggered
        self.onError = onError
        self.actRunTime = actRunTime
        self.initUI()
        self.counterColor()
        self.protectionAppareance()

    def initUI(self):  # create widgets
        # create quantity display
        self.lcdQuantity = QLCDNumber(self)
        self.lcdQuantity.setObjectName(u"lcdQuantity")
        self.lcdQuantity.setProperty("maximumHeight", 20)
        self.lcdQuantity.setProperty("maximumWidth", 100)
        self.lcdQuantity.setGeometry(0, 40, 80, 20)
        self.lcdQuantity.setProperty("intValue", self.quantity)
    # create fill button (50 pieces)
        btnFill = QPushButton(self)
        btnFill.setGeometry(QRect(0, 0, 80, 20))
        btnFill.setText("FILL")
        btnFill.pressed.connect(lambda: self.fillFeeder(50))
    # create substract button
        btnSubstract = QPushButton(self)
        btnSubstract.setGeometry(QRect(0, 20, 40, 20))
        btnSubstract.setText("-")
        btnSubstract.pressed.connect(lambda: self.substractPiece())

    # create add button
        btnAdd = QPushButton(self)
        btnAdd.setGeometry(QRect(40, 20, 40, 20))
        btnAdd.setText("+")
        btnAdd.pressed.connect(lambda: self.addPiece())

    # create protection restore switch
        self.btnProtection = QPushButton(self)
        self.btnProtection.setGeometry(QRect(0, 60, 80, 20))
        self.btnProtection.pressed.connect(
            lambda: self.protectionSwitch())

    # create status label
        self.lblStatus = QLabel(self)
        self.lblStatus.setGeometry(QRect(0, 80, 80, 20))
        self.lblStatus.setText(f"status: {self.status}")


# Simulation actions, actions made by the operator.


    def fillFeeder(self, pieces):
        print("Filling feeder with pieces")
        self.quantity += pieces
        self.lcdQuantity.setProperty("intValue", self.quantity)
        self.counterColor()

    def substractPiece(self):
        print("substract piece in feeder")
        if self.quantity > 0:
            self.quantity -= 1
        self.lcdQuantity.setProperty("intValue", self.quantity)
        self.counterColor()

    def addPiece(self):
        print("add piece in feeder")
        self.quantity += 1
        self.lcdQuantity.setProperty("intValue", self.quantity)
        self.counterColor()


# Automation actions, actions made by the PLC


    def activate(self):
        if self.onError == False:
            self.run = True
            self.status = 2
            self.statusLabel()

    def deactivate(self):
        self.run = False
        if self.status == 2:
            self.status = 1

    def protectionSwitch(self):
        if self.protection == True:
            self.protectionRestored()
        else:
            self.protectionTriggered()

    def protectionTriggered(self):
        self.run = False
        self.protection = True
        self.status = 3
        self.statusLabel()
        self.protectionAppareance()

    def protectionRestored(self):
        self.protection = False
        self.status = 1
        self.statusLabel()
        self.protectionAppareance()

    def generalError(self):
        self.run = False
        self.status = 3
        self.statusLabel()

    def reset(self):
        self.status = 1
        self.onError = False
        self.run = False
        self.protectionRestored()
        self.statusLabel()

# Widgets animation
    def counterColor(self):
        # animate color of LCD counter quantity
        if self.quantity < self.minimum:
            self.lcdQuantity.setStyleSheet(
                "QLCDNumber{font-size: 18pt; background-color: red; color:white}")
        else:
            self.lcdQuantity.setStyleSheet(
                "QLCDNumber{font-size: 18pt; background-color: green; color:white}")

    def protectionAppareance(self):
        if self.protection == True:
            self.btnProtection.setText("TRIG")
            self.btnProtection.setStyleSheet(
                "QPushButton{font-size: 12pt; background-color: red; color:white}")
        else:
            self.btnProtection.setText("OK")
            self.btnProtection.setStyleSheet(
                "QPushButton{font-size: 12pt; background-color: green; color:black}")

    def statusLabel(self):
        self.lblStatus.setText(f"status: {self.status}")
        if self.status == 0:
            self.lblStatus.setStyleSheet(
                "QLabel{font-size: 12pt; background-color: grey; color:black}")
        if self.status == 1:
            self.lblStatus.setStyleSheet(
                "QLabel{font-size: 12pt; background-color: blue; color:white}")
        if self.status == 2:
            self.lblStatus.setStyleSheet(
                "QLabel{font-size: 12pt; background-color: green; color:white}")
        if self.status == 3:
            self.lblStatus.setStyleSheet(
                "QLabel{font-size: 12pt; background-color: red; color:white}")
