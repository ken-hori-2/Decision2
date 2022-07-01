import numpy as np
import matplotlib.pyplot as plt

# 平均 50, 標準偏差 10 の正規乱数を1,000件生成
# x = np.random.normal(50, 10, 1000)
x = np.random.normal(0.5, 0.01, 10)

# ヒストグラムを出力
plt.hist(x, bins=20, ec='black')
# filename="hist2.png"
# plt.savefig(filename)
plt.grid()
plt.show()

# plt.hist(x, bins=50, ec='black')
# # filename="hist.png"
# # plt.savefig(filename)
# plt.grid()
# plt.show()

# plt.hist(x, bins=100, ec='black')
# # filename="hist.png"
# # plt.savefig(filename)
# plt.grid()
# plt.show()