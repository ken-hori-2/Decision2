import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [80, 60, 40, 20, 5]
y2 = [20, 40, 60, 80, 95]

plt.bar(x, y1)
plt.bar(x, y2, bottom=y1)



plt.show()


label = ["A", "B", "C", "D", "E"]

plt.pie(x, labels=label)
plt.axis('equal') # 出力が楕円形になるのを防ぐため
plt.show()