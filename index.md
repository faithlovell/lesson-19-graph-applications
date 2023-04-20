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
G = nx.Graph()

nodes = [["A", 1, 1],["B", 1, 2],["C", 2, 1],["D", 3, 4],["E", 3, 1],["F", 3, 7],["G", 4, 7],["H", 4, 2],["I", 5, 4],["J", 5, 7],["K", 6, 2],["L", 7, 1],["M", 8, 1],["N", 7, 4],["O", 6, 5],["P", 6, 8],["Q", 7, 8],["R", 8, 2],["S", 8, 4],["T", 8, 8]]


for node in nodes:
    G.add_node(node[0], pos = (node[1], node[2]))


edges = [
    ["A", "B", 6],
    ["A", "C", 2],
    ["C", "E", 7],
    ["C", "D", 9],
    ["B", "D", 7],
    ["D", "F", 3],
    ["F", "G", 7],
    ["G", "I", 7],
    ["D", "H", 2],
    ["H", "I", 20],
    ["G", "J", 3],
    ["J", "O", 30],
    ["I", "O", 3],
    ["I", "K", 10],
    ["K", "L", 5],
    ["L", "M", 5],
    ["M", "R", 2],
    ["R", "S", 10],
    ["S", "T", 12],
    ["K", "N", 12],
    ["O", "N", 3],
    ["O", "P", 7],
    ["P", "Q", 7],
    ["Q", "T", 7],
]

for pair in edges:
    G.add_edge(pair[0], pair[1], weight = int(pair[2]))

#Drawing Graph: 

# nodes
nx.draw_networkx_nodes(G, pos = nx.get_node_attributes(G,'pos'), node_size=700)

# edges
nx.draw_networkx_edges(G, pos = nx.get_node_attributes(G,'pos'), width=6)
nx.draw_networkx_edges(G, pos = nx.get_node_attributes(G,'pos'), width=6, alpha=0.5, edge_color="b"
)

# node labels
nx.draw_networkx_labels(G, pos = nx.get_node_attributes(G,'pos'), font_size=10, font_family="sans-serif")
#
#  edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos = nx.get_node_attributes(G,'pos'), edge_labels=edge_labels)

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
def solution (G: nx.Graph) -> nx.Graph:
    solution = nx.shortest_path(G, source="A", target="T", method='dijkstra')
    length = nx.shortest_path_length(G, source="A", target="T")
    print("The shortest path from Point A to Point T is: ")
    print(solution)
    print(length)
    return solution

solution(G)

```

**Output**

```
['A', 'D', 'O', 'P', 'T']
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
