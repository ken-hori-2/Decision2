from cProfile import label
from statistics import mode
from turtle import shape
from xmlrpc.client import TRANSPORT_ERROR
import matplotlib.pyplot as plt
import numpy as np
import random

# s >= b (= w*x) 0622 ver.

# model__w2_b1 copy 2_matrix.py の整理版

# PARAMETER
N = 10
X = int(input("試行回数 X : "))
IGNITION_LIST = np.zeros(shape=X)
FIRE = False
NON_FIRE = 0
DISCOVERY_RATE = np.zeros(X*N).reshape((X, N))
COUNT = np.zeros(shape=X)
NODE = np.zeros(X*N).reshape((X, N))
IGNITION_RESULT = np.zeros(X*N).reshape((X, N))



def rand_NODE(zero, one, x):
  return [random.randint(zero, one) for i in range(x)]

def perceptron(x1):
	w1 = 2
	b = x1*w1
	if 1.5 < b : # 1 < b:
		return 0
	else:
		return 1

print("\n##########################\nノードの総数 {} * {} セット で試験開始\n##########################".format(N, X))
# for i in range(X):
#     NODE[i] = rand_NODE(0, 1, N)
#     print("\nNODE:{}".format(NODE[i]))
NODE = [rand_NODE(0, 1, N) for i in range(X)]
print("\nNODE (10列 * 5行)\nX={}".format(NODE))


for x in range(X):
    print("\n########################\nNODE:{}".format(NODE[x]))
    for i in range(N):
        if NODE[x][i] == 1:         # 発見率の正しいやり方
            COUNT[x] += 1
        DISCOVERY_RATE[x][i] = COUNT[x] / (i + 1)

        IGNITION_RESULT[x][i] = perceptron(DISCOVERY_RATE[x][i])
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

    print("\n発見率:{}".format(DISCOVERY_RATE[x]))
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
# plt.show()
# num = input("input figure num : ")
# fig.savefig("/Users/ken/Desktop/Decision-making/0618/0619/0620/fig/img_{}.png".format(num))