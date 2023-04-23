#DFS application
import networkx as nx
import matplotlib.pyplot as plt
import pprint
import json

#initialize directed graph G
G = nx.DiGraph()

#add all clubs participating into the graph
#all clubs signified by first letter of their name for readability
G.add_nodes_from(['A', 'T', 'F', 'E', 'K', 'I', 'L', 'G', 'C', 'P', 'G', 'N', 'M', 'D', 'W', 'S', 'O', 'V', 'J', 'H'])

#add directed edges between clubs who have to paint their portion before another club (no cycles!)
G.add_edges_from([('A', 'F'), ('A', 'E'), ('A', 'I'), ('A', 'L'), ('F', 'T'), ('F', 'D'), ('E', 'D'), ('E', 'P'), ('I', 'C'), ('I', 'N'), ('L', 'H'), ('T', 'K'), ('P', 'K')])
G.add_edges_from([('L', 'N'), ('D', 'K'), ('P', 'G'), ('C', 'W'), ('C', 'N'), ('N', 'O'), ('N', 'V'), ('O', 'S'), ('V', 'M'), ('O', 'J'), ('V', 'J'), ('W', 'K')])
