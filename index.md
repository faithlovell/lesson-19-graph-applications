# School Life

**CISC320 Spring 2023 Lesson 19 - Graph Applications**

Group Members:

- Aparna Roy (aparnar@udel.edu)
- Emma Frampton (eframpt@udel.edu)
- Sakhee Desai (sakheed@udel.edu)
- Fourth member (email)

Our project's theme is school. (elaborate on project description later)

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
import matplotlib.pyplot as plt
import pprint
import json
```

# First Problem Title (for DFS)

**Informal Description**:

> **Formal Description**:
>
> - Input:
> - Output:

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]

**Setup code**:

```python

```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python

```

**Output**

```

```

**Interpretation of Results**:

---

# Finding Empty Nearby Classrooms

**Informal Description**:
A group of school students wants to find an empty classroom to be able to work on their group project together, but they don't want to have to walk too far to find one. So, the problem is to find all the empty classrooms that are less than 3 hallways away so that the students know their options.

> **Formal Description**:
> Create a map of all the classrooms in a one-story school building, with nodes representing classrooms and edges representing hallways.
> Problem: A group of students needs to find a quiet space to work on their group project, but they don't want to walk too far.
> Find all the empty classrooms that are less than 3 hallways away from their current location, Classroom A.
>
> - Input: A graph of classrooms in a one-story school building, with nodes representing classrooms and edges representing hallways.
> - Output: A list of classrooms that are empty and less than 3 hallways away from Classroom A.

**Graph Problem/Algorithm**: BFS

**Setup code**:

```python
# Create the graph
G = nx.Graph()

# Add nodes to graph
# Empty Classrooms
G.add_nodes_from(['L', 'I', 'G', 'E', 'O', 'S', 'T', 'U', 'X', 'Y', 'Z'], empty=True)
# Non-Empty Classrooms
G.add_nodes_from(['M', 'K', 'J', 'H', 'C', 'B', 'D', 'A', 'N', 'F', 'P', 'Q', 'R', 'V', 'W'], empty=False)

# Add edges to graph
G.add_edges_from([('R', 'F'), ('N', 'H'), ('V', 'Y'), ('L', 'O'), ('R', 'M'), ('B', 'W'), ('M', 'L'), ('M', 'H'), ('M', 'I'), ('L', 'I'), ('L', 'K'), ('K', 'I'), ('K', 'J'), ('K', 'H'), ('J', 'I'), ('J', 'H'), ('I', 'H'), ('H', 'G'), ('H', 'C'), ('H', 'B'), ('G', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'A'), ('B', 'A'), ('A', 'D'), ('D', 'E'), ('D', 'F'), ('A', 'F'), ('A', 'E'), ('E', 'F'), ('A', 'N'), ('A', 'P'), ('N', 'O'), ('F', 'O'), ('N', 'Q'), ('F', 'P'), ('P', 'Q'), ('O', 'Q'), ('P', 'R'), ('P', 'S'), ('Q', 'S'), ('R', 'T'), ('S', 'T'), ('S', 'V'), ('S', 'Z'), ('T', 'U'), ('T', 'V'), ('V', 'X'), ('V', 'W'), ('W', 'Y'), ('X', 'Y'), ('Y', 'Z')])

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
```

**Visualization**:

![BFS Graph](./BFS-Graph.png)

**Solution code:**

```python
# Apply BFS to find all nodes less than 3 hallways away from Classroom A
two_away = nx.descendants_at_distance(G, 'A', 2)
one_away = nx.descendants_at_distance(G, 'A', 1)

# All classooms that are close (< 3 hallways away)
close_rooms = one_away.union(two_away)

# Filter out non-empty classrooms from Graph
empty_and_close = [node for node in close_rooms if G.nodes[node]["empty"] == True]
# Final Output: all rooms less than 3 hallways away that are empty
print("Empty Nearby Classrooms: ", empty_and_close)
```

**Output**

```
Empty Nearby Classrooms:  ['S', 'G', 'E', 'O']
```

**Interpretation of Results**:
Classrooms S, G, E, and O, are both empty and also less than 3 hallways away from Classroom A. The students will now be able to easily decide from this list of classrooms where they want go to work on their group project.

---

# Finding the Shortest Cross Country Trail (for Dijkstra's)

**Informal Description**: The problem is to find the shortest path for a cross country runner from a designated start point to a given end point. The given park map provides the time taken for each trail (edge).

> **Formal Description**:
>
> - Input:
> - Output:

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]

**Setup code**:

```python
#create an empty, undirected graph
G = nx.Graph()

#add nodes

nodes = ["A","B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]

for node in nodes:
    G.add_node(node)


edges = [
    ["A", "B", 6],
    ["A", "C", 2],
    ["C", "E", 7],
    ["C", "F", 9],
    ["A", "D", 3],
    ["B", "G", 7],
    ["G", "H", 7],
    ["G", "I", 7],
    ["H", "J", 2],
    ["F", "J", 20],
    ["J", "K", 3],
    ["A", "K", 30],
    ["E", "L", 3],
    ["I", "M", 10],
    ["N", "H", 5],
    ["D", "O", 15],
    ["P", "O", 2],
    ["L", "P", 12],
    ["A", "Q", 12],
    ["B", "R", 12],
    ["A", "S", 13],
    ["T", "P", 7],
    ["L", "T", 7],
    ["A", "R", 7],
    ["S", "Q", 1],
]

for pair in edges:
    G.add_edge(pair[0], pair[1], weight = int(pair[2]))




#visualization:
#Source: https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html

pos = nx.spring_layout(G)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, width=6)
nx.draw_networkx_edges(
    G, pos, width=6, alpha=0.5, edge_color="b"
)

# node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
```

**Visualization**:

![Image goes here]("dijkstra graph.png")

**Solution code:**

```python

```

**Output**

```

```

**Interpretation of Results**:

---

# Fourth Problem Title (for Prim's/Kruskal's)

**Informal Description**:

> **Formal Description**:
>
> - Input:
> - Output:

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]

**Setup code**:

```python

```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python

```

**Output**

```

```

**Interpretation of Results**:
