import numpy as np
import matplotlib.pyplot as plt

data = np.arange(0, 100).reshape(10, 10)
fig, ax = plt.subplots()
im = ax.imshow(data)
plt.colorbar(im)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 11)
y = np.linspace(0, 20, 11)
X, Y = np.meshgrid(x, y)
z = np.abs(X) + np.abs(Y)
fig, ax = plt.subplots()
im = ax.imshow(z, origin='lower', extent=(0, 20, 0, 20))
plt.colorbar(im)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 11)
y = np.linspace(0, 20, 11)
X, Y = np.meshgrid(x, y)
z = np.abs(X) + np.abs(Y)
fig, ax = plt.subplots()
im = ax.imshow(z, origin='lower', extent=(0, 20, 0, 20))
im.set_data(z * 2)   # データを2倍の値に差し替え
plt.colorbar(im)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 11)
y = np.linspace(0, 20, 11)
X, Y = np.meshgrid(x, y)
z = np.abs(X) + np.abs(Y)
fig, ax = plt.subplots()
im = ax.imshow(z, origin='lower', extent=(0, 20, 0, 20))
im.set_data(z * 2)   # データを2倍の値で入れ替え
plt.colorbar(im)
im.autoscale()  # カラーバーの最大値最小値を自動更新
plt.show()