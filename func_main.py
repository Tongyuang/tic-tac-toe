#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   func_main.py
@Time    :   2022/11/04 23:46:21
@Author  :   Yuang Tong 
@Contact :   yuangtong1999@gmail.com
'''

# here put the import lib


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSignalMapper
from Ui_main import Ui_MainWindow
from logic import Game,make_empty_board
from functools import partial
import json

class MainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        
    def setup(self,MainWindow):
        with open("./settings.json",'r') as rf:
            self.settings = json.load(rf)
            rf.close()
        self.cross_icon = QtGui.QIcon(self.settings["crosslogo"])
        self.circle_icon = QtGui.QIcon(self.settings["circlelogo"])
        self.iconsize = QtCore.QSize(90,90)
        self.setupUi(MainWindow)
        self.settext(self.settings["starttext"])
        for i,button in enumerate(self.buttonGroup.buttons()):
            button.clicked.connect(partial(self.buttonclicked,i))
            self.buttonGroup.setId(button,i)
        
        self.actionRestart.triggered.connect(self.restart_slot)
        self.actionRevoke.triggered.connect(self.revoke_slot)
        self.game = Game()

    def settext(self,text):
        self.label_2.setText(text)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
    def seticon(self,button_idx,icon):
        self.buttonGroup.button(button_idx).setIcon(icon)
        self.buttonGroup.button(button_idx).setIconSize(self.iconsize)
    
    def clearicon(self,button_idx):
        self.buttonGroup.button(button_idx).setIcon(QtGui.QIcon())
    # some SLOT functions
    def buttonclicked(self,i):
        # 
        #print(self.game.board)
        pos = (i//3,i%3)
        chess = self.game.getchess()
        if self.game.put(pos):
            chess_icon = self.circle_icon if chess==1 else self.cross_icon
            self.seticon(i,chess_icon)
            winner = self.game.checkwinner()
            if winner == 2:
                self.settext(self.settings["drawtext"])
            elif winner == 1:
                self.settext(self.settings["circlewintext"])
            elif winner == -1:
                self.settext(self.settings["crosswintext"])
            else:
                self.settext("Now it's {}'s turn".format("O" if self.game.getchess()==1 else "X"))
    
    def restart_slot(self):
        self.game.restart()      
        # clear all icons
        for i in range(len(self.buttonGroup.buttons())):
            self.clearicon(i)
        self.settext(self.settings["starttext"])
    
    def revoke_slot(self):
        pos = self.game.back()
        if pos[0]>-1:
            idx = pos[0]*3+pos[1]
            self.clearicon(idx)
            self.settext("Now it's {}'s turn".format("O" if self.game.getchess()==1 else "X"))