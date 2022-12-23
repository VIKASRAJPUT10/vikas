#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[2]:


test_board=['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[3]:


def player_input():
    'output=(player 1 marker,player 2 marker)'
    marker=''
    while marker!='X' and marker!='O':
        marker=input('player1 choose(X or O): ').upper()
    if marker=='X':
        return('X','O')
    else:
        return('O','X')


# In[4]:


player1_marker,player2_marker=player_input()


# In[5]:


player2_marker


# In[6]:


def place_marker(board,marker,position):
    board[position]=marker


# In[7]:


place_marker(test_board,'$',9)
display_board(test_board)


# In[8]:


def win_check(board,mark):
    return((board[7]==board[8]==board[9]==mark)or
          (board[4]==board[5]==board[6]==mark)or
           (board[1]==board[2]==board[3]==mark)or
           (board[7]==board[4]==board[1]==mark)or
           (board[8]==board[5]==board[2]==mark)or
           (board[9]==board[6]==board[3]==mark)or
           (board[7]==board[5]==board[3]==mark)or
           (board[9]==board[5]==board[1]==mark))


# In[13]:


display_board(test_board)
win_check(test_board,'X')


# In[14]:


import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'player1'
    else:
        return 'player2'


# In[15]:


def space_check(board,position):
    return board[position]==''


# In[16]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[17]:


def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('choose a position:(1-9)'))
    return position


# In[20]:


def replay():
    choice=input('play again ? yes or no')
    return choice=='yes'


# In[23]:


print('Welcome to tic tac toe')
while True:
    the_board=['']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+'will go first')
    play_game=input('ready to play? y or n?')
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='player 1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON !!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('GAME TIE !!!')
                    break
                else:
                    turn='player 2'
        else:
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON !!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('GAME TIE !!!')
                    break
                else:
                    turn='player 1'
    if not replay():
        break
                    


# In[ ]:




