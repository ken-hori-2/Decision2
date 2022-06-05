from cProfile import label
import random
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sympy import re

# 戻るたびに許容が増加（ストレスの増加率が減少）


# hyper parameter
n = 30
stress = 0
#

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

rondom_list1 = []

for k in range(n):
  x = random.randint(0, 1)
  rondom_list1.append(x)

# print("標準ライブラリ使用")
print("ノードの有無:{}".format(rondom_list1))
# print("Node数は" + str(len(rondom_list1) - 1) + "(初期値を除く)です")

x = rondom_list1
judge = False
retry = False
re_count = 0
count_list = [0]*n


for j in range(10):
    for i in range(len(x)):
        if x[i] == 1:
            if stress > 1: #0:
                stress -= 1
            else: # add
                stress = 0
        else:
            # stress += 1
            stress = stress + ((9/10) ** re_count)
        
        if re_count < 1:
            stress_list[i] = stress
        elif re_count == 1:
            stress_list2[i] = stress
        elif re_count == 2:
            stress_list3[i] = stress
        elif re_count == 3:
            stress_list4[i] = stress
        elif re_count == 4:
            stress_list5[i] = stress
        elif re_count == 5:
            stress_list6[i] = stress
        elif re_count == 6:
            stress_list7[i] = stress
        elif re_count == 7:
            stress_list8[i] = stress
        elif re_count == 8:
            stress_list9[i] = stress
        elif re_count == 9:
            stress_list10[i] = stress


        if stress >= 3:
            print('結果　: Node {}個目で終了'.format(i+1))
            # judge = True
            b_num = i
            # break
            retry = True
            i = 0
            stress = 0
            re_count += 1
            count_list[re_count] = re_count
            break
        
        if i ==(len(x)-1):
            judge = True
            print('GOAL!')
            # goal_list = 
            break
    
    if judge:
        break


print("ストレスの合計:{}".format(stress))
print("ストレスの遷移1:{}".format(stress_list))
print("ストレスの遷移2:{}".format(stress_list2))
print("ストレスの遷移3:{}".format(stress_list3))
print('リトライ数:{}'.format(re_count))
print(count_list)

fig = plt.figure(figsize=(8, 3))
# xziku = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# xziku2 = [1.2,2.2,3.2,4.2,5.2,6.2,7.2,8.2,9.2,10.2,11.2,12.2,13.2,14.2,15.2,16.2,17.2,18.2,19.2,20.2,21.2,22.2,23.2,24.2,25.2,26.2,27.2,28.2,29.2,30.2]
# xziku3 = [1.4,2.4,3.4,4.4,5.4,6.4,7.4,8.4,9.4,10.4,11.4,12.4,13.4,14.4,15.4,16.4,17.4,18.4,19.4,20.4,21.4,22.4,23.4,24.4,25.4,26.4,27.4,28.4,29.4,30.4]


xziku = np.arange(1, 31)
xziku2 = np.arange(1.1, 31)
xziku3 = np.arange(1.2, 31)
# コメントアウト
# plt.plot(xziku, stress_list, marker = 'o', color = "g", alpha =0.3)
# plt.bar(xziku, stress_list,color = "#66bd63", width = 1, label = "stress")
plt.bar(xziku, stress_list, width = 1, label = "stress", alpha = 0.8)

# plt.title("stress change")
# plt.title("Goal !")
# plt.scatter(xziku, x, color ="y", label = "Node")

    # if re_count == 1:
# コメントアウト
if count_list[1] == 1:
    # plt.plot(xziku+0.1, stress_list2, marker = 'o', color = "r", alpha =0.5)
    # plt.bar(xziku+0.15, stress_list2,label = "stress", alpha =0.7)
    plt.bar(xziku, stress_list2, width = 0.9, label = "stress", alpha =0.7)
if count_list[2] == 2:
    # plt.plot(xziku+0.2, stress_list3, marker = '*', color = "y", alpha =1)
    # plt.bar(xziku+0.3, stress_list3,label = "stress", alpha =0.6)
    plt.bar(xziku, stress_list3, width = 0.8,label = "stress", alpha =0.7)
if count_list[3] == 3:
    # plt.plot(xziku+0.3, stress_list3, marker = '*', color = "b", alpha =1)
    # plt.bar(xziku+0.45, stress_list4, label = "stress", alpha =0.5)
    plt.bar(xziku, stress_list4, width = 0.7,label = "stress", alpha =0.7)
if count_list[4] == 4:
    # plt.plot(xziku+0.3, stress_list3, marker = '*', color = "m", alpha =1)
    # plt.bar(xziku+0.6, stress_list5, label = "stress", alpha =0.4)
    plt.bar(xziku, stress_list5, width = 0.6,label = "stress", alpha =0.7)
if count_list[5] == 5:
    # plt.plot(xziku+0.3, stress_list3, marker = '*', color = "black", alpha =1)
    # plt.bar(xziku+1, stress_list6, label = "stress", alpha =0.3)
    plt.bar(xziku, stress_list6, width = 0.5,label = "stress", alpha =0.7)
if count_list[6] == 6:
    # plt.plot(xziku+0.2, stress_list3, marker = '*', color = "y", alpha =1)
    # plt.bar(xziku+0.3, stress_list7, label = "stress", alpha =0.6)
    plt.bar(xziku, stress_list7, width = 0.4,label = "stress", alpha =0.7)
if count_list[7] == 7:
    # plt.plot(xziku+0.3, stress_list3, marker = '*', color = "b", alpha =1)
    # plt.bar(xziku+0.45, stress_list8, label = "stress", alpha =0.5)
    plt.bar(xziku, stress_list8, width = 0.3,label = "stress", alpha =0.7)
if count_list[8] == 8:
    # plt.plot(xziku+0.3, stress_list3, marker = '*', color = "m", alpha =1)
    # plt.bar(xziku+0.6, stress_list9, label = "stress", alpha =0.4)
    plt.bar(xziku, stress_list9, width = 0.2,label = "stress", alpha =0.7)
if count_list[9] == 9:
    # plt.plot(xziku+0.3, stress_list3, marker = '*', color = "black", alpha =1)
    # plt.bar(xziku+1, stress_list10, label = "stress", alpha =0.3)
    plt.bar(xziku, stress_list10, width = 0.1,label = "stress", alpha =0.7)
# if judge:
#     plt.bar(xziku+0.75, stress_list7, label = "stress", alpha =0.3)

plt.scatter(xziku, x, color ="b", label = "Node")
if judge:
    # plt.title("Failed {} !".format(b_num+1))
    plt.title("Goal ! リトライ数:{}".format(re_count))
plt.legend()


# x = np.arange(1, 30)

def bar_multiple(axes, xziku, stress_list):
    n = len(stress_list)
    width = 1/n #0.8 / n 
    if n % 2 == 0:
        diff = - (n / 2) * width
        for height in stress_list:
            axes.bar(xziku + diff, height, width, align='edge', label = "stress")
            diff += width
    else:
        diff = - ((n - 1) / 2) * width
        for height in  stress_list:
            axes.bar(xziku + diff, height, width, align='center', label = "stress")
            diff += width
fig, ax = plt.subplots(figsize=(8, 3))
plt.scatter(xziku, x, color ="y", label = "Node")
bar_multiple(ax, xziku, (stress_list, stress_list2, stress_list3, stress_list4, stress_list5, stress_list6, stress_list7, stress_list8))

# plt.bar(xziku, stress_list, color='b', width = 0.3, align='center', label = "stress")
# plt.bar(xziku2, stress_list2, color='r', width = 0.3,label = "stress")
# plt.bar(xziku3, stress_list3, color='g', width = 0.3,label = "stress")


if judge:
    # plt.title("Failed {} !".format(b_num+1))
    plt.title("Goal ! リトライ数:{}".format(re_count))
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