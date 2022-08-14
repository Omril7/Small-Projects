# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 22:52:36 2022

@author: omril
"""
import numpy as np

board = [[7, 0, 2, 0, 5, 0, 6, 0, 0],
          [0, 0, 0, 0, 0, 3, 0, 0, 0],
          [1, 0, 0, 0, 0, 9, 5, 0, 0],
          [8, 0, 0, 0, 0, 0, 0, 9, 0],
          [0, 4, 3, 0, 0, 0, 7, 5, 0],
          [0, 9, 0, 0, 0, 0, 0, 0, 8],
          [0, 0, 9, 7, 0, 0, 0, 0, 5],
          [0, 0, 0, 2, 0, 0, 0, 0, 0],
          [0, 0, 7, 0, 4, 0, 2, 0, 3]]

# reset = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

count = 0

def possible(y,x,n):
    global board
    for i in range(0,9):
        if board[y][i] == n:
            return False
    for i in range(0,9):
        if board[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if board[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global board
    global count
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0
                return
    count += 1
    print("\nOption number {}:".format(count))
    print(np.matrix(board)) 
    

solve()
print("\n\nTotal options =",count)