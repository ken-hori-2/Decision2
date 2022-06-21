import networkx as nx
import matplotlib.pyplot as plt
# G=nx.Graph()
# G.add_node(1,id=1000,since='December 2008')
# G.add_node(2,id=2000,since='December 2008')
# G.add_node(3,id=3000,since='January 2010')
# G.add_node(4,id=2000,since='December 2016')
# G.add_edge(1,2,since='December 2008')
# G.add_edge(1,3,since='February 2010')
# G.add_edge(2,3,since='March 2014')
# G.add_edge(2,4,since='April 2017')
# nx.draw_spectral(G,with_labels=True,node_size=3000)
# plt.show()

import networkx as nx
import matplotlib.pyplot as plt
# G=nx.Graph()
# G.add_node("{}\nNode0".format(1))
# G.add_node("{}\nNode1".format(2))
# G.add_node("{}\nNode2".format(3))
# G.add_node("{}\nNode3".format(4))
# # G.add_edge("{}\nNode0","{}\nNode1".format(1,2))
# # # G.add_edge("Node0","Node2")
# # G.add_edge("{}\nNode1","{}\nNode2".format(2,3))
# # G.add_edge("{}\nNode1","{}\nNode3".format(2,4))
# G.add_edge("1\nNode0","2\nNode1")
# # G.add_edge("Node0","Node2")
# G.add_edge("2\nNode1","3\nNode2")
# G.add_edge("2\nNode1","4\nNode3")
# nx.draw_spectral(G,with_labels=True,node_size=3000)
# plt.show()

G=nx.Graph()
G.add_node("1\nNode0")
G.add_node("2\nNode1")
G.add_node("3\nNode2")
G.add_node("4\nNode3")

G.add_edge("1\nNode0","2\nNode1",weight = 0.1)

G.add_edge("2\nNode1","3\nNode2",weight = 0.1)
G.add_edge("3\nNode2","4\nNode3",weight = 0.1)
nx.draw_spectral(G,with_labels=True,node_size=3000)
plt.show()