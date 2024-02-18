# -*- coding: utf-8 -*-
"""
Created on Wed May 25 23:59:27 2022

@author: rd3403
"""

def linear_congurence(xi):
    """Function to calculate linear congruence value and computer bet """   
    a = 22695477
    b=1
    m=2**32
    xi_plus_1 = (a*xi+b) %m
    if xi_plus_1 >= 2**31 :
        comp_move = 0
    else:
        comp_move = 1
    return comp_move, xi_plus_1


"""Function to test the input of difficulty that can only be 1 for an easy game or 2 for a difficult game"""
def input_diff_try(msg=''):
    while (True):
        y = (1,2)
        #input valdiation that provided integer can only be 1 or 2
        try:
            n = int(input(msg))
            if n in y:
                break
            else:
                print("Only difficulty 1 or 2 allowed. Please enter again")
                #Input validation so that type(input) can only be an integer
        except ValueError:
            print("Please only enter integers")
            pass
    return(n)

"""Function to test the input of moves, that have to be integers over 0"""
def input_move_try(msg=''):
    while (True):
        try:
            m = int(input(msg))
            if m > 0:
                break
            else:
                print("Amount of moves should be higher than 0")
                #Input validation so that type(input) can only be an integer
        except ValueError:
            print("Please only enter integers")
            pass
    return(m)

"""Function to test the input of a player, only integers (0,1) are allowed"""
def input_player_try(msg=''):
    while (True):
        x = (0,1)
        #input valdiation that provided integer can only be 0 or 1
        try:
            p = int(input(msg))
            if p in x:
                break
            else:
                print("Only number 0 or 1 allowed. Please enter again")
                #Input validation so that type(input) can only be an integer
        except ValueError:
            print("Please only enter integers")
            pass
    return(p)

"""Function to test the input whether player wants to stop a game (0) or start a new game (1)"""
def input_return_try(msg=''):
    while (True):
        z = (0,1)
        #input valdiation that provided integer can only be 0 or 1
        try:
            r = int(input(msg))
            if r in z:
                break
            else:
                print("To start a new game enter 1 or 0 to stop game")
                #Input validation so that type(input) can only be an integer
        except ValueError:
            print("Please only enter integers")
            pass
    return(r)
            



            