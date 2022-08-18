#!/usr/bin/python3

from z3 import *
import argparse
import itertools
import time
from subprocess import call

#-------------------------------
# Exercise :
# consider the following state machine with three bits
#   p' = q \/ r
#   q' = ~p /\ r
#   r' = ~(q == p)
#
# The machine updates value of the above variables according
# to the above update function. Primed variables indicate
# the next value of the bits
#
# 
# Using SAT solver find a cycle of three states of the state machine
#   -- the cycle must have 3 distinct states
#   -- the states may occur in any order
#----------------------------------


# state machine 

p = Bool("p")
q = Bool("q")
r = Bool("r")

p_update = Or( q, r )
q_update = And( Not(p), r )
r_update = Not( q == p )

vs  = [p       ,q       ,r       ]
ups = [p_update,q_update,r_update]



#----------------------------------------
# a few utitilities 


# supply for fresh bools
var_counter = 0
def count():
    global var_counter
    count = var_counter
    var_counter = var_counter +1
    return str(count)

def get_fresh_bool( suff = "" ):
    return Bool( "b_" + count() + "_" + suff )

def get_fresh_vec( vs, suff = "" ):
    n_vs = []
    for v in vs:
        n_vs.append( get_fresh_bool( suff ) )
    return n_vs

# substitutes a vector of variables
def substitute_vars( formula, from_vars, to_vars ):
    f = formula
    for j in range( 0, len(from_vars) ):
        f = substitute( f, (from_vars[j], to_vars[j]) )
    return f

#-----------------------------------

def rename_tr( vs, ups, frm, to ):
    cs = []
    for i in range( 0, len(ups) ):
        update = ups[i]
        x_to = to[i]
        frm_up = substitute_vars( update, vs, frm )
        cs.append( x_to == frm_up )
    return And( cs )

steps = 3
i = 0
v_frm = get_fresh_vec( vs )
bmc_vars = [v_frm]
path = []
while i < steps:
    i = i + 1
    v_to = get_fresh_vec( vs )
    bmc_vars.append(v_to)
    path.append( rename_tr( vs, ups, v_frm, v_to ) )
    v_frm = v_to

def vec_eq( vs0, vs1 ):
    cs = []
    for i in range(0,len(vs0)):
        cs.append( vs0[i] == vs1[i] )
    return And(cs)

# property
s_cnt = len(bmc_vars)
init_vars = bmc_vars[0]
for i in range(0,s_cnt-1):
    for j in range(i+1,s_cnt-1):
        path.append( Not( vec_eq( bmc_vars[i], bmc_vars[j])) )


path.append( vec_eq( bmc_vars[0], bmc_vars[s_cnt-1]) )

s = Solver()
s.add( And(path) )
r = s.check()
if r == sat:
    m = s.model()
    for vs in bmc_vars:
        for v in vs:
            if is_true( m[v] ):
                print("1", end=" ")
            else:
                print("0", end =" ")
        print("")
else:
    print("unsat")

