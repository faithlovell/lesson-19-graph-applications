# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:

- Aparna Roy (aparnar@udel.edu)
- Emma Frampton (eframpt@udel.edu)
- Sakhee Desai (sakheed@udel.edu)
- Fourth member (email)

Our project's theme is school.

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

# Second Problem Title (for BFS)

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
