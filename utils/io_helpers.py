import json


def write_dict_to_json(dict_data, filename):
    """
    Writes python dictionary to a file in JSON format.

    :param dict_data: the dictionary to save to disk.
    :param filename: where to write the data do e.g. "somefile.json"
    :return:
    """
    json_str = json.dumps(dict_data, indent=4)

    with open(filename, 'w') as outfile:
        outfile.write(json_str)


def load_json_to_dict(filename):
    """
    Loads file contents into python dictionary.

    :param filename:
    :return:
    """
    try:
        with open(filename, 'r') as read_file:
            result = json.load(read_file)
            return result
    except FileNotFoundError:
        print('File ' + filename + ' not found. Did you run the "download" command first?')

    return False
