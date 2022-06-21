import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
# H = nx.path_graph(10)
H = nx.path_graph(3)
G.add_nodes_from(H)
G.add_edges_from([(0, 1), (1, 2)])
nx.draw(G, with_labels=True)

plt.show()


# FG = nx.Graph()
# # FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
# FG.add_weighted_edges_from([(1, 2, 0.1), (1, 3, 0.1), (2, 4, 0.1), (3, 4, 0.1)])
# for n, nbrs in FG.adj.items():
#     for nbr, eattr in nbrs.items():
#         wt = eattr['weight']
#         if wt < 0.5: print('(%d, %d, %.3f)' % (n, nbr, wt))

# print("====")
# print(FG[2])
# print(FG[1][3])

# nx.draw(FG, with_labels=True)
# plt.show()



# G = nx.Graph()
# G.add_edge(1, 2, weight=4.7 )
# G.add_edges_from([(3, 4), (4, 5)], color='red')
# G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
# G[1][2]['weight'] = 4.7
# G.edges[3, 4]['weight'] = 4.2

# print(G[4])
# print(G[2])

# nx.draw(G, with_labels=True)
# plt.show()

G = nx.Graph()
G.add_edge(1, 2, weight=1 )
G.add_edge(2, 3, weight=0.1 )
G.add_edge(3, 4, weight=1 )
# G.add_edges_from([(3, 4), (4, 5)], color='red')
# G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 1})])
# G[1][2]['weight'] = 1
# G.edges[3, 4]['weight'] = 1

print(G[4])
print(G[2])

nx.draw(G, with_labels=True)
plt.show()