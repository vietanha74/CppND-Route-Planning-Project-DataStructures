import heapq

class HuffmanNode:
    def __init__(self,char,freq) -> None:
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(message):
    
    frequency_table = {}
    for char in message:
        if char in frequency_table:
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1
    
    priority_queue = []
    for char,freq in frequency_table.items():
        node = HuffmanNode(char,freq)
        priority_queue.append(node)

    priority_queue.sort(key=lambda x:x.freq) 

    while len(priority_queue) > 1:
        left = priority_queue.pop(0)
        right = priority_queue.pop(0)
        combined_freq = left.freq + right.freq
        combined_node = HuffmanNode(None,combined_freq)
        combined_node.left = left
        combined_node.right = right
        priority_queue.append(combined_node)
        priority_queue.sort(key=lambda x:x.freq) 

    return priority_queue[0]

def generate_codes(node, code, codes):
    if node is None:
        return
    if node.char:
        codes[node.char] = code
    else:
        generate_codes(node.left, code + '0', codes)
        generate_codes(node.right, code + '1', codes)

def huffman_encoding(data):
    root = build_huffman_tree(data)
    codes = {}
    generate_codes(root, '', codes)

    encoded_data = ''
    for char in data:
        if char in codes:
            encoded_data += codes[char]

    return encoded_data, root

def huffman_decoding(encoded_message, huffman_tree):
    decoded_message = ""
    current_node = tree
    for bit in encoded_message:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char:
            decoded_message += current_node.char
            current_node = tree
    return decoded_message


# Example usage
a_great_sentence = "The bird is the word"
encoded_data, tree = huffman_encoding(a_great_sentence)
decoded_message = huffman_decoding(encoded_data, tree)
print("Decoded message:", decoded_message)
