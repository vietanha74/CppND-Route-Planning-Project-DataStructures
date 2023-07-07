## HUFFMAN ##
I implement huffman coding by Binary tree , frequency table and priority queue
    - Binary tree to store combined node. If huffman node has character is leaf node otherwise is huffman node.
    - Frequency table is a director it store character and frequency of it .
    - priority queue store node made from Frequency table , it server min-heap process.

### Run time complexity ###
    1. Building the Frequency Table:
        - Frequency table takes O(n) time, where n is the length of the input data.
    2. Building the Huffman Tree:
        - Priority queue of HuffmanNode objects takes O(n) time, as each character in the frequency table is processed once.
        - The while loop for combining nodes The while loop for combining nodes 
    3. Generating Huffman Codes:
        - The while loop for combining nodes 
    4. Encoding the Data:
        - Takes O(k) time, where k is the length of the encoded message.
    5. Decoding the Data:
        - Takes O(j) time, where k is the length of the encoded message.

 => All operator take : O(n log n)       
### Space complexity ###
    1. Frequency Table the frequency table would have a size of O(n), where n is the length of the input data.
    2. Priority Queue (Min-Heap) the space complexity is O(n).
    3. Building the Huffman Tree the space complexity is O(n).
    4. Codes Dictionary the space complexity is O(n).
    5. Encoded/Decoded Data the space complexity is O(n).

=> All operator take : O(n)
        
  
