import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from pyvis.network import Network


def convert_to_graph(data):

    g = nx.Graph()

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


def get_top_centrality_nodes(g, top_n=3):

    # get centrality of nodes
    centrality = nx.degree_centrality(g)
    centrality_sorted = dict(sorted(centrality.items(), key=lambda item: item[1], reverse=True))

    # pull off the top N nodes
    top_centrality_nodes = list(centrality_sorted)[0:top_n]
    return top_centrality_nodes


def output_pyvis_html(data, filename):

    g = convert_to_graph(data)

    net = Network(notebook=True,
                  cdn_resources='remote',
                  select_menu=True)

    net.from_nx(g)
    net.write_html(filename)


def output_nx_circular(data, filename):

    plt.figure(figsize=(14, 9))
    plt.margins(0.2)

    g = convert_to_graph(data)
    top_centrality_nodes = get_top_centrality_nodes(g)

    # setup the color of the nodes
    color_list = []
    for node in g.nodes():
        if node in top_centrality_nodes:
            color_list.append('tab:blue')
            continue
        # just a regular node
        color_list.append('grey')

    # start a circular layout for the graph rendering
    pos = nx.circular_layout(g)

    # offset the node labels so they look better
    pos_attrs = {}
    for node, coords in pos.items():
        pos_attrs[node] = (coords[0] + 0.13*(-1)*np.sign(coords[0]), coords[1]+0.13*(-1)*np.sign(coords[1]))
    nx.draw_networkx_labels(g, pos=pos, font_size=10)
    nx.draw(g, node_color=color_list, pos=pos_attrs)

    # add a legend
    labels = ['3 Most Central', 'Regular Node']
    labels_color = ['tab:blue', 'grey']
    for i in range(len(labels)):
        plt.scatter([], [], label=labels[i], color=labels_color[i])
    plt.legend(loc='lower right')

    # plt.show()
    plt.savefig(filename, bbox_inches='tight')


def output_nx_kamada_kawai(data, filename):

    plt.figure(figsize=(14, 9))
    plt.margins(0.2)

    g = convert_to_graph(data)
    top_centrality_nodes = get_top_centrality_nodes(g)

    # setup the color of the nodes
    color_list = []
    for node in g.nodes():
        if node in top_centrality_nodes:
            color_list.append('tab:blue')
            continue
        # just a regular node
        color_list.append('grey')

    # start a kamada_kawai_layout layout for the graph rendering
    pos = nx.kamada_kawai_layout(g)
    nx.draw_networkx_labels(g, pos=pos, font_size=10)
    nx.draw(g, node_color=color_list)

    # add a legend
    labels = ['3 Most Central', 'Regular Node']
    labels_color = ['tab:blue', 'grey']
    for i in range(len(labels)):
        plt.scatter([], [], label=labels[i], color=labels_color[i])
    plt.legend(loc='lower right')

    # plt.show()
    plt.savefig(filename, bbox_inches='tight')