import random
import matplotlib.pyplot as plt
#import numpy as np
#import sympy as sym
#from sympy import*

class Random_Walk:
    def random_walk(length):
        x, y = 0, 0
        step_x, step_y = [x], [y]

        for i in range(length):
            number = random.randint(1,4) #generates random number between 1and4
            if number == 1:
                x += 1
            elif number == 2:
                y += 1
            elif number == 3:
                x += -1
            else:
                y += -1
            step_x.append(x)
            step_y.append(y)
        return[step_x, step_y]

    walk = random_walk(100)
    print(walk)
    plt.plot(walk[0],walk[1])  #?
    plt.axis([-5, 5, -5, 5])
    plt.show()
#random.seed(1)
#x = 0
#walk =[]

#for i in range(10):
    #step= random.choice([-1,+1])
    #x += step
    #walk.append(x)
#print(walk)
#plt.plot(np.arange(10), walk)
#plt.show()
