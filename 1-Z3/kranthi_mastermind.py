from z3 import *

def initialize(n,k):
	global N,K,Move,s,x
	N=n
	K=k
	Move=[]
	x = [ Int('x%s' % i) for i in range(K) ]
	s = Optimize()
	c1= [ And( 0<=x[i] , x[i]<=N-1 ) for i in range(K) ]
	s.add( c1 )


def get_second_player_move():
	global N,K,Move,s,x
	if s.check() == sat:
		m = s.model()
		Move=[]
		for i in range(K):
			Move.append(m[x[i]])
	return Move


def put_first_player_response( red, white ):
	global N,K,Move,s,x
	s.add_soft( Sum( [ If( x[i]==Move[i] ,1,0) for i in range(K) ] ) == red )
	s.add_soft( 
		Sum( 
			[If( 
				Sum([If(x[j]==i,1,0) for j in range(K)]) <= Sum([If(Move[j]==i,1,0) for j in range(K)]), # no. of color i 
				Sum([If( x[j]==i ,1,0) for j in range(K)]) , # no. of color i in Final Answer
				Sum([If( Move[j]==i ,1,0) for j in range(K)]) # no. of color i in Our guess
				) 
			for i in range(N)]
		) == red+white 
	)