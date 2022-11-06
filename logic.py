#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   logic.py
@Time    :   2022/11/04 23:46:33
@Author  :   Yuang Tong 
@Contact :   yuangtong1999@gmail.com
'''

# here put the import lib
import numpy as np

def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]



class Game():
    def __init__(self):
        self.board = np.zeros((3,3))
        self.input_queue = []
        self.Chess = 1 # 1 for O and -1 for X
    def put(self,pos):
        x,y = pos
        if self.board[x][y] == 0:
            self.board[x][y] = self.Chess
            self.Chess = -self.Chess
            self.input_queue.append(pos)
            return True
        else:
            return False
    
    def get(self,pos): 
        x,y = pos
        return self.board[x][y]
    
    def back(self):
        if self.input_queue:
            (x,y) = self.input_queue.pop(-1)
            self.board[x][y] = 0
            self.Chess = -self.Chess
        return (x,y)
    def getwinner(self):
        # get the winner
        for i in range(3):
            if np.sum(self.board[i][:]) in [3,-3]:
                return self.board[i][0]
            if np.sum(self.board[:][i]) in [3,-3]:
                return self.board[0][i]
        
        if self.board[0][0]+self.board[1][1]+self.board[2][2] in [3,-3]:
            return self.board[0][0]
        if self.board[2][0]+self.board[1][1]+self.board[0][2] in [3,-3]:
            return self.board[2][0]
        return 0 if 0 in self.board else 2
    
    