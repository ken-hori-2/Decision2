def perceptron(x1, x2):
	w1 = 5		#任意の値を代入
	w2 = 5		#任意の値を代入
	theta = 8	#任意の値を代入
	sum = x1*w1+x2*w2
	if sum <= theta:
		return 0
	else:
		return 1

# print(perceptron(1, 1))


# 0618 neural network # ニューロンの発火

################# MODEL ####################
# 仮の訓練データ 重みとバイアスの初期値
X = [0.5, 0.3]  # x_1とx_2の2つの特徴量
weights = [[1, 2],[3, 4]]
# weights = [1, 1]
biases = 0 # []
################# MODEL ####################

# モデルを定義
model = (X, weights, biases)

import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
def step(x):
  return 1.0 * (x >= 0.0)

def activation(X, w, b):
    u = np.dot(X, w) + b
    print("u = {}".format(u))
    return sigmoid(u), step(u)

# def update(X, y, w, b, eta): # 解析的に重みの更新を行う。etaは学習率
#     a = (activation(X,w,b)-y)*activation(X,w,b)*(1-activation(X,w,b))
#     a = a.reshape(-1,1)
#     w -= eta * 1/float(len(y))*np.sum(a*X,axis=0)
#     b -= eta * 1/float(len(y))*np.sum(a)
#     return w, b


print(activation(*model))




# def step2(x):
#   return 1.0 * (x >= 3.0)

# print(step2(3))