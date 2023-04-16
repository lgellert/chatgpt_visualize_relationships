from utils.io_helpers import write_dict_to_json, load_json_to_dict
from utils.visualization_helpers import output_pyvis_html, output_nx_circular, output_nx_kamada_kawai


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

    filename = 'out/' + conversation.get_base_filename() + '.html'
    print('Writing Pyvis to ' + filename)
    output_pyvis_html(result, filename)


def output_circular(conversation, result):

    filename = 'out/' + conversation.get_base_filename() + '_circular.png'
    print('Writing NX Circular Diagram to ' + filename)
    output_nx_circular(result, filename)


def output_directed(conversation, result):

    filename = 'out/' + conversation.get_base_filename() + '_directed.png'
    print('Writing NX Directed Diagram to ' + filename)
    output_nx_kamada_kawai(result, filename)