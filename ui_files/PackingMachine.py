# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'PackingMachine.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1064, 960)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.frmControlInterface = QFrame(self.centralwidget)
        self.frmControlInterface.setObjectName(u"frmControlInterface")
        self.frmControlInterface.setGeometry(QRect(10, 10, 941, 161))
        self.frmControlInterface.setFrameShape(QFrame.StyledPanel)
        self.frmControlInterface.setFrameShadow(QFrame.Raised)
        self.frmButtons = QFrame(self.frmControlInterface)
        self.frmButtons.setObjectName(u"frmButtons")
        self.frmButtons.setGeometry(QRect(10, 10, 231, 141))
        self.frmButtons.setFrameShape(QFrame.StyledPanel)
        self.frmButtons.setFrameShadow(QFrame.Raised)
        self.btnStart = QPushButton(self.frmButtons)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(10, 10, 75, 61))
        self.btnStop = QPushButton(self.frmButtons)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setGeometry(QRect(10, 70, 75, 61))
        self.btnEmergency = QPushButton(self.frmButtons)
        self.btnEmergency.setObjectName(u"btnEmergency")
        self.btnEmergency.setGeometry(QRect(120, 10, 75, 61))
        self.btnReset = QPushButton(self.frmButtons)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setGeometry(QRect(120, 70, 75, 61))
        self.frmDisplays = QFrame(self.frmControlInterface)
        self.frmDisplays.setObjectName(u"frmDisplays")
        self.frmDisplays.setGeometry(QRect(249, 9, 181, 141))
        self.frmDisplays.setFrameShape(QFrame.StyledPanel)
        self.frmDisplays.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frmDisplays)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 52, 101))
        self.vloLbldisplay = QVBoxLayout(self.layoutWidget)
        self.vloLbldisplay.setObjectName(u"vloLbldisplay")
        self.vloLbldisplay.setContentsMargins(0, 0, 0, 0)
        self.lblSpeed = QLabel(self.layoutWidget)
        self.lblSpeed.setObjectName(u"lblSpeed")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblSpeed.setFont(font)
        self.lblSpeed.setLayoutDirection(Qt.LeftToRight)
        self.lblSpeed.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.vloLbldisplay.addWidget(self.lblSpeed)

        self.lblActPos = QLabel(self.layoutWidget)
        self.lblActPos.setObjectName(u"lblActPos")
        self.lblActPos.setFont(font)
        self.lblActPos.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.vloLbldisplay.addWidget(self.lblActPos)

        self.lblIpos = QLabel(self.layoutWidget)
        self.lblIpos.setObjectName(u"lblIpos")
        self.lblIpos.setFont(font)
        self.lblIpos.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.vloLbldisplay.addWidget(self.lblIpos)

        self.layoutWidget1 = QWidget(self.frmDisplays)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(90, 20, 66, 101))
        self.vloLcdDisplay = QVBoxLayout(self.layoutWidget1)
        self.vloLcdDisplay.setObjectName(u"vloLcdDisplay")
        self.vloLcdDisplay.setContentsMargins(0, 0, 0, 0)
        self.lcdSpeed = QLCDNumber(self.layoutWidget1)
        self.lcdSpeed.setObjectName(u"lcdSpeed")

        self.vloLcdDisplay.addWidget(self.lcdSpeed)

        self.lcdActPos = QLCDNumber(self.layoutWidget1)
        self.lcdActPos.setObjectName(u"lcdActPos")

        self.vloLcdDisplay.addWidget(self.lcdActPos)

        self.lcdIpos = QLCDNumber(self.layoutWidget1)
        self.lcdIpos.setObjectName(u"lcdIpos")

        self.vloLcdDisplay.addWidget(self.lcdIpos)

        self.frmMainSwitch = QFrame(self.frmControlInterface)
        self.frmMainSwitch.setObjectName(u"frmMainSwitch")
        self.frmMainSwitch.setGeometry(QRect(780, 0, 151, 151))
        self.frmMainSwitch.setFrameShape(QFrame.StyledPanel)
        self.frmMainSwitch.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frmMainSwitch)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 131, 121))
        self.vloMainSwitch = QVBoxLayout(self.verticalLayoutWidget)
        self.vloMainSwitch.setObjectName(u"vloMainSwitch")
        self.vloMainSwitch.setContentsMargins(0, 0, 0, 0)
        self.frmMachineInterface = QFrame(self.centralwidget)
        self.frmMachineInterface.setObjectName(u"frmMachineInterface")
        self.frmMachineInterface.setGeometry(QRect(10, 180, 661, 531))
        self.frmMachineInterface.setFrameShape(QFrame.StyledPanel)
        self.frmMachineInterface.setFrameShadow(QFrame.Raised)
        self.frmConveyor = QFrame(self.frmMachineInterface)
        self.frmConveyor.setObjectName(u"frmConveyor")
        self.frmConveyor.setGeometry(QRect(20, 150, 450, 150))
        self.frmConveyor.setFrameShape(QFrame.StyledPanel)
        self.frmConveyor.setFrameShadow(QFrame.Raised)
        self.lblImgConveyor = QLabel(self.frmConveyor)
        self.lblImgConveyor.setObjectName(u"lblImgConveyor")
        self.lblImgConveyor.setGeometry(QRect(0, 25, 400, 50))
        self.lblImgConveyor.setPixmap(QPixmap(u"images/logo A&R.svg"))
        self.lblImgConveyor.setScaledContents(True)
        self.lblBox1 = QLabel(self.frmConveyor)
        self.lblBox1.setObjectName(u"lblBox1")
        self.lblBox1.setGeometry(QRect(0, 0, 47, 20))
        self.lblBox2 = QLabel(self.frmConveyor)
        self.lblBox2.setObjectName(u"lblBox2")
        self.lblBox2.setGeometry(QRect(0, 50, 47, 13))
        self.lblBox3 = QLabel(self.frmConveyor)
        self.lblBox3.setObjectName(u"lblBox3")
        self.lblBox3.setGeometry(QRect(0, 100, 47, 13))
        self.lblBox4 = QLabel(self.frmConveyor)
        self.lblBox4.setObjectName(u"lblBox4")
        self.lblBox4.setGeometry(QRect(100, 100, 47, 13))
        self.lblBox5 = QLabel(self.frmConveyor)
        self.lblBox5.setObjectName(u"lblBox5")
        self.lblBox5.setGeometry(QRect(200, 100, 47, 13))
        self.lblBox6 = QLabel(self.frmConveyor)
        self.lblBox6.setObjectName(u"lblBox6")
        self.lblBox6.setGeometry(QRect(300, 100, 47, 13))
        self.lblBox7 = QLabel(self.frmConveyor)
        self.lblBox7.setObjectName(u"lblBox7")
        self.lblBox7.setGeometry(QRect(400, 100, 47, 13))
        self.lblBox8 = QLabel(self.frmConveyor)
        self.lblBox8.setObjectName(u"lblBox8")
        self.lblBox8.setGeometry(QRect(400, 50, 47, 13))
        self.lblBox9 = QLabel(self.frmConveyor)
        self.lblBox9.setObjectName(u"lblBox9")
        self.lblBox9.setGeometry(QRect(400, 0, 47, 13))
        self.lblBox10 = QLabel(self.frmConveyor)
        self.lblBox10.setObjectName(u"lblBox10")
        self.lblBox10.setGeometry(QRect(300, 0, 47, 13))
        self.lblBox11 = QLabel(self.frmConveyor)
        self.lblBox11.setObjectName(u"lblBox11")
        self.lblBox11.setGeometry(QRect(200, 0, 47, 13))
        self.lblBox12 = QLabel(self.frmConveyor)
        self.lblBox12.setObjectName(u"lblBox12")
        self.lblBox12.setGeometry(QRect(100, 0, 47, 13))
        self.btnTest = QPushButton(self.frmMachineInterface)
        self.btnTest.setObjectName(u"btnTest")
        self.btnTest.setGeometry(QRect(510, 452, 75, 61))
        self.frmSettingsInterface = QFrame(self.centralwidget)
        self.frmSettingsInterface.setObjectName(u"frmSettingsInterface")
        self.frmSettingsInterface.setGeometry(QRect(680, 180, 271, 531))
        self.frmSettingsInterface.setFrameShape(QFrame.StyledPanel)
        self.frmSettingsInterface.setFrameShadow(QFrame.Raised)
        self.frmInfo = QFrame(self.centralwidget)
        self.frmInfo.setObjectName(u"frmInfo")
        self.frmInfo.setGeometry(QRect(10, 720, 940, 80))
        self.frmInfo.setFrameShape(QFrame.StyledPanel)
        self.frmInfo.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frmInfo)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 331, 41))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setTextFormat(Qt.RichText)
        self.label.setScaledContents(False)
        self.btnSuscribe = QPushButton(self.frmInfo)
        self.btnSuscribe.setObjectName(u"btnSuscribe")
        self.btnSuscribe.setGeometry(QRect(750, 0, 101, 75))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnSuscribe.sizePolicy().hasHeightForWidth())
        self.btnSuscribe.setSizePolicy(sizePolicy)
        self.btnSuscribe.setText(u"")
        icon = QIcon()
        icon.addFile(u"images/logo A&R.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSuscribe.setIcon(icon)
        self.btnSuscribe.setIconSize(QSize(150, 150))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1064, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.btnStart.setText(QCoreApplication.translate(
            "MainWindow", u"START", None))
        self.btnStop.setText(QCoreApplication.translate(
            "MainWindow", u"STOP", None))
        self.btnEmergency.setText(QCoreApplication.translate(
            "MainWindow", u"EMERGENCIA", None))
        self.btnReset.setText(QCoreApplication.translate(
            "MainWindow", u"RESET", None))
        self.lblSpeed.setText(QCoreApplication.translate(
            "MainWindow", u"SPEED:", None))
        self.lblActPos.setText(QCoreApplication.translate(
            "MainWindow", u"ACT POS:", None))
        self.lblIpos.setText(QCoreApplication.translate(
            "MainWindow", u"IPOS:", None))
        self.lblImgConveyor.setText("")
        self.lblBox1.setText(QCoreApplication.translate(
            "MainWindow", u"box1", None))
        self.lblBox2.setText(QCoreApplication.translate(
            "MainWindow", u"box2", None))
        self.lblBox3.setText(QCoreApplication.translate(
            "MainWindow", u"box3", None))
        self.lblBox4.setText(QCoreApplication.translate(
            "MainWindow", u"box4", None))
        self.lblBox5.setText(QCoreApplication.translate(
            "MainWindow", u"box5", None))
        self.lblBox6.setText(QCoreApplication.translate(
            "MainWindow", u"box6", None))
        self.lblBox7.setText(QCoreApplication.translate(
            "MainWindow", u"box7", None))
        self.lblBox8.setText(QCoreApplication.translate(
            "MainWindow", u"box8", None))
        self.lblBox9.setText(QCoreApplication.translate(
            "MainWindow", u"box9", None))
        self.lblBox10.setText(QCoreApplication.translate(
            "MainWindow", u"box10", None))
        self.lblBox11.setText(QCoreApplication.translate(
            "MainWindow", u"box11", None))
        self.lblBox12.setText(QCoreApplication.translate(
            "MainWindow", u"box12", None))
        self.btnTest.setText(QCoreApplication.translate(
            "MainWindow", u"test", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Modelo Virtual VS7WB_v1", None))
    # retranslateUi
