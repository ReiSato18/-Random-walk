import numpy as np
import random
import itertools
from menger import stage3 as stage 
n = 27
itr = 10
step = [i for i in range(0,itr+1)]
r_list = [i for i in range(0,n)]
walk = np.zeros([n,n,n],dtype=np.uint8)
walk[0,0,0] = 1
prob =[]
time=[]
for t in step:
    if t == 0:
        pass
    else:
        number = random.randint(1,6)
        next_walk = np.zeros([n,n,n],dtype=np.uint8)
        for i in itertools.product(r_list,r_list,r_list):
            x = i[0]
            y = i[1]
            z = i[2]
        #Boundary condition
            x1 = (x-1 + n) % n
            x2 = (x+1) % n
            y1 = (y-1 + n) % n
            y2 = (y+1) % n
            z1 = (z-1 + n) % n
            z2 = (z+1) % n
            if  stage[i]== 0:
                continue
            else:
                if walk[i]==1:
                    if number == 1:
                        if stage[x2,y,z]==1:
                            next_walk[x2,y,z]=walk[i]
                        else:
                            next_walk[x,y,z]=walk[i]
                    elif number == 2:
                        if stage[x,y2,z]==1:
                            next_walk[x,y2,z]=walk[i]
                        else:
                            next_walk[x,y,z]=walk[i]
                    elif number == 3:
                        if stage[x,y,z2]==1:
                            next_walk[x,y,z2]=walk[i]
                        else:
                            next_walk[x,y,z]=walk[i]
                    elif number == 4:
                        if stage[x1,y,z]==1:
                            next_walk[x1,y,z]=walk[i]
                        else:
                            next_walk[x,y,z]=walk[i]
                    elif number == 5:
                        if stage[x,y1,z]==1:
                            next_walk[x,y1,z]=walk[i]
                        else:
                            next_walk[x,y,z]=walk[i]
                    elif number == 6:
                        if stage[x,y,z1]==1:
                            next_walk[x,y,z1]=walk[i]
                        else:
                            next_walk[x,y,z]=walk[i]
                else:
                    continue
           
        walk = np.copy(next_walk)
        if t!=0 and walk[0,0,0]== 1:
            prob.append((1/6)**t)
            time.append(t)
        else:
            continue
print(time,prob)
