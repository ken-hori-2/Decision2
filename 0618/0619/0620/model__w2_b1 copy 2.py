from statistics import mode
from turtle import shape
import matplotlib.pyplot as plt
import numpy as np
import random

# s >= b (= w*x) 0622 ver.

# パラメータ
N = 10
NODE = [1,1,1,0,0,1,0,1,0,0]
NODE = [1,1,1,0,0,0,0,0,0,0] # 0622 # 50%　つまり、0が5回来たら戻る-> 許容が大きすぎる？
# NODE = [1,1,1,1,0,0,0,0,0,0]

NODE = [1,1,0,1,0,1,0,0,0,0]

# ランダム ver.
NODE = np.zeros(shape=10)
def rand_NODE(a, b, k):
  return [random.randint(a, b) for i in range(k)]

# print("\nNODE:{}".format(NODE))
N_pre_x = np.zeros(shape=10)
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

print("\n########################")

NODE = rand_NODE(0, 1, 10)
print("\nNODE:{}".format(NODE))

N_pre_y = np.zeros(shape=N)
for i in range(N):
    if NODE[i] == 1:         # 発見率の正しいやり方
        count += 1
    N_pre_x[i] = count / (i + 1)

    N_pre_y[i] = perceptron(N_pre_x[i])
    if N_pre_y[i] == 0:
        print("y = {} Go".format(N_pre_y[i]))
    else:
        print("y = {} Back".format(N_pre_y[i]))

print("\n発見率:{}".format(N_pre_x))
print("発火の可否 : {}".format(N_pre_y))


# 確かに許容は発見率が大きくなるほど大きくなるが、許容しすぎている？
# 迷いを持ちつつ、意思決定しているというよりは、溜まり切るポイントを先延ばしにしているだけ？
# また、bをこえた迷いを持って戻るというよりは、戻ることに疑いのない状態の再現しかできていない

# NODEが半分以上ある道は正しい道と定義？

# 以下 LINE 意思決定のメモ
# 初っ端に０がくるとアウト -> 意思決定に曖昧さがない (初っ端の方で０だと、次に１だとしても発見率は50％なので、戻ってしまう)
# -> 進んだ個数が少ないほど柔軟性、曖昧性があまりない