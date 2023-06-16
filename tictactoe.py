"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    
    
    
    o_count = sum(i.count(O) for i in board)
    x_count = sum(i.count(X) for i in board)
    if o_count > x_count:
        return X
    elif x_count > o_count:
        return O
    else:
        return X
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i, row in enumerate(board):
        for j, cells in enumerate(row):
            if cells == None:
                possible_actions.add((i,j))
    return possible_actions

def result(board, action):
    
    if action == None or len(action) != 2:
        raise Exception("No valid State")

    
    i, j = action
    
    #change board depending on action
    if board[i][j] == EMPTY:
        new_board = copy.deepcopy(board)
        new_board[i][j] = player(board)
        return new_board
    else:
        raise Exception("No valid State")

def winner(board):
    for i in board:
        if i.count(X) == 3:
            return X
        if i.count(O) == 3:
            return O
        
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == X:
            return X
        if board[0][j] == board[1][j] == board[2][j] == O:
            return O

    if board[0][0] == board[1][1] == board[2][2] == X or board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O or board[0][2] == board[1][1] == board[2][0] == O:
        return O

    return None






def terminal(board):

    x_count = sum(i.count(X) for i in board)
    o_count = sum(i.count(O) for i in board)
    if x_count + o_count == 9:
        return True
    if utility(board) != 0:
        return True
    return False


def utility(board):
    
    utility = 0
    if winner(board) == X:
        utility = 1
    elif winner(board) == O:
        utility = -1
    else:
        utility = 0
    return utility

def Max_Value(state):
    v = -math.inf
    if terminal(state):
        return utility(state)
    for action in actions(state):
        v = max(v,Min_Value(result(state,action)))
    return v

def Min_Value(state):
    v = math.inf
    if terminal(state):
        return utility(state)
    for action in actions(state):
        v = min(v,Max_Value(result(state,action)))
    return v

def minimax(board):
    
    if terminal(board) == True:
        return None
    if player(board) == X:
        v = - math.inf
        best_action = None
        for action in actions(board):
            min_val = Min_Value(result(board,action))
            if min_val > v:
                v = min_val
                best_action = action
        return best_action
    elif player(board) == O:
        v = math.inf
        best_action = None
        for action in actions(board):
            max_val = Max_Value(result(board,action))
            
            if max_val < v:
                v = max_val
                best_action = action
        return best_action


