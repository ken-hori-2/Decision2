def perceptron(x1, x2):
	w1 = 5		#任意の値を代入
	w2 = 5		#任意の値を代入
	theta = 8	#任意の値を代入
	sum = x1*w1+x2*w2
	if sum <= theta:
		return 0
	else:
		return 1

print("perceptron = {}".format(perceptron(1, 1)))

import numpy as np
import matplotlib.pyplot as plt

# 0618 neural network # ニューロンの発火
x = np.arange(-5, 5, 0.1)
################# MODEL ####################
# 仮の訓練データ 重みとバイアスの初期値
X = 0.6  # 特徴量
X2 = 3
weights = 0.5
weights2 = 1/6
# weights = [1, 1]
biases = 0
################# MODEL ####################

# モデルを定義
model = (X, weights, biases)
model2 = (X2, weights2, biases)

def sigmoid(x):
    return 1/(1+np.exp(-x))
def step(x):
  return 1.0 * (x >= 0.0)

def activation(X, w, b):
    u = np.dot(X, w) + b
    print("u = {}".format(u))
    return sigmoid(u), step(u)

y = activation(*model)
# print("z = {}".format(y))

# plt.plot(x, y, "g")
# plt.show()

y2 = activation(*model2)
print("z2 = {}".format(y2))



import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def neuron(x, w, b):
   return sigmoid(w * x - b)

x = np.arange(-5, 5, 0.1) 

# 重み 1 バイアス 0 赤のグラフ
y = neuron(x, 1, 0) 
plt.plot(x, y, color="r") 

# 重み 0.3 バイアス 0 青のグラフ
y = neuron(x, 0.3, 0)
plt.plot(x, y, color="b") 

# 赤の関数と青の関数と橙の和
# 3 * 1の隠れ層 緑のグラフ
y1 = neuron(x, 1, 0) * neuron(x, 0.3, 0) 
plt.plot(x, y1, "orange") 

plt.ylim(-0.5, 3) 
plt.show()