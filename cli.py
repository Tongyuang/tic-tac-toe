#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   cli.py
@Time    :   2022/11/05 15:51:31
@Author  :   Yuang Tong 
@Contact :   yuangtong1999@gmail.com
'''

# here put the import lib
from logic import make_empty_board
# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.




if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.
        winner = 'X'  # FIXME