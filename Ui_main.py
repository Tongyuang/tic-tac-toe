# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/tongyuang/study/UWGIX/Course/TECHIN 509/Practice/Week-5/tic-tac-toe/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 532)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1_1.setGeometry(QtCore.QRect(21, 110, 120, 120))
        self.Button1_1.setAutoFillBackground(True)
        self.Button1_1.setText("")
        self.Button1_1.setCheckable(False)
        self.Button1_1.setObjectName("Button1_1")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.Button1_1)
        self.Button1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1_2.setGeometry(QtCore.QRect(141, 110, 120, 120))
        self.Button1_2.setAutoFillBackground(True)
        self.Button1_2.setText("")
        self.Button1_2.setCheckable(False)
        self.Button1_2.setObjectName("Button1_2")
        self.buttonGroup.addButton(self.Button1_2)
        self.Button1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1_3.setGeometry(QtCore.QRect(261, 110, 120, 120))
        self.Button1_3.setAutoFillBackground(True)
        self.Button1_3.setText("")
        self.Button1_3.setCheckable(False)
        self.Button1_3.setObjectName("Button1_3")
        self.buttonGroup.addButton(self.Button1_3)
        self.Button2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2_1.setGeometry(QtCore.QRect(21, 230, 120, 120))
        self.Button2_1.setAutoFillBackground(True)
        self.Button2_1.setText("")
        self.Button2_1.setCheckable(False)
        self.Button2_1.setObjectName("Button2_1")
        self.buttonGroup.addButton(self.Button2_1)
        self.Button2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2_2.setGeometry(QtCore.QRect(141, 230, 120, 120))
        self.Button2_2.setAutoFillBackground(True)
        self.Button2_2.setText("")
        self.Button2_2.setCheckable(False)
        self.Button2_2.setObjectName("Button2_2")
        self.buttonGroup.addButton(self.Button2_2)
        self.Button2_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2_3.setGeometry(QtCore.QRect(261, 230, 120, 120))
        self.Button2_3.setAutoFillBackground(True)
        self.Button2_3.setText("")
        self.Button2_3.setCheckable(False)
        self.Button2_3.setObjectName("Button2_3")
        self.buttonGroup.addButton(self.Button2_3)
        self.Button3_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3_1.setGeometry(QtCore.QRect(21, 350, 120, 120))
        self.Button3_1.setAutoFillBackground(True)
        self.Button3_1.setText("")
        self.Button3_1.setCheckable(False)
        self.Button3_1.setObjectName("Button3_1")
        self.buttonGroup.addButton(self.Button3_1)
        self.Button3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3_2.setGeometry(QtCore.QRect(141, 350, 120, 120))
        self.Button3_2.setAutoFillBackground(True)
        self.Button3_2.setText("")
        self.Button3_2.setCheckable(False)
        self.Button3_2.setObjectName("Button3_2")
        self.buttonGroup.addButton(self.Button3_2)
        self.Button3_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3_3.setGeometry(QtCore.QRect(261, 350, 120, 120))
        self.Button3_3.setAutoFillBackground(True)
        self.Button3_3.setText("")
        self.Button3_3.setCheckable(False)
        self.Button3_3.setObjectName("Button3_3")
        self.buttonGroup.addButton(self.Button3_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(21, 350, 360, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(140, 110, 2, 360))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(260, 110, 2, 360))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 211, 30))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 201, 30))
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(20, 230, 360, 2))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 10, 131, 20))
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_Player1 = QtWidgets.QLabel(self.centralwidget)
        self.label_Player1.setGeometry(QtCore.QRect(260, 30, 131, 20))
        self.label_Player1.setTextFormat(QtCore.Qt.PlainText)
        self.label_Player1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Player1.setObjectName("label_Player1")
        self.label_Player2 = QtWidgets.QLabel(self.centralwidget)
        self.label_Player2.setGeometry(QtCore.QRect(260, 50, 131, 20))
        self.label_Player2.setTextFormat(QtCore.Qt.PlainText)
        self.label_Player2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Player2.setObjectName("label_Player2")
        self.label_Player3 = QtWidgets.QLabel(self.centralwidget)
        self.label_Player3.setGeometry(QtCore.QRect(260, 70, 131, 20))
        self.label_Player3.setTextFormat(QtCore.Qt.PlainText)
        self.label_Player3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Player3.setObjectName("label_Player3")
        self.label_Nowplaying = QtWidgets.QLabel(self.centralwidget)
        self.label_Nowplaying.setGeometry(QtCore.QRect(20, 80, 131, 20))
        self.label_Nowplaying.setTextFormat(QtCore.Qt.PlainText)
        self.label_Nowplaying.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Nowplaying.setObjectName("label_Nowplaying")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuNewGame = QtWidgets.QMenu(self.menuMain)
        self.menuNewGame.setObjectName("menuNewGame")
        MainWindow.setMenuBar(self.menubar)
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.actionRevoke = QtWidgets.QAction(MainWindow)
        self.actionRevoke.setObjectName("actionRevoke")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionPvP = QtWidgets.QAction(MainWindow)
        self.actionPvP.setObjectName("actionPvP")
        self.actionPvP_2 = QtWidgets.QAction(MainWindow)
        self.actionPvP_2.setObjectName("actionPvP_2")
        self.actionPvB = QtWidgets.QAction(MainWindow)
        self.actionPvB.setObjectName("actionPvB")
        self.actionPvsP = QtWidgets.QAction(MainWindow)
        self.actionPvsP.setObjectName("actionPvsP")
        self.menuNewGame.addSeparator()
        self.menuNewGame.addAction(self.actionPvB)
        self.menuNewGame.addAction(self.actionPvsP)
        self.menuMain.addAction(self.actionRestart)
        self.menuMain.addAction(self.actionRevoke)
        self.menuMain.addAction(self.actionExit_2)
        self.menuMain.addAction(self.menuNewGame.menuAction())
        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe"))
        self.label.setText(_translate("MainWindow", "Welcome to Yuang\'s Tic Tac Toe!"))
        self.label_3.setText(_translate("MainWindow", "World Ranking:"))
        self.label_Player1.setText(_translate("MainWindow", "Player1 x/x/x"))
        self.label_Player2.setText(_translate("MainWindow", "Player2 x/x/x"))
        self.label_Player3.setText(_translate("MainWindow", "Player3 x/x/x"))
        self.label_Nowplaying.setText(_translate("MainWindow", "Now Playing: Player1"))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.menuNewGame.setTitle(_translate("MainWindow", "NewGame"))
        self.actionRestart.setText(_translate("MainWindow", "Restart"))
        self.actionRevoke.setText(_translate("MainWindow", "Revoke"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionPvP.setText(_translate("MainWindow", "PvP"))
        self.actionPvP_2.setText(_translate("MainWindow", "PvP"))
        self.actionPvB.setText(_translate("MainWindow", "PvB"))
        self.actionPvsP.setText(_translate("MainWindow", "PvP"))
