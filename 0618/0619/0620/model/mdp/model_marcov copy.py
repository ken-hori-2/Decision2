import numpy as np
import copy
import itertools
import seaborn as sns
import matplotlib.pyplot as plt

def tp(transition_probability):

    data = transition_probability
    zero = np.zeros((np.max(data)+1,np.max(data)+1))

    for i in range(len(data)-1):
        j = copy.deepcopy(i)
        j += 1
        for x, y in itertools.product(range(np.max(data)+1), range(np.max(data)+1)):
            if data[i] == x and data[j] == y:
                zero[x][y] += 1

    row_sum = np.sum(zero, axis=1).reshape((np.max(data)+1,1))
    prob    = zero / row_sum

    return prob # , data


# NODE =        [0, 1, 0, 0, 1, 0, 0, 0]
# NODE = np.array([0, 0, 0, 1, 0, 0, 1, 1, 2, 2])
# print('0 1 :{0}日, 0 2 :{1}日, 0 3 :{2}日'.format(np.count_nonzero(NODE==0), np.count_nonzero(NODE==1), np.count_nonzero(NODE==2)))
NODE = np.array([1, 0, 1, 2, 0, 1, 2, 3, 0])
print('0 0 :{0}日, 0 1 :{1}日, 0 2 :{2}日', '0 2 :{3}日'.format(np.count_nonzero(NODE==0), np.count_nonzero(NODE==1), np.count_nonzero(NODE==2), np.count_nonzero(NODE==3)))

# prob, data = tp(NODE)
print(tp(NODE))

sns.heatmap(tp(NODE), cmap='Blues', vmin=0, vmax=1, center=.5,
            square=True, cbar_kws={"shrink": .5},
            xticklabels = 1, yticklabels = 1)

plt.show()




from graphviz import Digraph

def Graphviz(data, node_label):
    states = np.max(data)+1

    g = Digraph()

    for i in range(states):
        g.node(str(i), label=node_label[i])

    edges = np.array([np.sort(np.array([np.arange(states)]*states).flatten()),
                      np.array([np.arange(states)]*states).flatten()]).T

    # edge_labels = np.round(tp(data), 2).flatten().astype('str')
    edge_labels = np.round(tp(data), 3).flatten().astype('str')

    for i, e in enumerate(edges):
        if edge_labels[i] != '0.0':
            g.edge(str(e[0]), str(e[1]), label=edge_labels[i])

    # g.view()

    return g

node_label = ['0連続', '1連続', '2連続', '3連続']
g = Graphviz(NODE, node_label)
g.view()
# plt.show()