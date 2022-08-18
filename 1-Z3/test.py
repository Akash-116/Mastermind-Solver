

from z3 import *
import argparse
import itertools
import time
from subprocess import call

# n is the no. of queens

# def sum_upto_k (ls, k):
# 	# ls is the list of bools
# 	# k is the parameter in "summation <= k"

p1 = Bool("p1")
p2 = Bool("p2")

s = solver(p1+p2==2)
print(s)
