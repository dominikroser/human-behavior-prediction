# -*- coding: utf-8 -*-
"""import auxilary functions to ensure calculation of computer_move and correct input of player"""

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

"""Main function of game that allows to restart game and counts winner per round and game"""
def game():
    # opening message
    print('Welcome to Human Behavior Prediction by Dominik Roser')
    Total_player_wins = []
    Total_computer_wins = []
 
    def main(): 
        """Game setting is decided, if the difficulty and the number of moves""" 
        select_difficulty = input_diff_try("Please choose the type of game (1:Easy, 2:Difficult):")
        level_difficulty = 'Easy Game'if select_difficulty ==1 else 'Difficult game'
        #Choose the number of moves
        moves =  input_move_try("Enter the number of moves:  ")
        
        """All variables are put in there initial state at the beginning of each game"""
        throw00, throw01, throw10, throw11 = 0, 0, 0, 0
        MS = 0 
        PS = 0 
        turn = 0  
        xi = 1234
        list_player_move = []
        
        for turn in range(moves):
            """Easy part is presented as a special case together with the first round of the difficult part as no entires have been made before"""
            """Difficult part is after else planing computer move based on last player's input and throw count"""
            if select_difficulty ==1 or turn ==0:
                computer_move,xi = linear_congurence(xi)
            else:
                if list_player_move[-1] ==0 and throw10> throw00:
                        computer_move = 1
                elif list_player_move[-1] ==0 and throw10 < throw00:
                        computer_move = 0
                elif list_player_move[-1] ==1 and throw11 > throw01: 
                        computer_move = 1
                elif list_player_move[-1] ==1 and throw11 < throw01:
                        computer_move = 0
                else:
                    computer_move,xi = linear_congurence(xi)
                    
            """Player input is validated and then added to a list of all of the player's input"""                    
            player_move = input_player_try("Choose your number %s (0 or 1):" % (turn+1))
            list_player_move.append(player_move)
            
            """Throws are counted after the second turn as only then player has provided two inputs, which are relevant for the throw count"""  
            if turn in range(0,1):
                    pass
            else:
                    if list_player_move[-1] ==0 and list_player_move[-2] == 0:
                        throw00 +=1
                    elif list_player_move[-1] == 0 and list_player_move[-2] == 1:
                        throw01 +=1
                    elif list_player_move[-1] == 1 and list_player_move[-2] == 0:
                        throw10 +=1
                    elif list_player_move[-1] == 1 and list_player_move[-2] == 1:
                        throw11 +=1         
                          
            """Outcome of winner of the round, same results Computer wins, otherwise player wins""" 
            if player_move == computer_move: 
                        MS = MS + 1
                        print("player = 0 machine = 0 - Machine wins!")
                        print("You: %d Computer: %d" % (PS, MS))
            else:
                        PS = PS + 1
                        print ("player = 1 machine = 0 - Player wins!")
                        print("You: %d Computer : %d" % (PS,MS))
                        
            print('PLAYER: ' + '*'*PS)
            print('COMPUTER: ' + '*' *MS)
            
            """Each outcome of turn is added and the one how wins more turns overall wins the whole game"""
        if MS > PS:
            print("\n Machine wins, %s is Over final result Player: %d - Computer: %d" %(level_difficulty,PS,MS))
            Total_computer_wins.append(1)
        elif MS < PS:
            print ("\n You win, %s is Over final result Player: %d - Computer: %d" %(level_difficulty,PS,MS))
            Total_player_wins.append(1)
        else:    
            print("\n It is a tie, %s is Over final result Player: %d - Computer: %d" %(level_difficulty,PS,MS))
            Total_computer_wins.append(1)
            Total_player_wins.append(1)   
            
            """After each game Player has the option to restart game or stop game. When not restarting the party who won more rounds of games overall, wins the entire game"""
        restart = input_return_try("Do you want to start a new game? Yes(1) No(0):")
        if restart == 1:
            main()
            list_player_move.clear()
        else:
            print("Total Player Wins: %s, Total Computer Wins:%s" %(sum(Total_player_wins),sum(Total_computer_wins)))
    main()
game()
     
   
        
                