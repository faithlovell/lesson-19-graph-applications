# BFS Problem
import networkx as nx
import matplotlib.pyplot as plt 
#import pprint
import json

# Create the graph
G = nx.Graph()

# Add nodes to graph
# Empty Classrooms
G.add_nodes_from(['L', 'I', 'G', 'E', 'O', 'S', 'T', 'U', 'X', 'Y', 'Z'], empty=True)
# Not Empty Classrooms
G.add_nodes_from(['M', 'K', 'J', 'H', 'C', 'B', 'D', 'A', 'N', 'F', 'P', 'Q', 'R', 'V', 'W'], empty=False)

# Add edges to graph
#G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (2, 6), (1, 7), (6, 8), (3, 9), (9, 10), (3, 11), (11, 12), (11, 13), (11, 14), (5, 15), (4, 16), (2, 17), (8, 18), (8, 19), (18, 20)])
#G.add_edges_from([('A', 'B'), ('C', 'D'), ('A', 'E'), ('E', 'F'), ('A', 'G'), ('B', 'H'), ('E', 'I'), ('F', 'J'), ('F', 'K'), ('C', 'L'), ('C', 'M'), ('F', 'N'), ('D', 'O'), ('D', 'P'), ('F', 'Q'), ('A', 'R'), ('R', 'S'), ('B', 'T')])
G.add_edges_from([('M', 'L'), ('M', 'H'), ('M', 'I'), ('L', 'I'), ('L', 'K'), ('K', 'I'), ('K', 'J'), ('K', 'H'), ('J', 'I'), ('J', 'H'), ('I', 'H'), ('H', 'G'), ('H', 'C'), ('H', 'B'), ('G', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'A'), ('B', 'A'), ('A', 'D'), ('D', 'E'), ('D', 'F'), ('A', 'F'), ('A', 'E'), ('E', 'F'), ('A', 'N'), ('A', 'P'), ('N', 'O'), ('F', 'O'), ('N', 'Q'), ('F', 'P'), ('P', 'Q'), ('O', 'Q'), ('P', 'R'), ('P', 'S'), ('Q', 'S'), ('R', 'T'), ('S', 'T'), ('S', 'V'), ('S', 'Z'), ('T', 'U'), ('T', 'V'), ('V', 'X'), ('U', 'W'), ('V', 'W'), ('W', 'Y'), ('X', 'Y'), ('Y', 'Z')])
print(G.nodes.data())

'''print("Number of nodes: ", G.number_of_nodes())
print("Number of edges: ", G.number_of_edges())

print("G.nodes = ", G.nodes)
print("G.edges = ", G.edges)
print("G.degree = ", G.degree)

print(nx.descendants_at_distance(G, 'A', 2))'''
# print(nx.descendants_at_distance(G, 2, 2))

# iterate through all rooms 3 or fewer hallways away from source node to filter for empty classrooms
# color nodes based on if they're empty or not empty

# Show graph 
plt.figure()
nx.draw_networkx( G,
                pos=nx.spring_layout(G, iterations=1000),
                arrows=False, with_labels=True)
plt.show()


