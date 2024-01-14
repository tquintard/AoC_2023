from typing import List
import re
import networkx as nx
from collections import defaultdict


def main(inputs: List[str]) -> List[str]:
    # Part 1
    nodes = defaultdict(list)
    for line in inputs:
        m = re.findall(r'\w+', line)
        nodes[m[0]] += m[1:]

    # Create an empty graph
    G = nx.Graph()

    # Add edges from the dictionary values
    for node, neighbors in nodes.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor, capacity=1.0)
    # Uses min_cut fonction of nx to find the edge the most used
    nodes = list(nodes.keys())
    node_ref = nodes[0]
    for node in nodes[1:]:
        cut_value, (L, R) = nx.minimum_cut(G, node_ref, node)
        if cut_value == 3:
            return len(L)*len(R), '!!MERRY XMAS!!'
