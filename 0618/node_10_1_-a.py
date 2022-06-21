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

# 閾値設定
TRIGAR = 4 #3 #2 #1
times = 0
Node = []

judge = False
count_list = [0]*n
b_num = 0

for k in range(n):
  x = random.randint(0, 1)
  Node.append(x)

print("Nodeの一致度:{}".format(Node))
# print("Node数は" + str(len(Node) - 1) + "(初期値を除く)です")


for i in range(len(Node)):

        if Node[i] == 1:
            if stress > 1:
                stress -= 1
            else: # add
                stress = 0
            times += 1
            # continue
        else:
            stress += 1
            # # stress = stress + (stress * ((1/2) ** times))
            # # stress = stress + ((1/2) ** times)
            # stress = stress + ((9/10) ** times)
        
        
        stress_list[i] = stress
        print(stress_list)

        if stress >= TRIGAR:#3:
            print('結果　: Node {}個目で終了'.format(i+1))
            b_num = i
            count_list[times] = times
            break

        if i ==(len(Node)-1):
            judge = True
            print('End !　30steps')
            b_num = i
            break

print("ストレスの合計:{}".format(stress))
print("ストレスの遷移:{}".format(stress_list))

print('一致数:{}'.format(times))
print(count_list)
fig = plt.figure(figsize=(8, 3))
xziku = np.arange(1, n + 1)

plt.plot(xziku, stress_list, marker = 'o', color = "m", alpha =0.5)
# plt.bar(xziku, stress_list,color = "#66bd63", label = "stress", alpha = 0.5)
plt.bar(xziku, stress_list,color = "red", label = "stress", alpha = 0.5)

if judge:
    plt.title("End !  Node発見数:{}".format(times))
else:
    plt.title("trigar {} !  Node一致数 : {}".format(b_num+1, times))

plt.scatter(xziku, Node, color ="y", label = "Node")
plt.legend()

plt.show()