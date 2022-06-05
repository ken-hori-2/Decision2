import numpy as np
import matplotlib.pyplot as plt
 
# 平均 50, 標準偏差 10 の正規乱数を1,000件生成
# x = np.random.normal(50, 10, 1000)
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
y = [0, 0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 
# ヒストグラムを出力
# plt.hist(x, range=(0, 30))
# plt.hist(x,y)
# plt.hist(y,bins=30)

plt.plot(x, y, marker = 'o')

plt.bar(x, y,color = "green")

# plt.show()

# save as png
plt.savefig('/Users/ken/Desktop/Decision-making/meeting0602/fig/figure.png')



y1 = [0, 0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y2 = [1.0, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

plt.plot(x, y1, marker="o", color = "red", linestyle = "--")
plt.plot(x, y2, marker="v", color = "blue", linestyle = ":")

plt.show()


fig = plt.figure()

# 1行2列に分割した中の1(左側)
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x, y1, marker="o", color = "red", linestyle = "--")

# 1行2列に分割した中の2(右側)
ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(x, y2, marker="v", color = "blue", linestyle = ":")

plt.show()