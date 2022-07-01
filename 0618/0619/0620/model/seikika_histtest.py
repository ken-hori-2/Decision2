import numpy as np
import matplotlib.pyplot as plt
data=[1,2,2,3,3,3,4,4,4,4]
# 正規化されたヒストグラムを計算する
hist, edges = np.histogram(data, density=True)
w = edges[1] - edges[0]
hist = hist * w
# グラフにプロット
plt.bar(edges[:-1], hist, w)
# 正規化されていることを確認
print( sum(hist) )