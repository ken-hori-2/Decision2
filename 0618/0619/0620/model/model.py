# #numpy,scipy.statsからnorm,math,matplotlib.pyplotをインポート！
# import numpy as np
# from scipy.stats import norm
# import math
# import matplotlib.pyplot as plt

# #0から100まで、0.01間隔で入ったリストXを作る！
# # X = np.arange(0,100,0.1)
# X = np.arange(0,1,0.01)
# #確率密度関数にX,平均50、標準偏差20を代入
# # Y = norm.pdf(X,50,20)
# Y = norm.pdf(X,0.5,0.1)

# x = np.random.normal(0.5, 0.1, 10)

# #x,yを引数にして、関数の色をr(red)に指定！カラーコードでも大丈夫です！
# plt.plot(X,Y,color='orange')
# plt.hist(x, ec='black')
# plt.grid()
# plt.show()

# ベータ乱数を受理・棄却法で生成
# 目標分布（ここではベータ分布）のpdfは既知とする
# 提案分布として一様分布を使用

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from scipy.stats import uniform, beta

np.random.seed()

# 目標分布f
f = beta(a=2.7, b=6.3).pdf

# 提案分布g
# 提案分布から乱数生成するためにgvも保持
gv = uniform
g = gv.pdf

# 分布の上限を指定する定数Mを設定
# ベータ分布のpdfの上限値を指定すればベータ分布をすべて覆える
# 最大値を求めるためにベータ分布のpdfにマイナスをつけて
# 最小値問題に帰着させる
xopt = scipy.optimize.fmin(lambda x: -f(x), 0.0, disp=False)
M = f(xopt)[0]
print("M =", M)

# 受理・棄却法
Nsim = 100000

# 提案分布gからの乱数Yを生成
Y = gv.rvs(size=Nsim)

# 一様乱数UをNsim個生成
U = uniform.rvs(size=Nsim)

# Yから受理の条件を満たすサンプルXを残して残りを棄却
X = Y[U <= f(Y) / (M * g(Y))]
print(u"サンプル数: %d => %d" % (len(Y), len(X)))
print(u"実際の受理率  : %f" % (len(X) / float(len(Y))))
print(u"理論的な受理率: %f" % (1.0 / M))

# 目標分布を描画
x = np.linspace(0.0, 1.0, 1000)
y = f(x)
plt.plot(x, y, 'r-', lw=2)

# 提案分布（一様分布）を描画
y = M * uniform.pdf(x)
plt.plot(x, y, 'g-', lw=2)

# 受理した乱数の分布を描画
plt.hist(X, bins=50, ec = "black", density= True)

plt.show()