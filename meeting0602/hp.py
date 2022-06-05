import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import stats

import numpy as np
import matplotlib.pyplot as plt


# 行は状態0～7、列は移動方向で↑、→、↓、←を表す
theta_0 = np.array([[1, 7, np.nan, np.nan],  # s0
                    [1, np.nan, np.nan, np.nan],  # s1
                    [1, np.nan, np.nan, np.nan],  # s2
                    [1, 7, np.nan, np.nan],  # s3
                    [1, np.nan, np.nan, np.nan],  # s4
                    [1, 9, np.nan, np.nan],  # s5
                    [1, np.nan, np.nan, np.nan],  # s6
                    [1, np.nan, np.nan, np.nan],  # s7、※ LandMark
                    [1, np.nan, np.nan, np.nan],  # s8
                    [1, 9, np.nan, np.nan],  # s9
                    [1, np.nan, np.nan, np.nan]   # s10

                    ])

# 方策パラメータthetaを行動方策piに変換する関数の定義
[m, n] = theta_0.shape  # thetaの行列サイズを取得
pi_________sub = np.zeros((m, n))
for i in range(0, m):
        pi_________sub[i, :] = np.nansum(theta_0[i, :])  # 割合の計算


def simple_convert_into_pi_from_theta(theta):
    '''単純に割合を計算する'''

    [m, n] = theta.shape  # thetaの行列サイズを取得
    pi = np.zeros((m, n))
    for i in range(0, m):
        pi[i, :] = theta[i, :] / np.nansum(theta[i, :])  # 割合の計算

    pi = np.nan_to_num(pi)  # nanを0に変換

    return pi


# 初期の方策pi_0を求める
pi_0 = simple_convert_into_pi_from_theta(theta_0)

# 初期の方策pi_0を表示
pi_0

LM = np.nan_to_num(theta_0)  # nanを0に変換
#N = 0

# 1step移動後の状態sを求める関数を定義
LM__LM=[0]*36
LM__LM_2=[0]*36
i=0



def get_next_s(TT,TEST,pi, s, N):
    
    if TEST==True:
        s_next = s - 1
        print('Tt2 s=={}'.format(s))
    elif TEST==False:
        s_next = s + 1  # 右に移動するときは状態の数字が1大きくなる
        print('TTt3 s=={}'.format(s))
    
        if s == 8:#and TT ==False:
            s_next = s - 1
            TEST = True
            #TT =True
            print('TT s=={}'.format(s))

            
   
    if LM[s][1]==7:                      #LMが来た場合、信念が増加
        N += 1
        LM__LM[s]+=1
        print('LM:{}={}'.format(s,N))

    if LM[s][1]==9:                      #LMが来た場合、信念が増加
        #N += 1
        LM__LM[s]+=2
        print('LM:{}={}'.format(s,N))

    return s_next,N,LM__LM,LM__LM_2,TEST

# 迷路内をエージェントがゴールするまで移動させる関数の定義


def goal_maze(pi):
    s = 0  # スタート地点
    state_history = [0]  # エージェントの移動を記録するリスト
    N = 0
    TEST = False
    TT = False
    

    while (1):  # ゴールするまでループ
        next_s,N,LM__LM,LM__LM_2,TEST = get_next_s(TT,TEST,pi, s, N)
        state_history.append(next_s)  # 記録リストに次の状態（エージェントの位置）を追加

        if next_s == 10:  # ゴール地点なら終了
            
            break
        elif len(state_history)>20:
            break
        else:
            s = next_s
            
    return state_history,N,s,LM__LM,LM__LM_2


# 迷路内をゴールを目指して、移動
state_history,N,s,LM__LM,LM__LM_2 = goal_maze(pi_0)


print(state_history)
print("迷路を解くのにかかったステップ数は" + str(len(state_history) - 1) + "です")

# 利用するライブラリ
import numpy as np
from scipy.stats import beta # ベータ分布
#import matplotlib.pyplot as plt
import matplotlib.animation as animation


# データ数(試行回数)を指定
#N = 10 #100
print('LM===={}'.format(N))
LM_count = N
print('LM_count===={}'.format(LM_count))

N = (len(state_history) - 1)#8

# 推移の記録用の受け皿を初期化

print('state history={}'.format(N))

print('LM__LM====={}'.format(LM__LM))


a_history = [0]  # エージェントの移動を記録するリスト
a_history[0]=1
# 推論処理
for n in range(N): #0~9で回るが、一番初めのn=0の時にanimationでは一マス進んでいるので、LM__LM[n+1]にしている

    # 事後分布のパラメータを計算
    if LM__LM[n+1]==1:  #n+1==2 or n+1==4 or n+1==6 or n+1==8:
        
        a_history.append(1)
   
    if LM__LM[n+1]==0: #毎回少しずつ減少
        
        a_history.append(0)

    if LM__LM[n+1]==2: #毎回少しずつ減少
        
        a_history.append(2)
        

print('a_history={}'.format(a_history))



xx = [1] #1,4,8,10
yy = [0]
history = [1,0,0,1,0,1,0,0,0,1,0]
n=0

X = [0.]*1000
Y = [0.]*1000

from matplotlib import animation
from IPython.display import HTML
import matplotlib.cm as cm  # color map

fig = plt.figure(figsize=(1, 1))

ax = plt.gca()
xlim= ax.set_xlim(0, 1)#ax.get_xlim()
ylim= ax.set_ylim(0, 6)#ax.get_ylim()



xedges = np.linspace(xlim[0],xlim[1],7)
yedges = np.linspace(ylim[0],ylim[1],7)
xedges,yedges

#np.histogram2dでヒストグラムデータを求める。Hが各区画における頻度のデータとなる。
H, xedge, yedge = np.histogram2d(X[:i], Y[:i],bins=(xedges, yedges))

fig, axes = plt.subplots(ncols=2,figsize=(6,6))
ax = axes.ravel()

ax[0].grid()
ax[0].set(xlim=xlim, ylim=ylim)
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
line, = ax[0].plot([2.5], [3.5], marker="o", color='g', markersize=30)
line1, = ax[0].plot([1.5], [2.5], marker="|", alpha=0.5 ,color='r', markersize=10)

# 状態を示す文字S0～S8を描く
ax[0].text(0.5, 0.5, 'S1', size=8, ha='center')
ax[0].text(0.5, 1.0, 'S2', size=8, ha='center')
ax[0].text(0.5, 1.5, 'S3', size=8, ha='center')
ax[0].text(0.5, 2.0, 'S4', size=8, ha='center')
ax[0].text(0.5, 2.5, 'S5', size=8, ha='center')
ax[0].text(0.5, 3.0, 'S6', size=8, ha='center')
ax[0].text(0.5, 3.5, 'S7', size=8, ha='center')
ax[0].text(0.5, 4.0, 'S8', size=8, ha='center')
ax[0].text(0.5, 4.5, 'S9', size=8, ha='center')

ax[0].text(0.5, 5.0, 'S10', size=8, ha='center')
ax[0].text(0.5, 5.5, 'S11', size=8, ha='center')

ax[0].text(0.5, 0.3, 'START', ha='center')



X = [0.]*1000
Y = [0.]*1000


def animate(i):
    '''フレームごとの描画内容'''
    # plt.cla()

    state = state_history[i]  # 現在の場所を描く
    x = 0.5  # 状態のx座標は、3で割った余り+0.5
    y = state/2 + 0.5
    line.set_data(x, y)


    X[i] = x
    Y[i] = y
    
    line1.set_data(X[:i], Y[:i])

    ax[0].plot([0.45], [0.7], marker="*", color='y', markersize=20)
    ax[0].plot([0.45], [2.2], marker="*", color='y', markersize=20)
    ax[0].plot([0.45], [3.1], marker="*", color='y', markersize=20)
    ax[0].plot([0.45], [5.1], marker="*", color='y', markersize=20)
    #ax[0].plot([0.45], [5.2], marker="*", color='y', markersize=10)

    a = True
    
    if i<11:
        if a == True:
            yy[0]+=1
           
       
        for j in range(11):
                
                a=i-j
                
                if i-j>=0: #LMがあるところはさらに追加
                    print('{},{}:a_history={}'.format(i,j,a_history))

                    

                    if a_history[i]==1: ####テスト###
                        yy[0] += 1#0.3+a/20#1.5#a/10#
                        

                    if a_history[i]==2:   #様子がおかしい時
                        
                        yy[0] -= 1#2#(3+j*5)#1.5#a/10#
                        #yy[i-j] -= 0.5#1#0.3
                        a = False
                        ax[1].bar(xx,yy,color='red',ec="red")#blue
                        
               
        ax[1].bar(xx,yy,color='#00AAFF',ec="#0000FF")#blue

    #plt.title('i=' + str(i) + '   [ ' + str(rand+1) + ' ]')

    if np.max(yy) <20:
        plt.ylim(0,20)

#　初期化関数とフレームごとの描画関数を用いて動画を作成する
anim = animation.FuncAnimation(fig, animate, frames=len(
    state_history), interval=1000, repeat=True)

#HTML(anim.to_jshtml())
plt.show()
