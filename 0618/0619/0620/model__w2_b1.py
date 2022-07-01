from statistics import mode
from turtle import shape
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [80, 60, 40, 20, 5]
y2 = [20, 40, 60, 80, 95]

def perceptron(x1):
	w1 = 2		#任意の値を代入
	b = 1	#任意の値を代入
	sum = x1*w1
	if sum <= b:
		return 0
	else:
		return 1

print("perceptron = {}\n".format(perceptron(1)))


# w*x -b < 0

import numpy as np
import matplotlib.pyplot as plt

# 0618 neural network # ニューロンの発火

# 発見率
x = 0.8
pre_x = np.zeros(shape=10)
for i in range(10):
    pre_x[i] += 1.0 - i*0.1

print("発見率:{}".format(pre_x))
################# MODEL ####################
# 重みとバイアスの初期値
weights = 2
biases = 1
################# MODEL ####################

# モデルを定義
model = (x, weights, biases)

# pre_model = (pre_x, weights, biases)

# def sigmoid(x):
#     return 1/(1+np.exp(-x))
def step(x):
#   return 1.0 * (x >= 0.0)
    return 1.0 * (x < 0.0)  # (x < 2.0) # ステップ関数の逆ver.

def trigar(u):
    # if u >= 0:
    if u > 0:                       # (0 = ) w*x - b > 0 つまり、 b (1) < w*x (2*x) なら Go
        # print("50%以上(>= 0.5)")
        print("> 0.5")
        return 0
    else:
        # print("50%未満(< 0.5)")
        print("<= 0.5")
        return 1

def activation(x, w, b):
    u = round(np.dot(x, w) - b, 1)  # u = w*x - b を小数点第一位で四捨五入
    print("u = {}".format(u))
    return trigar(u) #sigmoid(u), step(u)

y = activation(*model)
if y == 0:
    # print("y = {} stay".format(y))
    print("y = {} Go".format(y))
else:
    print("y = {} Back".format(y))


# 逆ステップ関数の図示
# xline = np.arange(-5, 5, 0.1)
# yline = step(xline)
# plt.plot(xline, yline, "g")
# plt.show()

print("\n########################")
pre_y = np.zeros(shape=10)
for i in range(10):
    pre_y[i] = activation(pre_x[i], weights, biases)
    if pre_y[i] == 0:
        print("y = {} Go".format(pre_y[i]))
    else:
        print("y = {} Back".format(pre_y[i]))

print(pre_y)