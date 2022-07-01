# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y1 = [80, 60, 40, 20, 5]
# y2 = [20, 40, 60, 80, 95]

# plt.bar(x, y1)
# plt.bar(x, y2, bottom=y1)



# plt.show()


# label = ["A", "B", "C", "D", "E"]

# plt.pie(x, labels=label)
# plt.axis('equal') # 出力が楕円形になるのを防ぐため
# plt.show()


import numpy as np
a = np.array([1, 2])
b = np.array([4, 3])
u = np.dot(a, b)
print(u)

a = np.array([2])
b = np.array([4])
u = np.dot(a, b)
print(u)

# from fractions import Fraction

# print(float(Fraction('0.1')+Fraction('0.2'))) # 0.3
# print(float(Fraction('1')/(Fraction('1')/Fraction('60')))) # 60.0

import numpy as np
import matplotlib.pylab as plt

def step_function(x):
  y = x > 0
  return y #.astype(np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
# plt.show()



# x = np.zeros(shape=10)
# for i in range(5):
#     x[i] += 1.0 - i*0.1

# print("発見率:{}".format(x))

# x = []

# for i in range(5):
#     x += (1.0 - i*0.1)

# print("発見率:{}".format(x))




# <- 0623 メモ

# NODE:[0, 0, 1, 1, 1, 1, 0, 0, 1, 0]
# y = 1.0 Back
# y = 1.0 Back
# y = 1.0 Back
# y = 1.0 Back
# y = 0.0 Go
# y = 0.0 Go
# y = 0.0 Go
# y = 1.0 Back
# y = 0.0 Go
# y = 1.0 Back

# 発見率:[0.         0.         0.33333333 0.5        0.6        0.66666667
#  0.57142857 0.5        0.55555556 0.5       ]
# 発火の可否 : [1. 1. 1. 1. 0. 0. 0. 1. 0. 1.]


# NODE:[0, 1, 0, 0, 0, 0, 0, 1, 1, 0]
# y = 1.0 Back
# y = 1.0 Back
# y = 1.0 Back
# y = 1.0 Back
# y = 1.0 Back
# y = 1.0 Back
# y = 1.0 Back
# y = 1.0 Back
# y = 1.0 Back
# y = 1.0 Back

# 発見率:[0.         0.5        0.33333333 0.25       0.2        0.16666667
#  0.14285714 0.25       0.33333333 0.3       ]
# 発火の可否 : [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]




α = 2
# P = 3
P = np.array([[.1,.2],
              [.3,.4],
               ])
mat = α @ P
print(f"mat:{mat}")