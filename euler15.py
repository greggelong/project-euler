'''
latice paths are very cool

solutions introduce you to some other areas of math

like pascal's triangle

and the central binomal coefficient

it can be solved on a calculator using the formula

(2R!)/R!^2  here R is 20

these solutions use the fact that  to get from

(0,0) to (m,n) is equal to the number of routes
from
(0,0) to (m-1, n) + (0,0) to (m,n-1)

the first one is a simple recursive
but the stack gets too filled up

the second is iterative

and it solves it quickly

for greater detail see the notes from project euler you
recieve after solving


'''
#
def countRoutes(m,n):
    ''' recursive solution lattice paths'''
    # exit condition
    if n == 0 or m == 0:
        return 1
    # recursive call to rule for lattice paths 
    return countRoutes(m-1,n) + countRoutes(m,n-1)



# iterative solution see notes and 


def cntRoutes(m,n):
    # create a 2 d array in python style
    rows,cols = m+1, n+1
    grid = [[1]*cols]*rows
    
    print(grid)
    for i in range(1, m+1):
        for j in range(1, n+1):
            grid[i][j] = grid[i -1][j] + grid[i][j-1]
    
    return grid              

print(cntRoutes(20,20))