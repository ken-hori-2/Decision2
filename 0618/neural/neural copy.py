def perceptron(x1, x2):
	w1 = 5		#任意の値を代入
	w2 = 5		#任意の値を代入
	theta = 8	#任意の値を代入
	sum = x1*w1+x2*w2
	if sum <= theta:
		return 0
	else:
		return 1

print(perceptron(1, 1))


# neural network # ニューロンの発火

################# MODEL ####################
# 仮の訓練データ（1件分）を準備
X = [0.05, 0.1]  # x_1とx_2の2つの特徴量
# 重みとバイアスの初期値
weights = [1, 1]
biases = 0 # []
################# MODEL ####################

# モデルを定義
model = (X, weights, biases)

y = 0.5
model2 = (X, y, weights, biases)

# コメントアウト
# X = [1, 1]
# w = [1, 1]
# b = 0

import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
def step(x):
  return 1.0 * (x >= 0.0)

def activation(X, w, b):
    u = np.dot(X,w)+b
    print("u={}".format(u))
    return sigmoid(u),step(u)

# def loss(X, y, w, b):
#     dif = y - activation(X, w, b)
#     return np.sum(dif**2/(2*len(y)),keepdims=True)

def accuracy(X, y, w, b):
    pre = predict(X, w, b)
    return np.sum(np.where(pre==y,1,0))/len(y)

def predict(X, w, b):
    result = np.where(activation(X, w, b)<(0.5, -1.0, 1.0))
    # print("predict:{}".format(result))
    return result

# def update(X, y, w, b, eta): # 解析的に重みの更新を行う。etaは学習率
#     a = (activation(X,w,b)-y)*activation(X,w,b)*(1-activation(X,w,b))
#     a = a.reshape(-1,1)
#     w -= eta * 1/float(len(y))*np.sum(a*X,axis=0)
#     b -= eta * 1/float(len(y))*np.sum(a)
#     return w, b

# print(activation(X, w, b))
print(activation(*model))

print(predict(*model))
# print(accuracy(*model2))






# def step2(x):
#   return 1.0 * (x >= 3.0)

# print(step2(3))