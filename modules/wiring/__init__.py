import networkx as nx


def create_graph(nodes: dict) -> nx.Graph:
    # Create an empty graph
    G = nx.Graph()

    # Add edges from the dictionary values
    for node, neighbors in nodes.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor, capacity=1.0)
    return G
