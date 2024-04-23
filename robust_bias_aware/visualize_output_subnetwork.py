
import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_graphml('covid19.graphml')
nx.draw(G)
plt.show()