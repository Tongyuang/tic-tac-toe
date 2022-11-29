#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   func_main.py
@Time    :   2022/11/29 10:39:07
@Author  :   Yuang Tong 
@Contact :   yuangtong1999@gmail.com
'''

# here put the import lib


import json
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSignalMapper

import NameInputMain
from log import MyLogger
from logic import Game, make_empty_board
from Ui_main import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    '''
    The mainWindow class
    '''
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        
    def setup(self,MainWindow):
        '''Setup Mainwindow'''
        with open("./settings.json",'r') as rf: # load some settings
            self.settings = json.load(rf)
            rf.close()
        self.cross_icon = QtGui.QIcon(self.settings["crosslogo"])
        self.circle_icon = QtGui.QIcon(self.settings["circlelogo"])
        self.iconsize = QtCore.QSize(90,90)
        self.setupUi(MainWindow)
        self.Logger = MyLogger()
        
        '''
        set all the button not enabled at the beginning, also set Ids
        '''
        for i,button in enumerate(self.buttonGroup.buttons()):
            button.clicked.connect(partial(self.buttonclicked,i))
            self.buttonGroup.setId(button,i)
            button.setEnabled(False)
            
        '''some trigger functions and slot connections'''
        self.actionRestart.triggered.connect(self.restart_slot)
        self.actionRevoke.triggered.connect(self.revoke_slot)
        
        self.actionPvsP.triggered.connect(self.pvp_slot)
        self.actionPvB.triggered.connect(self.pvb_slot)
        self.settext(self.settings["starttext"])
        self.mode = 1 # playing mode, 1 for pvp and 0 for ai
        
        self.game = Game()
        # subwindows
        self.inputwindow = NameInputMain.NameInputMain()
        self.inputwindow._sgnal.connect(self.setplayername)
        self.inputwindow.setModal(True)
        
        self.playername = None
    def settext(self,text):
        '''
        use the label to set text
        '''
        self.label_2.setText(text)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
    def seticon(self,button_idx,icon):
        '''set icon'''
        self.buttonGroup.button(button_idx).setIcon(icon)
        self.buttonGroup.button(button_idx).setIconSize(self.iconsize)
    
    def clearicon(self,button_idx):
        '''Clear icon'''
        self.buttonGroup.button(button_idx).setIcon(QtGui.QIcon())
    # some SLOT functions
    def showtext(self):
        '''show the winner's status or who's turn'''
        winner = self.game.checkwinner()
        if winner == 2:
            self.settext(self.settings["drawtext"])
        elif winner == 1:
            self.settext(self.settings["circlewintext"])
        elif winner == -1:
            self.settext(self.settings["crosswintext"])
        else:
            self.settext("Now it's {}'s turn".format("O" if self.game.getchess()==1 else "X"))
    def buttonclicked(self,i):
        '''main button slot functions'''
        pos = (i//3,i%3)
        chess = self.game.getchess()
        if self.game.put(pos):
            chess_icon = self.circle_icon if chess==1 else self.cross_icon
            self.seticon(i,chess_icon)
            self.showtext()
            if self.mode==0 and self.game.winner==0:# pvb
                chess = self.game.getchess()
                ai_pos = self.game.ai_random_step()
                chess_icon = self.circle_icon if chess==1 else self.cross_icon
                self.seticon((ai_pos[0]*3+ai_pos[1]),chess_icon)
                self.showtext()
    def restart_slot(self):
        '''how to restart'''
        self.game.restart()      
        # clear all icons
        for i in range(len(self.buttonGroup.buttons())):
            self.clearicon(i)
            self.buttonGroup.button(i).setEnabled(False)
        self.settext(self.settings["starttext"])
    
    def revoke_slot(self):
        '''one step back'''
        pos = self.game.back()
        if pos[0]>-1:
            idx = pos[0]*3+pos[1]
            self.clearicon(idx)
            self.settext("Now it's {}'s turn".format("O" if self.game.getchess()==1 else "X"))
    
    def pvp_slot(self):
        '''human vs human'''
        self.restart_slot()
        self.mode = 1
        for i,button in enumerate(self.buttonGroup.buttons()):
            button.setEnabled(True)
        self.settext(self.settings["pvptext"])
            
    def pvb_slot(self):
        '''human vs robot'''
        #
        self.inputwindow.show()
        self.restart_slot()
        self.mode = 0
        for i,button in enumerate(self.buttonGroup.buttons()):
            button.setEnabled(True)
        self.settext(self.settings["pvbtext"])
    
    def setplayername(self,name):
        self.playername = name
    
        