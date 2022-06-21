import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def neuron(x, w, b):
   return sigmoid(w * x - b)

x = np.arange(-5, 5, 0.1) 

# 重み 2 バイアス -2 赤のグラフ
y = neuron(x, 2, -2) 
plt.plot(x, y, color="r") 

# 重み 0.5 バイアス 1 青のグラフ
y = neuron(x, 0.5, 1)
plt.plot(x, y, color="b") 

# 重み 2 バイアス 4 橙のグラフ
y = neuron(x, 2, 4) 
plt.plot(x, y, color="orange") 

# 赤の関数と青の関数と橙の和
# 3 * 1の隠れ層 緑のグラフ
y1 = neuron(x, 2, -2) + neuron(x, 0.5, 1) + neuron(x, 2, 4) 
plt.plot(x, y1, "g") 

plt.ylim(-0.5, 3) 
plt.show()


# 橙の重みとバイアス
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def neuron(x, w, b):
   return sigmoid(w * x - b)

x = np.arange(-5, 5, 0.1) 

# 重み 2 バイアス -2 赤のグラフ
y = neuron(x, 2, -2) 
plt.plot(x, y, color="r") 

# 重み 0.5 バイアス 1 青のグラフ
y = neuron(x, 0.5, 1)
plt.plot(x, y, color="b") 

# 重み -2 バイアス -4 橙のグラフ
y = neuron(x, -2, -4) 
plt.plot(x, y, color="orange") 

# 赤の関数と青の関数と橙の和
# 3 * 1の隠れ層 緑のグラフ
y2 = neuron(x, 2, -2) + neuron(x, 0.5, 1) + neuron(x, -2, -4) 
plt.plot(x, y2, "g") 

plt.ylim(-0.5, 3) 
plt.show()



# グラフの比較
y1 = y1
y2 = y2
fig = plt.figure(figsize=(8,5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.plot(x, y1 , "g")
ax2.plot(x, y2, "orange")
plt.show()







# import matplotlib.pyplot as plt
from matplotlib import animation, rc, gridspec
from IPython.display import HTML

fig = plt.figure()
ims = []

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def neuron(x, w, b):
   return sigmoid(w * x - b)

x = np.arange(-5, 5, 0.1) 
# X = 0.7
for i in range(10):
    Y = neuron(x, i, -2) # + neuron(x, 0.5, 1) + neuron(x, 2, 4)
    im = plt.plot(x, Y, "orange")
    ims.append(im)
ani = animation.ArtistAnimation(fig, ims, interval=500)

plt.show()