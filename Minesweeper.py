"""
Student: Omri Leizerovitch
ID: 316542166
Assignment : no. 6
Program: minesweeper.py
"""
import random
class MSSquare:
    ''' minesweeper square '''
    def __init__(self):
        self.__has_mine = False
        self.__hidden = True
        self.__neighbor_mines = 0
    
    @property                 # return if has mine
    def has_mine(self):
        return self.__has_mine
    @has_mine.setter          #set if has mine
    def has_mine(self,value):
        self.__has_mine = value
        
    @property                 # return if hidden
    def hidden(self):
        return self.__hidden
    @hidden.setter            # set if hidden
    def hidden(self,value):
        self.__hidden = value
        
    @property                 # return number of neighbors mine
    def neighbor_mines(self):
        return self.__neighbor_mines
    @neighbor_mines.setter    # set number of neighbors mine
    def neighbor_mines(self,value):
        self.__neighbor_mines = value
        
    def __str__(self):
        if not self.has_mine and not self.hidden:
            return str(self.neighbor_mines)
        else:
            return ' '
        
def print_board(lst):
    ''' function that get a list (board) and print vizualize board '''
    line = '+---'
    print(' {0}+'.format(line*len(lst)))
    for i in range(len(lst)):
        print('{0}|'.format(i+1), end='')
        for j in range(len(lst[i])):
            print(' {0} |'.format(lst[i][j]),end='')
        print()
        print(' {0}+'.format(line*len(lst)))
    for i in range(len(lst)):
        print('   {0}'.format(i+1),end= '')
    print()
    
def print_board_end_game(lst):
    ''' function that get a list (board) and print the reveal board
    if you won or if you lose '''
    line = '+---'
    print(' {0}+'.format(line*len(lst)))
    for i in range(len(lst)):
        print('{0}|'.format(i+1), end='')
        for j in range(len(lst[i])):
            if lst[i][j].has_mine:
                print(' X |',end='')
            else:
                print(' {0} |'.format(lst[i][j].neighbor_mines), end='')
        print()
        print(' {0}+'.format(line*len(lst)))
    for i in range(len(lst)):
        print('   {0}'.format(i+1),end= '')
    print()
    
def count_neighbor_mine(board,row,col):
    ''' function that counts the number of mines around the location,
    (the location is board[row][col]) and updated the result in the list '''
    neighbor_count = 0
    if row-1 >= 0 and col-1 >= 0:                        # 1
        if board[row-1][col-1].has_mine:
            neighbor_count+=1
    if row-1 >= 0:                                      # 2
        if board[row-1][col].has_mine:
            neighbor_count+=1
    if row-1 >= 0 and col+1 < len(board):              # 3
        if board[row-1][col+1].has_mine:
            neighbor_count+=1
    if col-1 >= 0:                                      # 4
        if board[row][col-1].has_mine:
            neighbor_count+=1
    if col+1 < len(board):                            # 6
        if board[row][col+1].has_mine:
            neighbor_count+=1
    if row+1 < len(board) and col-1 >= 0:              # 7
        if board[row+1][col-1].has_mine:
            neighbor_count+=1
    if row+1 < len(board):                            # 8
        if board[row+1][col].has_mine:
            neighbor_count+=1
    if row+1 < len(board) and col+1 < len(board):    # 9
        if board[row+1][col+1].has_mine:
            neighbor_count+=1
    if neighbor_count!=0:
        board[row][col].neighbor_mines = neighbor_count
    return board
    
def reveal_neighbor_rec(lst,row,col,not_hidden_count):
    ''' function that get a list, row, column and counter (of not hidden locations),
    and reveals recursively if there is an empty "box" near the location,
    and update the counter that will tell us how much "boxes" did we reveal so far'''
    lst[row][col].hidden = False
    not_hidden_count+=1
    if row-1 >= 0 and col-1 >= 0:
        if lst[row-1][col-1].neighbor_mines > 0 and lst[row-1][col-1].hidden == True:
            lst[row-1][col-1].hidden = False
            not_hidden_count+=1
        elif lst[row-1][col-1].hidden == True:
            lst, not_hidden_count = reveal_neighbor_rec(lst,row-1,col-1,not_hidden_count)
    if row-1 >= 0:
        if lst[row-1][col].neighbor_mines > 0 and lst[row-1][col].hidden == True:
            lst[row-1][col].hidden = False
            not_hidden_count+=1
        elif lst[row-1][col].hidden == True:
            lst, not_hidden_count = reveal_neighbor_rec(lst,row-1,col,not_hidden_count)
    if row-1 >= 0 and col+1 < len(lst):
        if lst[row-1][col+1].neighbor_mines > 0 and lst[row-1][col+1].hidden == True:
            lst[row-1][col+1].hidden = False
            not_hidden_count+=1
        elif lst[row-1][col+1].hidden == True:
            lst, not_hidden_count = reveal_neighbor_rec(lst,row-1,col+1,not_hidden_count)
    if col-1 >= 0:
        if lst[row][col-1].neighbor_mines > 0 and lst[row][col-1].hidden == True:
            lst[row][col-1].hidden = False
            not_hidden_count+=1
        elif lst[row][col-1].hidden == True:
            lst, not_hidden_count = reveal_neighbor_rec(lst,row,col-1,not_hidden_count)
    if col+1 < len(lst):
        if lst[row][col+1].neighbor_mines > 0 and lst[row][col+1].hidden == True:
            lst[row][col+1].hidden = False
            not_hidden_count+=1
        elif lst[row][col+1].hidden == True:
            lst, not_hidden_count = reveal_neighbor_rec(lst,row,col+1,not_hidden_count)
    if row+1 < len(lst) and col-1 >= 0:
        if lst[row+1][col-1].neighbor_mines > 0 and lst[row+1][col-1].hidden == True:
            lst[row+1][col-1].hidden = False
            not_hidden_count+=1
        elif lst[row+1][col-1].hidden == True:
            lst, not_hidden_count = reveal_neighbor_rec(lst,row+1,col-1,not_hidden_count)
    if row+1 < len(lst):
        if lst[row+1][col].neighbor_mines > 0 and lst[row+1][col].hidden == True:
            lst[row+1][col].hidden = False
            not_hidden_count+=1
        elif lst[row+1][col].hidden == True:
            lst, not_hidden_count = reveal_neighbor_rec(lst,row+1,col,not_hidden_count)
    if row+1 < len(lst) and col+1 < len(lst):
        if lst[row+1][col+1].neighbor_mines > 0 and lst[row+1][col+1].hidden == True:
            lst[row+1][col+1].hidden = False
            not_hidden_count+=1
        elif lst[row+1][col+1].hidden == True:
            lst, not_hidden_count = reveal_neighbor_rec(lst,row+1,col+1,not_hidden_count)
    return lst, not_hidden_count

def main():
    while 1: 
        try:#check if input is legal, if not return exception and gives another try
            size = int(input('Enter size: '))
            if size<4 or size>9:
                raise Exception ('\nChoose size between 4-9')
            else:
                break
        except Exception as error:
            print(error)
            
    board=[[] for i in range(size)] # make the list (board)
    for i in range(len(board)):
        for j in range(len(board)):
            board[i].append(MSSquare()) #put in every place a default MSSquare type
    
    while 1:
        try:#check if input is legal, if not return exception and gives another try
            mine = int(input('Enter number of mines (no more than twice the size!): '))
            if mine > 2*size or mine < 1:
                raise Exception ('\nChoose mines between 1 to {0}'.format(2*size))
            else:
                break
        except Exception as error:
            print(error)
            
    print_board(board) #print empty board
    count = 0
    while count < mine: #arrange mines randomly
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        if not board[x][y].has_mine:
            board[x][y].has_mine = True
            count+=1
                
    for r in range(size): #count the number of neighbor mines in every place on the board
        for c in range(size):
            board = count_neighbor_mine(board,r,c) 
    
    not_hidden_count = 0
    while 1:
        try:#check if input is legal, if not return exception and gives another try
            x = input('Enter your choice (row ,column):')
            x = x.split()
            row , col = int(x[0])-1 , int(x[1])-1
            if row >= 0 and row < size and col >= 0 and col < size:
                if board[row][col].has_mine:
                    print_board_end_game(board)
                    print('\nYou hit a mine. You Lose...')
                    break
                if board[row][col].neighbor_mines > 0:
                    board[row][col].hidden = False
                    not_hidden_count+=1
                    if not_hidden_count == (size*size)-mine:
                        print_board_end_game(board)
                        print('\nYou Won!')
                        break
                    else:
                        print_board(board)
                        print('\n{0} is still hidden. Keep trying!'.format((size*size)-mine-not_hidden_count))
                else:
                    board, not_hidden_count = reveal_neighbor_rec(board,row,col,not_hidden_count)
                    if not_hidden_count == (size*size)-mine:
                        print_board_end_game(board)
                        print('\nYou Won!')
                        break
                    else:
                        print_board(board)
                        print('\n{0} is still hidden. Keep trying!'.format((size*size)-mine-not_hidden_count))
            elif row <0 or row > size-1:
                raise Exception ('\nChoose row between 1 to {0}!'.format(size))
            elif col <0 or col > size-1:
                    raise Exception ('\nChoose column between 1 to {0}!'.format(size))
        except Exception as error:
            print(error)
main()
