from matplotlib import animation
from IPython.display import HTML
import matplotlib.cm as cm  # color map
import matplotlib.pyplot as plt
import numpy as np

state_history = []
for i in range(10):
    state_history.append(1)

fig = plt.figure(figsize=(1, 1))

ax = plt.gca()
xlim= ax.set_xlim(0, 1)#ax.get_xlim()
ylim= ax.set_ylim(0, 6)#ax.get_ylim()



xedges = np.linspace(xlim[0],xlim[1],7)
yedges = np.linspace(ylim[0],ylim[1],7)
xedges,yedges

#np.histogram2dでヒストグラムデータを求める。Hが各区画における頻度のデータとなる。
# H, xedge, yedge = np.histogram2d(X[:i], Y[:i],bins=(xedges, yedges))

fig, axes = plt.subplots(ncols=2,figsize=(6,6))
ax = axes.ravel()

def animate(i):
    '''フレームごとの描画内容'''
    # plt.cla()

    state = state_history[i]  # 現在の場所を描く
    x = 0.5  # 状態のx座標は、3で割った余り+0.5
    y = state/2 + 0.5
    # line.set_data(x, y)


    # X[i] = x
    # Y[i] = y
    
    # line1.set_data(X[:i], Y[:i])

    ax[0].plot([0.45], [0.7], marker="*", color='y', markersize=20)
    ax[0].plot([0.45], [2.2], marker="*", color='y', markersize=20)
    ax[0].plot([0.45], [3.1], marker="*", color='y', markersize=20)
    ax[0].plot([0.45], [5.1], marker="*", color='y', markersize=20)
    #ax[0].plot([0.45], [5.2], marker="*", color='y', markersize=10)

    a = True
    
    # if i<11:
    #     if a == True:
    #         yy[0]+=1
           
       
    #     for j in range(11):
                
    #             a=i-j
                
    #             if i-j>=0: #LMがあるところはさらに追加
    #                 print('{},{}:a_history={}'.format(i,j,a_history))

                    

    #                 if a_history[i]==1: ####テスト###
    #                     yy[0] += 1#0.3+a/20#1.5#a/10#
                        

    #                 if a_history[i]==2:   #様子がおかしい時
                        
    #                     yy[0] -= 1#2#(3+j*5)#1.5#a/10#
    #                     #yy[i-j] -= 0.5#1#0.3
    #                     a = False
    #                     ax[1].bar(xx,yy,color='red',ec="red")#blue
                        
               
    ax[1].bar(1,i,color='#00AAFF',ec="#0000FF")#blue

    #plt.title('i=' + str(i) + '   [ ' + str(rand+1) + ' ]')

    if np.max(i) <20:
        plt.ylim(0,20)

#　初期化関数とフレームごとの描画関数を用いて動画を作成する
anim = animation.FuncAnimation(fig, animate, frames=len(
    state_history), interval=1000, repeat=True)

#HTML(anim.to_jshtml())
plt.show()