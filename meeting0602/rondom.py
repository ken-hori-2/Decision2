import random

rondom_list1 = []

for k in range(30):
  x = random.randint(0, 1)
  rondom_list1.append(x)

print("標準ライブラリ使用")
print(rondom_list1)

print("Node数は" + str(len(rondom_list1) - 1) + "(初期値を除く)です")

# 1回目　[1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0]
# 2回目　[0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# 3回目　[0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1]


stress = 1
times = 0
print(stress * (1/2) ** times)
print((1/2) ** times)

import numpy as np
x = np.arange(1.1, 30)
print(x)