# BFS Problem
import networkx as nx
import matplotlib.pyplot as plt 

# Create the graph
G = nx.Graph()

# Add nodes to graph
# Empty Classrooms
G.add_nodes_from(['L', 'I', 'G', 'E', 'O', 'S', 'T', 'U', 'X', 'Y', 'Z'], empty=True)
# Non-Empty Classrooms
G.add_nodes_from(['M', 'K', 'J', 'H', 'C', 'B', 'D', 'A', 'N', 'F', 'P', 'Q', 'R', 'V', 'W'], empty=False)

# Add edges to graph
G.add_edges_from([('R', 'F'), ('N', 'H'), ('V', 'Y'), ('L', 'O'), ('R', 'M'), ('B', 'W'), ('M', 'L'), ('M', 'H'), ('M', 'I'), ('L', 'I'), ('L', 'K'), ('K', 'I'), ('K', 'J'), ('K', 'H'), ('J', 'I'), ('J', 'H'), ('I', 'H'), ('H', 'G'), ('H', 'C'), ('H', 'B'), ('G', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'A'), ('B', 'A'), ('A', 'D'), ('D', 'E'), ('D', 'F'), ('A', 'F'), ('A', 'E'), ('E', 'F'), ('A', 'N'), ('A', 'P'), ('N', 'O'), ('F', 'O'), ('N', 'Q'), ('F', 'P'), ('P', 'Q'), ('O', 'Q'), ('P', 'R'), ('P', 'S'), ('Q', 'S'), ('R', 'T'), ('S', 'T'), ('S', 'V'), ('S', 'Z'), ('T', 'U'), ('T', 'V'), ('V', 'X'), ('V', 'W'), ('W', 'Y'), ('X', 'Y'), ('Y', 'Z')])

# Apply BFS to find all nodes less than 3 hallways away from Classroom A
two_away = nx.descendants_at_distance(G, 'A', 2)
one_away = nx.descendants_at_distance(G, 'A', 1)

# All classooms that are close (< 3 hallways away)
close_rooms = one_away.union(two_away)

# Filter out non-empty classrooms from Graph
empty_and_close = [node for node in close_rooms if G.nodes[node]["empty"] == True]
# Final Output: all rooms less than 3 hallways away that are empty
print("Empty Nearby Classrooms: ", empty_and_close)

# Color classroom nodes based on if they are empty (teal) or not empty (orchid color)
color_map = nx.get_node_attributes(G, "empty")
for key in color_map:
    if color_map[key] == True:
        color_map[key] = "teal"
    else:
        color_map[key] = "orchid"

classroom_colors = [color_map.get(node) for node in G.nodes()]

# Show graph of all classrooms
plt.figure()
nx.draw_networkx( G, node_size=450, node_color=classroom_colors, arrows=False, with_labels=True)
plt.show()


