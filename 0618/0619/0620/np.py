from turtle import shape
import numpy as np




N = 5
X = 2

NODE = np.ones(X*N).reshape((X, N))
NODE2 = np.ones(X*N).reshape((N, X))


print(NODE)

# print("NODE: %i , NODE2: %i" %(NODE, NODE2))

print(f"NODE:\n {NODE}\nNODE2:\n {NODE2}")



test = np.zeros(shape=10)
for i in range(10):
    test[i] = i
    print("\nNODE:{}".format(test[i]))

x = 10
test2 = []
test2 = [i for i in range(x)]
print(test2)