__author__ = 'idnm'

from __init__ import *

raw_data = read_data('input_cat.txt')
rna_string = fasta_to_list(raw_data)[0]


def compatible(letter_1, letter_2):
    if letter_1 == 'A' and letter_2 == 'U' or letter_1 == 'U' and letter_2 == 'A':
        return True
    elif letter_1 == 'C' and letter_2 == 'G' or letter_1 == 'G' and letter_2 == 'C':
        return True
    else:
        return False

sample_string = 'AUGAUC'
sample_pairing = [[0, 1], [2, 5], [3, 4]]
new_pair = 'AU'


def intermediate_subpairing(k_1, k_2, pairing):
    return [pair for pair in pairing if k_1 < pair[0] < k_2 and k_1 < pair[1] < k_2]


def all_subpairings(pairing, string):
    max_elem = len(string)
    # print 'max_elem', max_elem
    dictionary = {}
    for k_1 in xrange(-1, max_elem + 1):
        if k_1 < max_elem + 1:
            key = str(k_1) + ' ' + str(k_1 + 1)
            dictionary[key] = []
        for k_2 in xrange(k_1 + 2, max_elem + 2):
            key = str(k_1) + ' ' + str(k_2)
            dictionary[key] = intermediate_subpairing(k_1, k_2, pairing)
    return dictionary

# print all_subpairings([[0, 1]], 'AU')
# print all_subpairings([[0, 1], [2, 3], [4, 5]])
# print all_subpairings([[0, 1], [2, 3], [4, 5], [8, 9]], 'AUAUGCGAAU')[str(5) + ' ' + str(10)]


def add_pair(pair, pairing, string):
    length_s = len(string)
    letter_1 = pair[0]
    letter_2 = pair[1]
    number_1 = length_s
    number_2 = number_1 + 1
    extended_pairings = []
    subpairings = all_subpairings(pairing, string)
    # print 'string', string
    # print 'existing pairing', pairing
    # print 'pair to add', pair
    # print 'letter_1', letter_1
    # print 'letter_2', letter_2
    # print 'number_1', number_1
    # print 'number_2', number_2
    # print 'all subpairings ', subpairings

    if compatible(letter_1, letter_2):
        extended_pairings += [pairing + [[number_1, number_2]]]
        # print 'trivial pairing added, current pairings = ', extended_pairings
    # else:
    #     print 'trivial pairing failed'
    #     pass
    for k_1 in xrange(0, length_s, 2):
        if compatible(letter_2, string[k_1]):
            for k_2 in xrange(k_1 + 1, length_s, 2):
                # print 'k_1 = ', k_1, 'k_2 = ', k_2
                # print 'string letter 1', string[k_1]
                # print 'string letter 2', string[k_2]
                if compatible(letter_1, string[k_2]):
                    # print 'compatible'
                    extended_pairings += [subpairings[str(-1) + ' ' + str(k_1)] + subpairings[str(k_1) + ' ' + str(k_2)] + \
                        subpairings[str(k_2) + ' ' + str(length_s)] + [[k_2, number_1]] + [[k_1, number_2]]]
                    # extended_pairings += [intermediate_subpairing(-1, k_1, pairing) + intermediate_subpairing(k_1, k_2, pairing) + \
                    # intermediate_subpairing(k_2, len(string), pairing) + [[k_2, number_1]] + [[k_1, number_2]]]
                    # print 'extended pairings', extended_pairings
                # else:
                #     print 'not compatible'
                #     pass
    return extended_pairings

# print add_pair('UU', [], 'AAAG')
# print add_pair('UA', [[0, 1]], 'AU')


def construct_pairings(string):
    length_s = len(string)
    # print 'input string length ', length_s
    pairings = [[]]
    for k in range(length_s)[::2]:
        # print 'length count k = ', k
        pair = string[k:k+2]
        # print 'current pair to add ', pair
        new_pairings = []
        # print 'current pairings ', pairings
        for pairing in pairings:
            # print 'current pairing ', pairing
            # print 'current substring to append to ', string[:k]
            new_pairings += add_pair(pair, pairing, string[:k])
        if not new_pairings == []:
            pairings = new_pairings
        # print 'now clearing pairings'
        # print '(k + 3 - 2*len(pairing)) = ', (k + 3 - 2*len(pairing))
        # print '(len(string) - k - 1) = ', (len(string) - k - 1)
        pairings = [pairing for pairing in pairings if (k + 3 - 2*len(pairing)) <= (length_s - k - 1)]
        if pairings == []:
            pairings = [[]]
        # print 'new pairings ', pairings
    return pairings

# print len(construct_pairings('AUAUGCGC'))
print len(construct_pairings('AUAUAUAUAUAUAUAUAU'))
