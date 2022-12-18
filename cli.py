#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   cli.py
@Time    :   2022/11/05 15:51:31
@Author  :   Yuang Tong 
@Contact :   yuangtong1999@gmail.com
'''

# here put the import lib
from logic import make_empty_board,Game
import json
from log import MyLogger
import numpy as np

# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

def build_map_dct(dct_in):
    '''build a mapping dict from a map'''
    mapping = {}
    for key in dct_in.keys():
        int_pos = int(key)
        letter = dct_in[key]
        mapping[letter] = int_pos
    return mapping

def get_str_board():
    output_str = ""
    for i in range(3):
        output_str += "|"
        for j in range(3):
            output_str += " " + str(i*3+j) + " "
            output_str += "|"
        output_str += "\n"
    return output_str
def play_in_terminal():
    Logger = MyLogger()
    game = Game()
    name = None
    with open("./settings.json",'r') as rf: # load some settings
        settings = json.load(rf)
        rf.close()
    print(settings["Terminal"]["Welcome_Text"])
    map_dct = build_map_dct(settings["Terminal"]["Keys"])
    print('These keys represents the positions:')
    for key in map_dct.keys():
        print('{}-{}'.format(key,map_dct[key])) 
    print('Positions as follows:')
    print(get_str_board())
    mode = 0
    while(True):
        while(mode not in ["1","2"]):
            mode = input("Please select game mode to play, 1 for single player, 2 for multiple player: ")
        if mode == "1":
            name = input("Please input player name: ")
        while(game.checkwinner()==0):

            
            input_letter = None
            while(input_letter not in map_dct.keys()):
                if game.getchess()==1:
                    input_letter = input(("It's {}'s turn:").format(settings["Terminal"]["O_icon"])).upper()
                else:
                    input_letter = input(("It's {}'s turn:").format(settings["Terminal"]["X_icon"])).upper()
            pos = map_dct[input_letter]
            if game.put((pos//3,pos%3)):
                print(game.get_str_board(
                Circle_char=settings["Terminal"]["O_icon"],
                Cross_char=settings["Terminal"]["X_icon"]
                ))

            else:
                print('please try again with a valid position.')
                continue
            if mode=="1":
                if game.checkwinner()==0:
                    print('AI step:')
                    game.ai_random_step()
                    print(game.get_str_board(
                        Circle_char=settings["Terminal"]["O_icon"],
                        Cross_char=settings["Terminal"]["X_icon"]
                    ))


        if game.checkwinner()==1:
            print('Winner is O!')
        elif game.checkwinner()==-1:
            print('Winner is X!')
        elif game.checkwinner()==2:
            print('Draw!')
        mode = 0
        input_letter = None
        # record
        if mode=="1":
            Logger.put(name,game.checkwinner())
        
        top3_df = Logger.gettop3()
        names = list(top3_df["Name"])
        scores = list(np.asarray(top3_df["Win"]*3+np.asarray(top3_df["Draw"])))
        print('Rankings:')
        for i in range(3):
            print('Name:{},Score:{}'.format(names[i],scores[i]))
        
        while(input_letter not in ['Y','N']):
            input_letter = input("Play Again? Y/N:").upper()
        if input_letter=='N':
            print('Thank you for your playing.')
            break

        
        
    



if __name__ == '__main__':
    #board = make_empty_board()
    #winner = None
    #while winner == None:
        #print("TODO: take a turn!")
        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.
        #winner = 'X'  # FIXME
    play_in_terminal()