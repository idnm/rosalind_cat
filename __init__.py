__author__ = 'idnm'


def fasta_to_dict(input_data_fasta):
    """ This function converts data from the FASTA format to a dictionary"""
    input_data_raw = input_data_fasta.split('>')[1:]
    input_dict = {}
    for item in input_data_raw:
        item_dict_line = item.split('\n')
        item_key = item_dict_line[0]
        item_word = ''
        for entry in item_dict_line[1:]:
            item_word += entry
        input_dict[item_key] = item_word
    return input_dict


def fasta_to_list(input_data_fasta):
    """Converts FASTA to list disregarding names"""
    in_dict = fasta_to_dict(input_data_fasta)
    out_list = []
    for key in in_dict:
        out_list += [in_dict[key]]
    return out_list


def read_data(input_txt):
    """Reads text information from input_txt"""
    input_file = open(input_txt, 'r')
    data = input_file.read()
    input_file.close()
    return data