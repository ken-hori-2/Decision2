from cProfile import label
from statistics import mode
from turtle import shape
from xmlrpc.client import TRANSPORT_ERROR
import matplotlib.pyplot as plt
import numpy as np
import random

# s >= b (= w*x) 0622 ver.

# model__w2_b1 copy 2_matrix.py の整理版 + 連続数版

# PARAMETER
N = 10
X = int(input("試行回数 X : "))
IGNITION_LIST = np.zeros(shape=X)
FIRE = False
NON_FIRE = 0
CONTINUE_NUM = np.zeros(X*N).reshape((X, N))
COUNT = np.zeros(shape=X)
NODE = np.zeros(X*N).reshape((X, N))
IGNITION_RESULT = np.zeros(X*N).reshape((X, N))

################# MODEL ####################
# 重みとバイアスの初期値
WEIGHTS = 2
BAIASES = 1
# モデルを定義
MODEL = (CONTINUE_NUM, WEIGHTS, BAIASES)
################# MODEL ####################

def rand_NODE(zero, one, x):
  return [random.randint(zero, one) for i in range(x)]

def perceptron(x1):
	w1 = -1 # 2
	b = x1*w1 + 4 # 3  w1 * x1 + b > 1  -> w1 * x1 + b -1 > 0
	if 1 < b:
		return 0
	else:
		return 1

print("\n##########################\nノードの総数 {} * {} セット で試験開始\n##########################".format(N, X))

NODE = [rand_NODE(0, 1, N) for i in range(X)]
print("\nNODE (10列 * 5行)\nX={}".format(NODE))


for x in range(X):
    print("\n########################\nNODE:{}".format(NODE[x]))
    for i in range(N):
        if NODE[x][i] == 0:
            if NODE[x][i-1] == 0 and i > 0:
                COUNT[x] += 1
            elif NODE[x][i-1] == 1 or i == 0:
                COUNT[x] += 1
        else:
            COUNT[x] = 0
        CONTINUE_NUM[x][i] = COUNT[x]

        IGNITION_RESULT[x][i] = perceptron(CONTINUE_NUM[x][i])
        if IGNITION_RESULT[x][i] == 0:
            print("y = {} Go".format(IGNITION_RESULT[x][i]))
            num = i + 1     # NODEは0からではなく、1からだから + 1
        else:
            print("y = {} Back".format(IGNITION_RESULT[x][i]))
            FIRE = True
            num = i + 1     # NODEは0からではなく、1からだから + 1
            break
    if FIRE:
        IGNITION_LIST[x] = num # i
        FIRE = False
    else:
        NON_FIRE += 1
        IGNITION_LIST[x] =  num

    print("\n連続数:{}".format(CONTINUE_NUM[x]))
    print("発火の可否(位置) : {}".format(IGNITION_RESULT[x]))

print("\n########################")



IGINITION_AVE = sum(IGNITION_LIST)/X
print("IGNITION_LIST:{}".format(IGNITION_LIST))
print("IGNITION_LIST_SUM:{}\nIGNITION_LIST_AVE:{}".format(sum(IGNITION_LIST), IGINITION_AVE))
print("NON_FIRE(発火しなかった): {} 回".format(NON_FIRE))

# 結果グラフで描写
fig = plt.figure(figsize=(10, 5))
x_plot = np.arange(1, X+1, 1)
plt.title("Graph of IGNITION locations")
plt.xlabel("試行回数 X")
plt.ylabel("発火時のNODE位置")
plt.plot(x_plot, IGNITION_LIST, label = "IGNITION location")
plt.hlines(IGINITION_AVE, 1, X, color="orange", linewidth = 3, label="average")
plt.legend()
plt.grid()
plt.show()
# num = input("input figure num : ")
# fig.savefig("/Users/ken/Desktop/Decision-making/0618/0619/0620/fig/img_{}.png".format(num))