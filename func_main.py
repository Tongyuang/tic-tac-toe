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

class MainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
    
    def setup(self,MainWindow):
        self.setupUi(MainWindow)
        for i,button in enumerate(self.buttonGroup.buttons()):
            button.clicked.connect(partial(self.ButtonClicked,i))
            self.buttonGroup.setId(button,i)
        
        self.game = Game()

    def settext(self,text):
        self.textBrowser_2.setText(text)
    def ButtonClicked(self,i):
        # 
        # pos = (i//3,i%3)
        # if self.game.put(pos):
            
        #if self.game.put(pos)
        #pass
        self.buttonGroup.button(i).setText('{}'.format(i))
    #def setupConnection(self):
        #self.Button1_1.clicked.connect(self.)

    #def setupGame(self):
    #    self.Game = logic.Game()
    
        
    #def setupSlot(self):
    #    self.Button1_1_clicked_slot = 