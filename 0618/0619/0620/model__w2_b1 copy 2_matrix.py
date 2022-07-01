from cProfile import label
from statistics import mode
from turtle import shape
from xmlrpc.client import TRANSPORT_ERROR
import matplotlib.pyplot as plt
import numpy as np
import random

# s >= b (= w*x) 0622 ver.

# パラメータ
N = 10 # 50 #10
X = int(input("試行回数 X : ")) #5 # 500
NODE = [1,1,1,0,0,1,0,1,0,0]
NODE = [1,1,1,0,0,0,0,0,0,0] # 50%　つまり、0が5回来たら戻る-> 許容が大きすぎる？
# NODE = [1,1,1,1,0,0,0,0,0,0]

# NODE = [1,1,0,1,0,1,0,0,0,0]

IGNITION = np.zeros(shape=X)
fire = False
non_fire = 0 # False

# ランダム ver.
# NODE = np.zeros(shape=N)
def rand_NODE(a, b, k):
  return [random.randint(a, b) for i in range(k)]

# print("\nNODE:{}".format(NODE))
# N_pre_x = np.zeros(shape=10)
N_pre_x = np.zeros(X*N).reshape((X, N))
count = 0

# for i in range(N):
#     if NODE[i] == 1:         # 発見率の正しいやり方
#         count += 1
#     N_pre_x[i] = count / (i + 1)
# print("\n発見率:{}".format(N_pre_x))

def perceptron(x1):
	w1 = 2		#任意の値を代入
	b = x1*w1

	if 1 < b:
		return 0
	else:
		return 1

print("\n##########################\nノードの総数 {} * {} セット で試験開始\n##########################".format(N, X))
count = np.zeros(shape=X)
# X = np.zeros(shape=5)
NODE = np.zeros(X*N).reshape((X, N))
# for x in range(2):
for i in range(X):
    NODE[i] = rand_NODE(0, 1, N)
    print("\nNODE:{}".format(NODE[i]))
# X[x] = NODE
    # X[i] = NODE
print("\nNODE (10列 * 5行)\nX={}".format(NODE))

# N_pre_y = np.zeros(shape=N)
N_pre_y = np.zeros(X*N).reshape((X, N))
for x in range(X):
    print("\n########################")
    print("\nNODE:{}".format(NODE[x]))
    for i in range(N):
        if NODE[x][i] == 1:         # 発見率の正しいやり方
            count[x] += 1
        N_pre_x[x][i] = count[x] / (i + 1)

        N_pre_y[x][i] = perceptron(N_pre_x[x][i])
        if N_pre_y[x][i] == 0:
            print("y = {} Go".format(N_pre_y[x][i]))
            # non_fire = True
            num = i +1     # NODEは0からではなく、1からだから + 1
        else:
            print("y = {} Back".format(N_pre_y[x][i]))
            fire = True
            num = i +1     # NODEは0からではなく、1からだから + 1
            break
    print("\n")
    if fire:
        IGNITION[x] = num # i
        fire = False
    else:
    # if non_fire:
        non_fire += 1
        IGNITION[x] =  num

    print("発見率:{}".format(N_pre_x[x]))
    print("発火の可否 : {}".format(N_pre_y[x]))

print("\n########################")
# 試行回数全部の結果 コメントアウト 0623
# print("\n発見率:{}".format(N_pre_x))
# print("発火の可否 : {}".format(N_pre_y))


# POINT? 考えること
#########################################################################

# 確かに許容は発見率が大きくなるほど大きくなるが、許容しすぎている？
# 迷いを持ちつつ、意思決定しているというよりは、溜まり切るポイントを先延ばしにしているだけ？
# また、bをこえた迷いを持って戻るというよりは、戻ることに疑いのない状態の再現しかできていない

# NODEが半分以上ある道は正しい道と定義？
#########################################################################

# x_plot = np.arange(0, X, 0.1)
x_plot = np.arange(1, X+1, 1)
# print(x_plot)
print("IGNITION:{}".format(IGNITION))
IGINITION_AVE = sum(IGNITION)/X
print("IGNITION_SUM:{}\nIGNITION_AVE:{}".format(sum(IGNITION), sum(IGNITION)/X))

print("NON_FIRE: {} 回".format(non_fire))
fig = plt.figure(figsize=(10, 5))
# plt.plot(x_plot, x_plot*2, linestyle='solid')
plt.title("Graph of ignition locations")
plt.xlabel("試行回数 X")
plt.ylabel("発火したNODE")
# plt.plot(x_plot, IGNITION, linestyle='solid')
plt.plot(x_plot, IGNITION, label = "ignition location")
# plt.plot(x_plot, IGINITION_AVE, linestyle='solid', color = "orange")
# plt.plot([0, X], [IGINITION_AVE, IGINITION_AVE], color="orange")
plt.hlines(IGINITION_AVE, 1, X, color="orange", linewidth = 3, label="average")
plt.legend()

plt.grid()
plt.show()
# num = input("input figure num : ")
# fig.savefig("/Users/ken/Desktop/Decision-making/0618/0619/0620/fig/img_{}.png".format(num))