from collections import Counter

# stores a mapping from code words to characters
encoding_map = dict()
# stores a mapping from code words to characters
decoding_map = dict()
counter = Counter()
total = 0

def construct_code(path):
    '''Construct a code from the empirical distribution found in a text file.


    :param path: The path to the text file
    '''
    global total

    with open(path) as text_file:
        for line in text_file:
            total += len(line)
            counter.update(line)

    # order list according to increasing letter counts
    ordered_list = sorted(counter.most_common(), key=lambda letter: letter[1])

    # initiate encoding_map with empty codewords
    for letter, count in ordered_list:
        encoding_map[letter] = ''

    # build the Huffman tree
    while len(ordered_list)>1:
        # take the two least likely symbols and prepend all symbols in the corresponding subtree with 0 or 1
        for letter in ordered_list[0][0]:
            encoding_map[letter] = '0' + encoding_map[letter]
        for letter in ordered_list[1][0]:
            encoding_map[letter] = '1' + encoding_map[letter]
        # create a new symbol which is the concatenation of the two least likely symbols
        # and the letter count is the sum of the two previous counts
        ordered_list[0] = (ordered_list[0][0] + ordered_list[1][0], ordered_list[0][1]+ordered_list[1][1])
        del ordered_list[1]
        # resort the list
        ordered_list = sorted(ordered_list, key=lambda letter: letter[1])

    # construct the decoding_map
    for letter, count in counter.most_common():
        decoding_map[encoding_map[letter]] = letter

construct_code('C:\\Users\\Max\\Downloads\\war_and_peace(1).txt')

def average_code_word_length():
    '''Compute the average code word length for the Huffman code

    :return: The average code word length
    '''
    avg = 0
    for key in encoding_map.keys():
        if key in counter:
            avg += ( counter[key] / total) * len(encoding_map[key])
    return(avg)

def encode(some_string):
    '''Encode a string according to a Huffman code.

    :param some_string: The string to encode
    :return: The encoding of the string
    '''
    encoded_message = ''
    for i in range(0, len(some_string)):
        encoded_message += encoding_map[some_string[i]]
    return(encoded_message)




def decode(some_code):
    '''Decode a Huffman-encoded message.

    :param some_code: The code sequence
    :return: The decoded message
    '''
    decoded = ''
    s = ''
    for i in range(0, len(some_code)):
        s += str(some_code[i])
        if s in decoding_map:
            decoded += decoding_map[s]
            s = ''
    return(decoded)


