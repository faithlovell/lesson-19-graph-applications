#DFS application
import networkx as nx
import matplotlib.pyplot as plt
import pprint
import json

#initialize directed graph G
G = nx.DiGraph()

#add all clubs participating into the graph
#all clubs signified by first letter of their name for readability
G.add_nodes_from(['A', 'T', 'F', 'E', 'K', 'I', 'L', 'G', 'C', 'P', 'N', 'M', 'D', 'W', 'S', 'O', 'V', 'J', 'H', 'Z'])

#add directed edges between clubs who have to paint their portion before another club
G.add_edges_from([('A', 'F'), ('A', 'E'), ('A', 'I'), ('A', 'L'), ('F', 'T'), ('F', 'D'), ('E', 'D'), ('E', 'P'), ('I', 'C'), ('I', 'N'), ('L', 'H'), ('T', 'K'), ('P', 'K'), ('H', 'Z')])
G.add_edges_from([('N', 'Z'), ('J', 'Z'), ('L', 'N'), ('D', 'K'), ('P', 'G'), ('C', 'W'), ('C', 'N'), ('N', 'O'), ('N', 'V'), ('O', 'S'), ('V', 'M'), ('O', 'J'), ('V', 'J'), ('W', 'K')])

#function that returns the order clubs should be scheduled, by inputting a graph G
def club_schedule(G: nx.Graph):
    #checks to see if graph is valid for scheduling problem
    if nx.is_directed_acyclic_graph(G):
        #dfs topological sorting using networkx function
        return list(nx.topological_sort(G))
    else:
        print("Invalid graph, please make sure your graph is directed acyclic.")
        return None

#answer for sample graph
order = club_schedule(G)
print(order)

#topological layout (so graph is easier to read) via networkx documentation https://networkx.org/documentation/stable/auto_examples/graph/plot_dag_layout.html
for layer, nodes in enumerate(nx.topological_generations(G)):
    for node in nodes:
        G.nodes[node]["layer"] = layer

# Compute the multipartite_layout using the "layer" node attribute
pos = nx.multipartite_layout(G, subset_key="layer")
#draw nodes
nx.draw_networkx_nodes(G, pos,  node_size = 300, node_color = 'orange')
#label nodes
nx.draw_networkx_labels(G, pos)
#draw edges
nx.draw_networkx_edges(G, pos, edge_color = 'black', arrows = True)
#draw graph
plt.show()
