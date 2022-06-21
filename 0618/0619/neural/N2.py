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

# 赤の関数と青の関数の和
# 2 * 1の隠れ層 緑のグラフ
y = neuron(x, 2, -2) + neuron(x, 0.5, 1)
plt.plot(x, y, "g") 

plt.ylim(-0.5, 2) 
plt.show()