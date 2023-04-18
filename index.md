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

G.add_node("One")
G.add_node("Two")

#add edges

G.add_edge("One")
G.add_edge("Two")

print("Number of nodes: ", G.number_of_nodes())
print("Number of edges: ", G.number_of_edges())

print("G.nodes = ", G.nodes)
print("G.edges = ", G.edges)
print("G.degree = ", G.degree)

#visualization: 
plt.figure(1)
nx.draw_networkx( G,
                pos=nx.spring_layout(G, iterations=1000),
                arrows=False, with_labels=True)
plt.show()

#Source: https://www.youtube.com/watch?v=CPQeSmDGiOQ

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
