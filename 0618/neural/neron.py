# # 取りあえず仮で、空の関数を定義して、コードが実行できるようにしておく
# def summation(x,weights, bias):
#     " 重み付き線形和の関数。"
#     return 0.0

# def sigmoid(x):
#     " シグモイド関数。"
#     return 0.0

# def identity(x):
#     " 恒等関数。"
#     return 0.0


# w = [0.0, 0.0]  # 重み（仮の値）
# b = 0.0  # バイアス（仮の値）
# x = [0.05, 0.1]  # x_1とx_2の2つの特徴量

# next_x = x  # 訓練データをノードへの入力に使う

# # ---ここまでは仮の実装。ここからが必要な実装---

# # 1つのノードの処理（1）： 重み付き線形和
# node_sum = summation(next_x, w, b)

# # 1つのノードの処理（2）： 活性化関数
# is_hidden_layer = True
# if is_hidden_layer:
#     # 隠れ層（シグモイド関数）
#     node_out = sigmoid(node_sum)
# else:
#     # 出力層（恒等関数）
#     node_out = identity(node_sum)




import numpy as np
import math

A = np.array([1, 2, 3])
B = np.array([2, 4, 6])
b = [1, 2]
print(np.dot(A, B)+b)
#28

def sigmoid(x):
    """
    シグモイド関数。
    - 引数：
    x： 入力データをfloat値で指定する。
    - 戻り値：
    シグモイド関数の計算結果をfloat値で返す。
    """
    return 1.0 / (1.0 + math.exp(-x))

x = [1, 2]
# W = [[0.5, 0.6],
#     [0.7, 0.8]]
W = [1, 1]
b = 0 #[1, 2]

u = np.dot(W,x)+b
print(u)

z = sigmoid(u)
print(z)