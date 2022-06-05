import random
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()

# x = [1, 2, 3, 4, 5, 6]
x = [1, 2, 3]
# y = [0,0,0,0,0,0]
y = [0,0,0]

node = [0, 0, 0]

def update(i):
    plt.cla()

    if i %10 == 0:
        node[0] += 1

    # # rand = random.randint(0, 5)
    # rand_y = random.randint(0, 1)
    # # y[0] += 1
    # # if i %5 == 0:
    # if rand_y == 1:
    #     # y[0] -= 4
    #     y[0] -= 0.5 # 1
    # else:
    # y[0] += 1 * (1 - (node[0]*0.1))
    y[0] = y[0] + ((9/10) ** node[0])
        
    ax.bar(x,y, color=['#66bd63'])

    plt.title('i=' + str(i))

    if np.max(y) <100:
        plt.ylim(0, 100)

ani = animation.FuncAnimation(fig, update, interval = 100)
plt.show()