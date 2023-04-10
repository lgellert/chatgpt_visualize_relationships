import networkx as nx
from matplotlib import pyplot as plt
from pyvis.network import Network


def convert_to_graph(data):
    g = nx.DiGraph()  # DiGraph for directed graph, Graph for undirected graph

    # first pass, make a node for ALL items
    for row in data:
        g.add_node(row['name'])
        for rec in row['recommendations']:
            g.add_node(rec['name'])

    # second pass, establish relationships
    for row in data:
        for rec in row['recommendations']:
            g.add_edge(row['name'], rec['name'])

    return g


def output_pyvis_html(data, filename):
    g = convert_to_graph(data)

    net = Network(notebook=True,
                  cdn_resources='remote',
                  select_menu=True)

    net.from_nx(g)
    net.write_html(filename)


def output_nx_circular(data, filename):
    g = convert_to_graph(data)
    pos = nx.circular_layout(g)

    plt.figure(1, figsize=(12, 12), dpi=72)
    nx.draw(g, pos)
    plt.show()