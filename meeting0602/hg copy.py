from matplotlib import animation
from IPython.display import HTML
import matplotlib.cm as cm  # color map
import matplotlib.pyplot as plt
import numpy as np

state_history = []
for i in range(10):
    # if i%2==0:
    if i == 4 or i == 8:
    # if i == 5:
        state_history.append(2)
    else:
        state_history.append(1)

#np.histogram2dでヒストグラムデータを求める。Hが各区画における頻度のデータとなる。
# H, xedge, yedge = np.histogram2d(X[:i], Y[:i],bins=(xedges, yedges))

# fig = plt.figure(figsize=(2, 7))
# ax = plt.gca()
fig, axes = plt.subplots(ncols=2,figsize=(4,7))
ax = axes.ravel()

yy = [0]
def animate(i):
    '''フレームごとの描画内容'''

    # if i<11:
    yy[0]+=0.1


# for j in range(11):

#         # a=i-j

#         if i-j>=0: #LMがあるところはさらに追加
    # print('{},{}:a_history={}'.format(i,j,a_history))

    

    # if state_history[i]==1: ####テスト###
    #     yy[0] += 0.1#0.3+a/20#1.5#a/10#
    #     ax[1].bar(0.1,yy,color='#00AAFF',ec="#0000FF")#blue
        

    if state_history[i]==2:   #様子がおかしい時
        
        yy[0] -= 0.1#2#(3+j*5)#1.5#a/10#
        #yy[i-j] -= 0.5#1#0.3
        # ax[1].bar(0.1,yy,color='red',ec="red")#blue
        ax[1].bar(0.1,yy,color='white',ec="white")#blue

        yy[0] = 0
    else:
        ax[1].bar(0.1,yy,color='green',ec="green")#blue


    # if i%2==0:   #様子がおかしい時
    #     ax[1].bar(1,0,color='red',ec="red")#blue
                        
               
    # else:
        # ax[1].bar(0.1,yy,color='#00AAFF',ec="#0000FF")#blue

    # plt.title('i=' + str(i) + '   [ ' + str(i) + ' ]')
    plt.title('i=' + str(i))

    if np.max(i) <= 10:
        plt.ylim(0,5)

#　初期化関数とフレームごとの描画関数を用いて動画を作成する
anim = animation.FuncAnimation(fig, animate, frames=len(
    state_history), interval=300, repeat=True)

#HTML(anim.to_jshtml())
plt.show()