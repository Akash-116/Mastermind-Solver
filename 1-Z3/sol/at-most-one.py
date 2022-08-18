#!/usr/bin/python

from z3 import *
import argparse
import itertools
import time

# number of variables
n=10

# constructed list of variables
vs = []
for i in range(n):
    name = "e_{}".format(i)
    v = Bool(name)
    vs.append( v )
    
print(vs)

# write function that encodes that exactly one variable is one
def sum_to_one( ls ):
    at_least_one = Or( ls )
    at_most_one_list = []
    for pair in itertools.combinations( ls, 2):
        l1 = pair[0]
        l2 = pair[1]
        at_most_one_list.append( Or( Not(l1), Not(l2) ) )
    at_most_one = And( at_most_one_list  )
    return And( at_least_one, at_most_one )

# call the function
F = sum_to_one( vs )
print F

# construct Z3 solver
s = Solver()

# add the formula in the solver
s.add( F )

# check sat value
result = s.check()

if result == sat:
    # get satisfying model
    m = s.model()
    for v in vs:
        if is_true( m[v] ):
            print v
else:
    print "unsat"
