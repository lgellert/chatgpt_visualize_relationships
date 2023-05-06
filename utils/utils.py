from utils.io_helpers import write_dict_to_json, load_json_to_dict
from utils.visualization_helpers import output_pyvis_html, output_nx_circular, \
    output_scikit_svg, convert_to_graph, get_top_centrality_nodes


def process_conversation(conversation):

    print('Getting ' + conversation.get_title() + ' Graph')
    result = conversation.collect_data()

    filename = 'out/' + conversation.get_base_filename() + '.json'
    print('Writing JSON results to ' + filename)
    write_dict_to_json(result, filename)

    return result


def load_previous_conversation_results(conversation):
    filename = 'out/' + conversation.get_base_filename() + '.json'
    return load_json_to_dict(filename)


def output_pyvis(conversation, result):

    filename = 'out/' + conversation.get_base_filename() + '_pyvis.html'
    print('Writing Pyvis to ' + filename)
    output_pyvis_html(result, filename)


def output_circular(conversation, result):

    filename = 'out/' + conversation.get_base_filename() + '_circular.png'
    print('Writing NX Circular Diagram to ' + filename)
    output_nx_circular(result, filename)


def output_svg(conversation, result):

    filename = 'out/' + conversation.get_base_filename() + '_scikit.svg'
    print('Writing SVG to ' + filename)
    output_scikit_svg(result, filename)


def output_top_nodes(conversation, result):
    g = convert_to_graph(result)
    top_centrality_nodes = get_top_centrality_nodes(g, top_n=10)

    print('Top 10 nodes found in the topic of ' + conversation.get_title() + ':')

    for i, name in enumerate(top_centrality_nodes):
        print('\t' + str(i + 1) + '. ' + name)
