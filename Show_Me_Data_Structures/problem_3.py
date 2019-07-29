import sys

def huffman_encoding(data):
    huffman = {}
    tree = {}
    temp = '1'
    for char in data:
        huffman[char] = huffman.get(char, 0) + 1
    for num in sorted(huffman.items(), key = lambda x: x[1]):
        tree[num[0]] = temp
        temp = '0' + temp

    encoded_data = ''
    for d in data:
        encoded_data += tree[d]
    return encoded_data, tree

def huffman_decoding(data, tree):
    huffman = {}
    for char in tree:
        huffman[tree[char]] = char

    temp = ''
    decoded_data = ''
    for d in data:
        if d == '1':
            decoded_data += huffman[temp + d]
            temp = ''
        else:
            temp += d
    return decoded_data


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))