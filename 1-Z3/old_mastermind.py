from z3 import *
import itertools

n = 0
k = 0
sol = Solver()
global count 
# count = 0

def sum_to_one( ls ):
    at_least_one = Or( ls )
    at_most_one_list = []
    for pair in itertools.combinations( ls, 2):
        l1 = pair[0]
        l2 = pair[1]
        at_most_one_list.append( Or( Not(l1), Not(l2) ) )
    at_most_one = And( at_most_one_list  )
    return And( at_least_one, at_most_one )

def sum_le_k (ls, k):
	at_most_k_list = []
	for Parr in itertools.combinations(ls, k+1):
		NotParr = [Not(h) for h in Parr]
		at_most_k_list.append(Or(NotParr))  #change possible input into solver
	return And(at_most_k_list)

def sum_ge_k (ls, k):
	at_least_k_list = []
	for Parr in itertools.combinations(ls, k):
		at_least_k_list.append(And(Parr))  #change possible input into solver
	return Or(at_least_k_list)


def sum_eq_k (ls, k):
	if k == 1:
		return sum_to_one(ls)

	return And(sum_le_k(ls, k), sum_ge_k(ls, k))



def initialize(n_i ,k_i):
	global n, k, s
	n == n_i
	k == k_i




	# global count
	# if(n != 10):
	# 	raise Exception("n is given wrongly as "+str(n))
	# if(k != 6):
	# 	print("k is given wrongly as "+str(k))
	# count = 0




def get_second_player_move():
	global count
	if count == 0:
		count = count+1
		return [1, 1, 1, 1, 1, 1]
	if count == 1:
		count = count+1
		return [2, 2, 2, 2, 2, 2]
	if count == 2:
		count = count+1
		return [8, 5, 5, 1, 5, 5]
	if count == 3:
		count = count+1
		return [2, 5, 1, 6, 6, 6]
	if count == 4:
		count = count+1
		return [3, 2, 0, 9, 8, 5]
	if count == 5:
		count = count+1
		return [6, 6, 6, 6, 6, 6]
	if count == 6:
		count = count+1
		return [8, 8, 1, 1, 8, 8]
	if count == 7:
		count = count+1
		return [2, 5, 1, 3, 1, 8]

def put_first_player_response( red, white):
	print('This is masterMind speaking : red reported as {} and white reported as {} '.format(red, white))

