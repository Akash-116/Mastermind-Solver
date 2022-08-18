from z3 import *

 
red_all =[]
white_all = []
move_all = []


n = 0
k = 0
x = 0
sol = Optimize()

def initialize(n_i ,k_i):
	global n, k, sol, x
	n = n_i
	k = k_i
	x = [Int("x[%d]" % j) for j in range(k)]
	for i in range(k):
		sol.add(x[i] >= 0, x[i] <= n-1)


def get_second_player_move():
	global n, k, move_all, sol, x, new_move

	sol.check()
	move_z3 = sol.model()
	new_move = [move_z3[x[i]] for i in range(k)]
	move_all.append(new_move)
	return new_move


	# while sol.check() == sat:
	# 	new_move = sol.model()
	# 	xval = [new_move.eval(x[j]).as_long() for j in range(k)]
	# 	satisfy = True
	# 	for i in range(len(white_all)):
	# 		if red_white(xval, move_all[i]) != red_all[i] + white_all[i]:
	# 			satisfy = False
	# 			sol.add(Or([x[i] != mod.eval(x[i]).as_long() for i in range(cols)])) # add constraint to check for different solution
	# 			break
	# 	if satisfy:
	# 		break



	# move_all.append(xval)
	# return xval



def put_first_player_response( red, white):
	global n, k, red_all, white_all, move_all, new_move ,sol ,x
	red_all.append(red)
	white_all.append(white)

	sol.add_soft(Sum([If(x[c] != new_move[c],1,0) for c in range(k)]) == k-red) # no. of terms in correct position

	sol.add_soft(
		Sum(
			[ If(
					Sum([If(x[j]==i,1,0) for j in range(k)]) <= Sum([If(new_move[j]==i,1,0) for j in range(k)]), 
					Sum([If(x[j]==i,1,0) for j in range(k)]), # no. of terms in answer with color 'i'
					Sum([If(new_move[j]==i,1,0) for j in range(k)]) # no. of terms in my move with color 'i'
				) for i in range(n)] # selecting min of no. of terms with a color 'i'
		) == red + white
	)


