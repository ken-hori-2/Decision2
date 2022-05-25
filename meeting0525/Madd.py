from cmath import pi
from unittest import result
import numpy as np
import matplotlib.pyplot as plt
import random

from numpy.core.defchararray import title
from pytest import skip
from tenacity import retry
from torch import ne
from urllib3 import Retry

# Madd_reset_0516.py　のコメントアウトを消したものが Madd_0523.py == Madd.py

# 初期位置での迷路の様子

# 図を描く大きさと、図の変数名を宣言

# # 現在地S0に緑丸を描画する
# line, = ax.plot([2.5], [3.5], marker="o", color='g', markersize=30)
fig = plt.figure(figsize=(2, 7))
ax = plt.gca()

# 状態を示す文字S0～S8を描く
plt.text(0.5, 4.5, 'Node\n(事前情報)', size=8, ha='center')
plt.text(0.5, 6.5, 'Node\n(事前情報)', size=8, ha='center')
plt.text(0.5, 8.5, 'Node\n(事前情報)', size=8, ha='center')

plt.text(0.5, 1.3, 'Node\n(事前情報)', size=8, ha='center')

plt.plot([0.5, 0.5], [0.0, 8.5],color="black")
#plt.text(4.5, 0.3, 'GOAL', ha='center')

# 描画範囲の設定と目盛りを消す設定
ax.set_xlim(0, 1)
ax.set_ylim(0, 9)
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='off', right='off', left='off', labelleft='off')

line3, = ax.plot([0.5], [1.5], marker="o", color='m', markersize=40)
line4, = ax.plot([0.5], [4.5], marker="o", color='m', markersize=40)
line5, = ax.plot([0.5], [6.5], marker="o", color='m', markersize=40)
line6, = ax.plot([0.5], [8.5], marker="o", color='m', markersize=40)

# 現在地S0に緑丸を描画する
line, = ax.plot([0.5], [0.5], marker="^", color='y', markersize=20)
line1, = ax.plot([0.5], [0.5], marker=">", color='r', markersize=20)
line2, = ax.plot([0.5], [0.5], marker=">", color='b', markersize=20)
line7, = ax.plot([0.5], [0.5], marker=">", color='g', markersize=20)



# 初期の方策を決定するパラメータtheta_0を設定

# 行は状態0～7、列は移動方向で↑、→、↓、←を表す
theta_0 = np.array([[1, np.nan, np.nan, np.nan],  # s0
                    [1, np.nan, np.nan, np.nan],  # s1
                    [1, np.nan, np.nan, np.nan],  # s2
                    [1, np.nan, np.nan, np.nan],  # s3
                    [1, 5, np.nan, np.nan],  # s4
                    [1, np.nan, np.nan, np.nan],  # s5
                    [1, 5, np.nan, np.nan],  # s6
                    [1, np.nan, np.nan, np.nan],  # s7、※ LandMark
                    [1, 5, np.nan, np.nan]  #s8
                    ])

# 方策パラメータthetaを行動方策piに変換する関数の定義


def simple_convert_into_pi_from_theta(theta):
    '''単純に割合を計算する'''

    [m, n] = theta.shape  # thetaの行列サイズを取得
    pi = np.zeros((m, n))
    for i in range(0, m):
        pi[i, :] = theta[i, :] / np.nansum(theta[i, :])  # 割合の計算

    pi = np.nan_to_num(pi)  # nanを0に変換

    return pi


# 初期の方策pi_0を求める
# pi_0 = simple_convert_into_pi_from_theta(theta_0)
[m, n] = theta_0.shape  # thetaの行列サイズを取得
# pi_0 = np.zeros((m, n))
pi_0 = np.nan_to_num(theta_0)  # nanを0に変換

# 初期の方策pi_0を表示
pi_0
print(pi_0)
PI = pi_0

# 1step移動後の状態sを求める関数を定義

state_history = [8]  # エージェントの移動を記録するリスト

num=[3,2,1]
num=[2,0,2]
D = 0

import random

List_sub = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]

SUM = 0

SUM_change = np.zeros(shape=(100))


TEST = np.zeros(shape=(500))
diff = np.zeros(shape=(500))
Diff2 = np.zeros(shape=(500))
retry_num = 0
Retry_sum = np.zeros(shape=(500))

import math

def AAA(s,depth,i,j,SUM, retry_num):
    # direction = ["up", "right", "down", "left"]

    
    if s == 8 or i > 500:
        test = np.random.choice(List_sub, 1, p=[0.05, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.05])
        TEST[i] = test 
        Diff2[i] = abs(1.0 - test)
        diff[j] = abs(1.0 - test)
        SUM += diff[j]

        if SUM >=0.5:
            print('\n疑念0.5以上')
            print('sum:{}\n'.format(SUM))
            print('j={}'.format(j))

            retry_num += 1
            s_next = 0
            depth = 0
            SUM = 0
            j = 0
            
            AAA(s_next,depth,i,j,SUM, retry_num)
        else:
            print('\n疑念0.5以下')
            # print('diff:{}'.format(diff))
            print('sum:{}\n'.format(SUM))
            print('j={} TEST = {}'.format(j,TEST))
            print('Diff2:{}'.format(Diff2))

            print('終了!!!!')
            print('state_history={}'.format(state_history))
            retry_num += 1

            excp = Exception()
            excp.value = state_history, SUM, retry_num
            raise excp

   
        
    if depth != 0 :# num[j]: #変更点　ずっと3進む
    # if depth > num[j]: #変更点　ずっと3進む
    #     # SUM += 0.1
    #     print('{}回目　num[{}]={} s={}'.format(i,j,num[j],s))
     if pi_0[s,1] == 5:
        print('{} 発見　LM !'.format(s))
        test = np.random.choice(List_sub, 1, p=[0.05, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.05])

        TEST[i] = test  
        Diff2[i] = abs(1.0 - test)
        diff[j] = abs(1.0 - test)

        SUM += diff[j]

        if SUM >= 0.5:
            print('\n疑念0.5以上')
            print('sum:{}\n'.format(SUM))
            print('j={}'.format(j))

            retry_num += 1
            s_next = 0
            depth = 0
            SUM = 0
            j = 0
            
            AAA(s_next,depth,i,j,SUM, retry_num)

        # SUM = 0 reset コメントアウト
        print('j = {}'.format(j))
        s_next = s #+ 3
        state_history.append(s_next)
        
        depth = 0
        AAA(s_next,depth,i+1,j+1,SUM, retry_num)

    
    
    s_next = s + 1  # 上に移動するときは状態の数字が3小さくなる
    state_history.append(s_next)#(s_next)

    AAA(s_next,depth+1,i+1,j,SUM, retry_num)
    

# 迷路内をエージェントがゴールするまで移動させる関数の定義
def AAA_top(s,depth):
    i = 0
    j = 0

    retry_num = 0

    SUM = 0
    try:
        AAA(s,depth,i,j,SUM, retry_num)
        return None
    except Exception as e:
        return e.value


def goal_maze(pi):
    s = 0  # スタート地点
    state_history = [8]  # エージェントの移動を記録するリスト
    state_history,SUM, retry_num = AAA_top(s,0) # s = 1
    
    return state_history,SUM, retry_num


# 迷路内をゴールを目指して、移動
state_history,SUM, retry_num = goal_maze(pi_0)

print("迷路を解くのにかかったステップ数は" + str(len(state_history) - 1) + "です")

# エージェントの移動の様子を可視化します
# 参考URL http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/
from matplotlib import animation
from IPython.display import HTML
import matplotlib.cm as cm  # color map


def init():
    '''背景画像の初期化'''
    line.set_data([], [])
    
    return (line,)

# 現在地S0に緑丸を描画する
#line1, = ax.plot([1.5], [2.5], marker="*", color='y', markersize=30)
#line2, = ax.plot([1.5], [4.0], marker="d", color='r', markersize=10)

SUM_2 = np.zeros(shape=(500))
SUM_1 = 0
SUM_3 = np.zeros(shape=(50))
j = 0
for i in range(len(state_history) - 1):  #いづれコメントアウト
    if state_history[i] == 1:
        SUM_3[j] = SUM_1
        j+=1

    Retry_sum[i] = j  # 追加 0513

    if state_history[i] == 1:
        SUM_1 = 0
    SUM_1 += Diff2[i]
    SUM_2[i] = SUM_1

    if i == len(state_history) - 2:
        SUM_2[i+1] = SUM_1
        SUM_3[j+1] = SUM_1
        Retry_sum[i+1] = retry_num

        SUM_2[i] = Diff2[i] + SUM_1

    
print('retry:{} {}'.format(Retry_sum,retry_num))


def animate(i):
    '''フレームごとの描画内容'''
    state = state_history[i]  # 現在の場所を描く
    x = 0.5  # 状態のx座標は、3で割った余り+0.5
    y = state  + 0.5

    z = Diff2[i]
    z += Diff2[i]

    plt.title('SUM[{:.0f}回目]={:.2f}\n\nΔstress={:.2f}'.format(Retry_sum[i], SUM_2[i], Diff2[i]))

    if state == 4:
        line1.set_data(x+0.2,y)
    elif state == 6:
        line2.set_data(x+0.2,y)
    elif state == 8:
        line7.set_data(x+0.2,y)
    else:
        line1.set_data(0.5,-0.5)
        line2.set_data(0.5,-0.5)
        line7.set_data(0.5,-0.5)
    line.set_data(x, y)
    return (line,)


#　初期化関数とフレームごとの描画関数を用いて動画を作成する
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(
    state_history), interval=500, repeat=False)

HTML(anim.to_jshtml())
plt.show()