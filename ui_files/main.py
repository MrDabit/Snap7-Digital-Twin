# --------------------------------------------------------------------------------------
# | Py module: main.py                                                                 |
# | Author: David García Rincón                                                        |
# | Date: 20210719                                                                     |
# | Version: 1.0 x64                                                                   |
# | Purpose: free software for testing and developing. Right working is not guarantied |
# --------------------------------------------------------------------------------------
# |                                        description                                 |
# --------------------------------------------------------------------------------------
# | This module is opening the ui form in #1                                           |
# | Generate the proccedure of the button read data in #2 calling the function readDB  |
# | included in module readDB.py mandatory                                             |
# --------------------------------------------------------------------------------------


import sys
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtUiTools import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from snap7.types import S7WLBit
from py_toggle import PyToggle
from py_widgets import PyFeeder, pyPneuCylinder
import PLCcom
import ini
import webbrowser


# 1. Define classes of objects in UI


class Container:
    def __init__(self, x, y, pos, posini):
        self.x = x
        self.y = y
        self.pos = pos
        self.posini = posini


class Motor:
    def __init__(self, status, setSpeed, actSpeed, pos):
        self.status = status
        self.setSpeed = setSpeed
        self.actSpeed = actSpeed
        self.pos = pos


box = [Container(0, 0, 0, 0), Container(0, 0, 0, 0),
       Container(0, 0, 0, 0), Container(0, 0, 0, 0),
       Container(0, 0, 0, 0), Container(0, 0, 0, 0),
       Container(0, 0, 0, 0), Container(0, 0, 0, 0),
       Container(0, 0, 0, 0), Container(0, 0, 0, 0),
       Container(0, 0, 0, 0), Container(0, 0, 0, 0),
       Container(0, 0, 0, 0)]

# 2. Create objetcs in the UI
# 2.1 Boxes in conveyor
box[1] = Container(0, 0, 1, 1)
box[2] = Container(0, 50, 12, 12)
box[3] = Container(0, 100, 11, 11)
box[4] = Container(100, 100, 10, 10)
box[5] = Container(200, 100, 9, 9)
box[6] = Container(300, 100, 8, 8)
box[7] = Container(400, 100, 7, 7)
box[8] = Container(400, 50, 6, 6)
box[9] = Container(400, 0, 5, 5)
box[10] = Container(300, 0, 4, 4)
box[11] = Container(200, 0, 3, 3)
box[12] = Container(100, 0, 2, 2)

# 2.2 Main motor
mainMotor = Motor(0, 0, 20, 0)


class mainFormMachineIf():

    # 1. Declaration of the mainform and call functions

    def __init__(self):
        super(mainFormMachineIf, self).__init__()
        self.ui = QUiLoader().load(QFile("PackingMachine.ui"))

        # open plc connection.
        conectionResult = PLCcom.plc_connect()
        # PLCcom.plc_connect()
        if conectionResult == False:
            print("fallo conexión")
            self.ui.lblPLCcom.setStyleSheet(
                "QLabel{font-size: 18pt; background-color: red; color:white}")
            self.ui.lblPLCcom.setText("PLC offline.....")
        else:
            self.ui.lblPLCcom.setStyleSheet(
                "QLabel{font-size: 18pt; background-color: green; color:black}")
            self.ui.lblPLCcom.setText("PLC online.....")

        # Push buttons main screen actions#
        # General buttons
        self.ui.btnSuscribe.clicked.connect(
            self.suscribe)  # Suscribe button action

        # Main switch (toogle custom widget)

        self.ui.chkMainSwitch = PyToggle(
            active_color="#00ff00"
        )
        self.ui.vloMainSwitch.addWidget(
            self.ui.chkMainSwitch, Qt.AlignCenter, Qt.AlignCenter)

        self.ui.chkMainSwitch.stateChanged.connect(self.mainSwitchOn)

        # Control buttons
        self.ui.btnStart.pressed.connect(
            self.startButtonPressed)  # Start machine
        self.ui.btnStart.released.connect(self.startButtonReleased)
        self.ui.btnStop.pressed.connect(self.stopButtonPressed)  # Stop machine
        self.ui.btnStop.released.connect(self.stopButtonReleased)
        self.ui.btnEmergency.pressed.connect(
            self.emergencyButtonPressed)  # Emergency stop
        self.ui.btnEmergency.released.connect(self.emergencyButtonReleased)
        self.ui.btnReset.pressed.connect(
            self.resetButtonPressed)  # Reset error
        self.ui.btnReset.released.connect(self.resetButtonReleased)

        self.ui.btnTest.clicked.connect(self.test)

        # Widgests in main screen

        # feeder1
        self.ui.wdgFeeder1 = PyFeeder(0, 30, 15, False, False, False, 0)
        self.ui.vloFeeder1.addWidget(
            self.ui.wdgFeeder1)

        # feeder2
        self.ui.wdgFeeder2 = PyFeeder(0, 40, 15, False, False, False, 0)
        self.ui.vloFeeder2.addWidget(
            self.ui.wdgFeeder2)

        # Cylinder test
        self.ui.wdgCylinder1 = pyPneuCylinder(True, False, 0, False, False)
        self.ui.verticalLayoutTEST.addWidget(
            self.ui.wdgCylinder1)

# Functions

    def suscribe(self):
        webbrowser.open(
            'https://www.youtube.com/channel/UC3sAY9xuFHe3G2xUd1lSZSA?sub_confirmation=1')

    # Test, run machine test

    def moveBox(self, i):

        if i == 1:
            self.ui.lblBox1.setGeometry(
                QtCore.QRect(box[i].x, box[i].y, 50, 20))

        if i == 2:
            self.ui.lblBox2.setGeometry(
                QtCore.QRect(box[i].x, box[i].y, 50, 20))

        if i == 3:
            self.ui.lblBox3.setGeometry(
                QtCore.QRect(box[i].x, box[i].y, 50, 20))

        if i == 4:
            self.ui.lblBox4.setGeometry(
                QtCore.QRect(box[i].x, box[i].y, 50, 20))

        if i == 5:
            self.ui.lblBox5.setGeometry(
                QtCore.QRect(box[i].x, box[i].y, 50, 20))

        if i == 6:
            self.ui.lblBox6.setGeometry(
                QtCore.QRect(box[i].x, box[i].y, 50, 20))

        if i == 7:
            self.ui.lblBox7.setGeometry(
                QtCore.QRect(box[i].x, box[i].y, 50, 20))

        if i == 8:
            self.ui.lblBox8.setGeometry(
                QtCore.QRect(box[i].x, box[i].y, 50, 20))

        if i == 9:
            self.ui.lblBox9.setGeometry(
                QtCore.QRect(box[i].x, box[i].y, 50, 20))

        if i == 10:
            self.ui.lblBox10.setGeometry(
                QtCore.QRect(box[i].x, box[i].y, 50, 20))

        if i == 11:
            self.ui.lblBox11.setGeometry(
                QtCore.QRect(box[i].x, box[i].y, 50, 20))

        if i == 12:
            self.ui.lblBox12.setGeometry(
                QtCore.QRect(box[i].x, box[i].y, 50, 20))

    def test(self):
        # Movement of the main motor boxes carrousel motion
        # The lenght of the conveyor is 400.
        # Box[i] is in pos 1 to 5 it moves horizontal right
        # Box[i] is in pos 5 to 7 it moves vertical down
        # Box[i] is in pos 7 to 10 it moves horizontal left
        # Box[i] is in pos 10 to 12 it moves vertical up

        inc = 1 * mainMotor.actSpeed
        ipos = mainMotor.pos // 100
        if ipos == 12:
            mainMotor.pos = 0

        mainMotor.pos = mainMotor.pos+inc

        print(f'posmotor {mainMotor.pos} ipos {ipos}')

        for i in range(1, 13, 1):
            box[i].pos = box[i].posini+(ipos)
            if box[i].pos >= 13:
                box[i].pos = box[i].pos-12

            posi = box[i].pos

            if posi >= 1 and posi < 5:
                box[i].x = box[i].x + 1*inc
                box[i].y = 0
            if posi >= 5 and posi < 7:
                box[i].x = 400
                box[i].y = box[i].y + 0.5*inc
            if posi >= 7 and posi < 11:
                box[i].x = box[i].x - 1*inc
                box[i].y = 100
            if posi >= 11:
                box[i].x = 0
                box[i].y = box[i].y - 0.5*inc

            self.moveBox(i)
        # ---------------------------------------------

        # Print in lcd values of speed and pos.

        self.ui.lcdSpeed.setProperty("intValue", mainMotor.actSpeed)
        self.ui.lcdActPos.setProperty("intValue", mainMotor.pos)
        self.ui.lcdIpos.setProperty("intValue", ipos)

    def mainSwitchOn(self):
        machineStatus = self.ui.chkMainSwitch.checkState()

        if machineStatus == 2:  # 2 means checked
            print(f"machine Status: PowerOn")
            ini.Ini()

# Action function of the Buttons

    def startButtonPressed(self):

        print("startPressed")
        PLCcom.writeDBbit(1, 0, 0, True)

    def startButtonReleased(self):
        print("startReleased")
        PLCcom.writeDBbit(1, 0, 0, False)

    def stopButtonPressed(self):
        print("stopPressed")
        PLCcom.writeDBbit(1, 0, 1, False)

    def stopButtonReleased(self):
        print("stopReleassed")
        PLCcom.writeDBbit(1, 0, 1, True)

    def emergencyButtonPressed(self):
        print("emergencyPressed")
        PLCcom.writeDBbit(1, 0, 2, False)

    def emergencyButtonReleased(self):
        print("emergencyPressed")
        PLCcom.writeDBbit(1, 0, 2, True)

    def resetButtonPressed(self):
        print("resetPressed")
        PLCcom.writeDBbit(1, 0, 3, True)

    def resetButtonReleased(self):
        print("resetReleased")
        PLCcom.writeDBbit(1, 0, 3, False)

    # PARTE DEDICADA  A LA LECTURA DEL DB EN SIEMENS

    def read(self):
        # 2.0 get data by running readDB function in readDB.py
        readDB.readDB()
        datos = readDB.readDB()
        cpuType = datos[0]
        cpuStatus = datos[1]
        name = datos[2]
        value = datos[3]
        status = datos[4]

        # 2.1 CPU data
        self.ui.txtCpuType.setText("{}".format(cpuType))

        if cpuStatus == 'S7CpuStatusRun':
            self.ui.ledCpuStatus.setStyleSheet(
                u"background-color: rgb(0, 255, 0);border-radius:15px;")
        else:
            self.ui.ledCpuStatus.setStyleSheet(
                u"background-color: rgb(255, 0, 0);border-radius:15px;")

        # 2.2 DB data
        self.ui.txtName.setText("{}".format(name))
        self.ui.lcdValue.setProperty("intValue", value)
        if status == True:
            self.ui.ledStatus.setStyleSheet(
                u"background-color: rgb(0, 255, 0);border-radius:30px;")
        else:
            self.ui.ledStatus.setStyleSheet(
                u"background-color: rgb(255, 0, 0);border-radius:30px;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = mainFormMachineIf()
    myapp.ui.show()
    sys.exit(app.exec_())
