from cProfile import label
import random
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# hyper parameter
n = 30
stress = 0
#

stress_list = [0]*n
rondom_list1 = []

for k in range(n):
  x = random.randint(0, 1)
  rondom_list1.append(x)

# print("標準ライブラリ使用")
print("ノードの有無:{}".format(rondom_list1))
# print("Node数は" + str(len(rondom_list1) - 1) + "(初期値を除く)です")

x = rondom_list1
judge = False

random_pm = random.randint(2,5)


for i in range(len(x)):
    if x[i] == 1:
        if stress > 1: #0:
            stress -= 1
        else: # add
            stress = 0
    else:
        stress += 1
    
    stress_list[i] = stress

    if stress >= random_pm:
        print('閾値設定 : {}'.format(random_pm))
        print('結果　: Node {}個目で終了'.format(i+1))
        judge = True
        b_num = i
        break

print("ストレスの合計:{}".format(stress))
print("ストレスの遷移:{}".format(stress_list))

fig = plt.figure(figsize=(8, 3))
xziku = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# plt.plot(xziku, stress_list, marker = 'o', color = "g")
# plt.bar(xziku, stress_list,color = "#66bd63", label = "stress")
# plt.title("stress change")

plt.plot(xziku, stress_list, marker = 'o', color = "g", alpha =0.5)
plt.bar(xziku, stress_list,color = "#66bd63", label = "stress")
# plt.title("stress change")
plt.title("Goal ! 閾値設定 : {}".format(random_pm))
plt.scatter(xziku, x, color ="y", label = "Node")
# plt.scatter(xziku, stress_list, label="label-A")
# plt.scatter(x1, y1, label="label-B")
# plt.xlabel("X-LABEL")
# plt.xlabel("Y-LABEL")

if judge:
    # x_str = 0.4
    # y_str = 0.6
    # s = "Break!"
    # ax = fig.add_subplot(1, 1, 1)
    # ax.text(x, y, s)
    # ax.grid()
    plt.title("Failed {} ! 閾値設定 : {}".format(b_num+1,random_pm))
plt.legend()
plt.show()



# fig, ax = plt.subplots()
# def update(i):
#     plt.cla()

#     if i %10 == 0:
#         node[0] += 1

#     # # rand = random.randint(0, 5)
#     # rand_y = random.randint(0, 1)
#     # # y[0] += 1
#     # # if i %5 == 0:
#     # if rand_y == 1:
#     #     # y[0] -= 4
#     #     y[0] -= 0.5 # 1
#     # else:
#     y[0] += 1 * (1 - (node[0]*0.1))
        
#     ax.bar(x,y, color=['#66bd63'])

#     plt.title('i=' + str(i))

#     if np.max(y) <100:
#         plt.ylim(0, 100)

# ani = animation.FuncAnimation(fig, update, interval = 100)
# plt.show()