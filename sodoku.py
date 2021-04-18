import numpy as np
import time,sys,os


def entre_grid():
    grid = []
    f = open(os.path.join(sys.path[0], "sudoku.txt"), "r")
    for line in f:
        k=[int(i) for i in line.replace('\n','')]
        grid+=[k]
    return grid
    
grid = entre_grid()


def possible(x,y,n) :
    global grid

    for i in range(0,9) :   #column
        if grid[x][i] == n :
            return False

    for i in range(0,9) :  #row
        if grid[i][y] == n :
            return False

    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(0,3) :  #box
        for j in range(0,3) :
            if grid[x0+i][y0+j] == n :
                return False

    return True
    
def solve() :
    global grid
    for x in range(9) :
        for y in range(9) :
            if grid[x][y] == 0 :
                for n in range (1,10) :
                    if possible(x,y,n) :

                        grid[x][y] = n
                        solve() 
                        grid[x][y] = 0
                        
                return 

    print("temps d'execution :",time.time()-start)
    print(np.matrix(grid))
    sys.exit()

start = time.time()
solve()
