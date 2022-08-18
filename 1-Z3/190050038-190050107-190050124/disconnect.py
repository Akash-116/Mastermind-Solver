from z3 import *

def find_minimal(graph,s,t):
	
	num_edge = len( graph )

	if(num_edge==0):
		return 0

	v_min = min(graph[0][0], graph[0][1])
	v_max = max(graph[0][0], graph[0][1])

	for i in range(1, num_edge):
		v_min = min(v_min,graph[i][0],graph[i][1])
		v_max = max(v_max,graph[i][0],graph[i][1])

	num_vertex = v_max - v_min + 1  # No. of vertices

	if(s<v_min or s>v_max or t<v_min or t>v_max):
		return 0
 
	p = [Bool("p_{}".format(i)) for i in range(v_min,v_max+1)] # Boolean for vertices reachable from s.
	e = [Bool("e_{}".format(i)) for i in range(num_edge)] # Boolean for edges removed.
 
	sol = Optimize()
	 
	sol.minimize(Sum([If(e[j],1,0) for j in range(num_edge)]))  # if e[j] is true, we have removed edge 'j'

	sol.add(p[s-v_min]) # every node has a path to itself.
	sol.add(Not(p[t-v_min])) # t shouldn't be reachable from s

	# If edge exists between i and j, then reachable(i) <=> reachable(j) 
	sol.add(And([Implies(Not(e[j]),And(Implies(p[graph[j][0]-v_min],p[graph[j][1]-v_min]),Implies(p[graph[j][1]-v_min],p[graph[j][0]-v_min]))) for j in range(num_edge)]))

	r=sol.check()

	if(r == sat):
		mo = sol.model()
		count = 0
		for i in range(num_edge):
			if(is_true(mo[e[i]])):
				count = count + 1		
		return count
		
	else:
		print("Something is Wrong")
		return -1

