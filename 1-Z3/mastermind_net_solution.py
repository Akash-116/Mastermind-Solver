from z3 import *

def main():
    sol = Solver()
    cols = 5

    a = [[4,7,2,9,1],
         [9,4,6,8,7],
         [3,1,8,7,2],
         [1,5,7,3,9]]

    # variables
    x = [Int("x[%d]" % j) for j in range(cols)]

    # constraints
    '''
    All are distinct
    '''
    sol.add(Distinct(x))

    '''
    All numbers 0 <= x_i <= 9
    '''
    for i in range(cols):
        sol.add(x[i] >= 0, x[i] <= 9)

    sol.add(Sum([If(x[c] != a[0][c],1,0) for c in range(cols)]) == 5) # no number in correct position
    sol.add(Sum([If(x[c] != a[1][c],1,0) for c in range(cols)]) == 5) # no number in correct position
    sol.add(Sum([If(x[c] != a[2][c],1,0) for c in range(cols)]) == 4) # one number in correct position
    sol.add(Sum([If(x[c] != a[3][c],1,0) for c in range(cols)]) == 3) # two numbers in correct position

    cnt = 0

    while sol.check() == sat:
        mod = sol.model()
        xval = [mod.eval(x[j]).as_long() for j in range(cols)]
        if len(set(xval) & set(a[0])) == 1 and\
           len(set(xval) & set(a[1])) == 1 and\
           len(set(xval) & set(a[2])) == 2 and\
           len(set(xval) & set(a[3])) == 2:
            cnt += 1
            print(xval)
        sol.add(Or([x[i] != mod.eval(x[i]).as_long() for i in range(cols)])) # add constraint to check for different solution

    print("#solutions: ", cnt)

if __name__ == "__main__":
    main()
'''
[6, 5, 0, 3, 2]
#solutions:  1
'''

