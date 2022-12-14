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
from log import MyLogger

def make_empty_board():
    return np.zeros((3,3))



class Game():
    '''The game class'''
    def __init__(self):
        self.board = np.zeros((3,3))
        self.input_queue = []
        self.chess = 1 # 1 for O and -1 for X
        self.winner = 0
        self.Logger = MyLogger()
        self.player = None
    
    def ai_random_step(self):
        '''ai takes a random step'''
        # make a step from ai
        pos = np.asarray(np.where(self.board==0)).T
        # random guss
        np.random.shuffle(pos)
        if len(pos)>0:
            self.put(pos[0])
            return pos[0]
        return None
    
    def ai_step(self):
        '''TODO: Use some algorithm to calculate the best step'''
        pass
        
    def getchess(self):
        '''Get the current chess to put'''
        return self.chess

    def put(self,pos):
        '''
        Put one chess at pos, return True if put successfully
        '''
        if self.winner == 0:
            x,y = pos
            if self.get(pos) == 0: # if no
                self.board[x][y] = self.chess
                self.chess = -self.chess
                self.input_queue.append(pos)
                return True
            else:
                return False
    
    def get(self,pos): 
        '''
        get the chess at the position
        '''
        x,y = pos
        return self.board[x][y]
    
    def back(self):
        '''
        One step backward
        '''
        if self.input_queue:
            (x,y) = self.input_queue.pop(-1)
            self.board[x][y] = 0
            self.chess = -self.chess
            self.winner = 0
            return (x,y)
        else:
            return (-1,-1)

    def checkwinner(self):
        '''
        Check the winner:
        0: not finished yet
        1: O wins
        -1: X wins
        2: Draw
        
        should also change the self.winner value
        '''
        if self.winner == 0:
            for i in range(3):
                if np.sum(self.board[i,:]) in [3,-3]:
                    self.winner = self.board[i][0]
                    return self.winner
                if np.sum(self.board[:,i]) in [3,-3]:
                    self.winner = self.board[0][i]
                    return self.winner
            if self.board[0][0]+self.board[1][1]+self.board[2][2] in [3,-3]:
                self.winner = self.board[0][0]
                return self.winner
            if self.board[2][0]+self.board[1][1]+self.board[0][2] in [3,-3]:
                self.winner = self.board[2][0]
                return self.winner
            
            if 0 not in self.board:
                self.winner = 2
                return self.winner
            
        return self.winner

    def restart(self):
        '''
        Restart the game
        '''
        self.board = np.zeros((3,3))
        self.input_queue = []
        self.chess = 1 
        self.winner = 0
        
    def get_str_board(self,Circle_char,Cross_char):
        output_str = ""
        for i in range(3):
            output_str += "|"
            for j in range(3):
                output_str += " " 
                
                if self.get((i,j)) == 0:
                    nxt = " "
                elif self.get((i,j)) == 1:
                    nxt = Circle_char
                else:
                    nxt = Cross_char
                output_str += nxt
                output_str += " |"
            output_str += "\n"
        return output_str
    
    