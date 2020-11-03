''' the permutaton method gives the answer for lattice paths for smaller grid but
and more interesting it can give directions for movement in the pat"

in this example the number it is a 4 by 4 grid

so to get from 0,0 to 4,4  with out backtracking

is the move left*4 down*4

you use that as you initial string and

and then find permutations to give you the other directions

the problem is that itertools will give duplicates

so we use set() to get rid of duplictaes

it is too slow to be scaleable

need to find a more scaleable algorithm
'''

import itertools
# these are the moves you can make on outside of the lattice from 0,0 to m,n
# for euler 15 it would be L *20 D *20

#moves = "L"*4 + "D"*4
#moves = "LLLLDDDD"
moves = ["L","L","L","L","D","D","D","D"]
# get all the permutations which include duplicates
pmoves = list(itertools.permutations(moves,len(moves)))

# use set to get rid of the duplicates

ndpmoves = set(pmoves)

#show the answer
#print(pmoves, len(pmoves))

print(ndpmoves, len(ndpmoves))


#for i in set(perm):
#    print(i)
    
    

