# BFS Problem
import networkx as nx
import matplotlib.pyplot as plt 
#import pprint
import json

# Create the graph
G = nx.Graph()

# Add nodes to graph
#G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'])

# Add edges to graph
#G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (2, 6), (1, 7), (6, 8), (3, 9), (9, 10), (3, 11), (11, 12), (11, 13), (11, 14), (5, 15), (4, 16), (2, 17), (8, 18), (8, 19), (18, 20)])
G.add_edges_from([('A', 'B'), ('C', 'D'), ('A', 'E'), ('E', 'F'), ('A', 'G'), ('B', 'H'), ('E', 'I'), ('F', 'J'), ('F', 'K'), ('C', 'L'), ('C', 'M'), ('F', 'N'), ('D', 'O'), ('D', 'P'), ('F', 'Q'), ('A', 'R'), ('R', 'S'), ('B', 'T')])

print("Number of nodes: ", G.number_of_nodes())
print("Number of edges: ", G.number_of_edges())

print("G.nodes = ", G.nodes)
print("G.edges = ", G.edges)
print("G.degree = ", G.degree)

print(nx.descendants_at_distance(G, 'A', 2))
# print(nx.descendants_at_distance(G, 2, 2))

# iterate through all rooms 3 or fewer hallways away from source node to filter for empty classrooms
# color nodes based on if they're empty or not empty

# Show graph 
plt.figure()
nx.draw_networkx( G,
                pos=nx.spring_layout(G, iterations=1000),
                arrows=False, with_labels=True)
plt.show()


