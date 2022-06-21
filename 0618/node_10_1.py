from cProfile import label
import random
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 発見するたびに許容が増加（ストレスの増加率が減少）

# hyper parameter
n = 10 # 30
stress = 0
stress_list = [0]*n
stress_list2 = [0]*n
stress_list3 = [0]*n

stress_list4 = [0]*n
stress_list5 = [0]*n
stress_list6 = [0]*n
stress_list7 = [0]*n
stress_list8 = [0]*n
stress_list9 = [0]*n
stress_list10 = [0]*n

# 閾値設定
TRIGAR = 1

# add
times = 0

Node = []

for k in range(n):
  x = random.randint(0, 1)
  Node.append(x)

# print("標準ライブラリ使用")
print("Nodeの一致度:{}".format(Node))
# print("Node数は" + str(len(Node) - 1) + "(初期値を除く)です")

# x = Node
judge = False

count_list = [0]*n

# for j in range(10):
for i in range(len(Node)):
        # if i != 0:
        if Node[i] == 1:
            # if stress > 1:
            #     stress -= 1

            # else: # add
            #     stress = 0
            times += 1
            continue
        else:
            stress += 1
            # # stress = stress + (stress * ((1/2) ** times))
            # # stress = stress + ((1/2) ** times)
            # stress = stress + ((9/10) ** times)
        
        stress_list[i] = stress

        if stress >= TRIGAR:#3:
            print('結果　: Node {}個目で終了'.format(i+1))
            b_num = i
            count_list[times] = times
            break

        if i ==(len(Node)-1):
            judge = True
            print('End !　30steps')
            break

print("ストレスの合計:{}".format(stress))
print("ストレスの遷移:{}".format(stress_list))
print("ストレスの遷移2:{}".format(stress_list2))
print("ストレスの遷移3:{}".format(stress_list3))
print('発見数:{}'.format(times))
print(count_list)
fig = plt.figure(figsize=(8, 3))
# xziku = np.arange(1, 31)
xziku = np.arange(1, n + 1)

plt.plot(xziku, stress_list, marker = 'o', color = "m", alpha =0.5)
plt.bar(xziku, stress_list,color = "#66bd63", label = "stress", alpha = 0.8)

if judge:
    # plt.title("Failed {} !".format(b_num+1))
    plt.title("End !  Node発見数:{}".format(times))
else:
    plt.title("Failed {} !  Node発見数:{}".format(b_num+1, times))

plt.scatter(xziku, Node, color ="y", label = "Node")
plt.legend()

plt.show()