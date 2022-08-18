#!/usr/bin/python3

from z3 import *
import argparse
import itertools
import time

problem1 = [
 [ 9, 0, 0,   0, 1, 0,   5, 0, 0],
 [ 7, 0, 0,   8, 0, 3,   0, 0, 2],
 [ 0, 0, 0,   0, 0, 0,   3, 0, 8],

 [ 0, 7, 8,   0, 2, 5,   6, 0, 0],
 [ 0, 0, 0,   0, 0, 0,   0, 0, 0],
 [ 0, 0, 2,   3, 4, 0,   1, 8, 0],

 [ 8, 0, 9,   0, 0, 0,   0, 0, 0],
 [ 5, 0, 0,   4, 0, 1,   0, 0, 9],
 [ 0, 0, 1,   0, 5, 0,   0, 0, 4]
]

problem2 = [
[ 0, 8, 0,   0, 0, 3,   0, 0, 0],
[ 5, 0, 3,   0, 4, 0,   2, 0, 0],
[ 7, 0, 4,   0, 8, 0,   0, 0, 3],

[ 0, 7, 0,   0, 0, 0,   5, 0, 0],
[ 0, 3, 0,   8, 0, 5,   0, 6, 0],
[ 0, 0, 1,   0, 0, 0,   0, 9, 0],

[ 9, 0, 0,   0, 3, 0,   7, 0, 6],
[ 0, 0, 7,   0, 2, 0,   3, 0, 1],
[ 0, 0, 0,   6, 0, 0,   0, 2, 0]
]

problem3 = [
[ 7, 0, 0,   8, 0, 5,   0, 0, 6],
[ 0, 0, 4,   0, 6, 0,   2, 0, 0],
[ 0, 5, 0,   2, 0, 4,   0, 9, 0],

[ 8, 0, 5,   0, 0, 0,   3, 0, 9],
[ 0, 1, 0,   0, 0, 0,   0, 6, 0],
[ 3, 0, 6,   0, 0, 0,   1, 0, 7],

[ 0, 6, 0,   5, 0, 7,   0, 1, 0],
[ 0, 0, 7,   0, 9, 0,   6, 0, 0],
[ 5, 0, 0,   3, 0, 6,   0, 0, 2]
]

problem4 = [
[ 0, 0, 0,   0, 0, 0,   0, 0, 0],
[ 0, 0, 0,   0, 0, 0,   0, 0, 0],
[ 0, 0, 0,   0, 0, 0,   0, 0, 0],

[ 0, 0, 0,   0, 0, 0,   0, 0, 0],
[ 0, 0, 0,   0, 5, 0,   0, 0, 0],
[ 0, 0, 0,   0, 0, 0,   0, 0, 0],

[ 0, 0, 0,   0, 0, 0,   0, 0, 0],
[ 0, 0, 0,   0, 0, 0,   0, 0, 0],
[ 0, 0, 0,   0, 0, 0,   0, 0, 0]
]

# problem = problem1
problem = problem4

vs = [ [ [ Bool ("e_{}_{}_{}".format(i,j,k)) for k in range(9)] for j in range(9)] for i in range(9)]

def sum_to_one( ls ):
    at_least_one = Or( ls )
    at_most_one_list = []
    for pair in itertools.combinations( ls, 2):
        l1 = pair[0]
        l2 = pair[1]
        at_most_one_list.append( Or( Not(l1), Not(l2) ) )
    at_most_one = And( at_most_one_list  )
    return And( at_least_one, at_most_one )

Fs = []

for i in range(9):
    for j in range(9):
        if problem[i][j] > 0 :
            k = problem[i][j] - 1
            Fs.append( vs[i][j][k] )

for i in range(9):
    for j in range(9):
        ls = []
        for k in range(9):        
            ls.append( vs[i][j][k] )
        Fs.append( sum_to_one( ls ) )

for j in range(9):
    for k in range(9):
        ls = []
        for i in range(9):        
            ls.append( vs[i][j][k] )
        Fs.append( sum_to_one( ls ) )

for i in range(9):
    for k in range(9):
        ls = []
        for j in range(9):        
            ls.append( vs[i][j][k] )
        Fs.append( sum_to_one( ls ) )

for i in range(3):
    for j in range(3):
        for k in range(9):        
            ls = []
            for r in range(3):
                for s in range(3):
                    ls.append( vs[3*i+r][3*j+s][k] )
            Fs.append( sum_to_one( ls ) )
                


s = Solver()
s.add( And( Fs ) )
if s.check() == sat:
    m = s.model()
    for i in range(9):
        if i % 3 == 0 :
            print("|-------|-------|-------|")
        for j in range(9):
            if j % 3 == 0 :
                print ("|", end =" ")
            for k in range(9):
                val = m[vs[i][j][k]]
                if is_true( val ):
                    print("{}".format(k+1), end =" ")
        print("|")
    print("|-------|-------|-------|")
else:
    print("sudoku is unsat")

# print vars
