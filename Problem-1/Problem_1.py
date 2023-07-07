class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None,None)
        self.tail = Node(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)

            #return value
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                # Evict the least recently used node (tail)
                del self.cache[self.pop_tail().key]

            new_node = Node(key,value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
    
    def _remove_node(self, node):
        next_node = node.next
        prev_node = node.prev
        #relinking next node
        next_node.prev = prev_node
        #relinking prev node
        prev_node.next = next_node

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)

    def _add_to_front(self, node):
        node_next = self.head.next
        node_next.prev = node
        #linking for node
        node.next = node_next
        node.prev = self.head
        #linking for head
        self.head.next = node

    def pop_tail(self):
        # Remove and return the tail node (least recently used)
        node = self.tail.prev
        prev_node = node.prev
        
        self._remove_node(node)
        self.tail.prev = prev_node
        return node

# Your LRUCache object will be instantiated and called as such:
# Test Case 1: Empty Cache
cache = LRUCache(5)
print("Test Case 1:")
print("Cache Capacity:", cache.capacity)
print("Get 'A':", cache.get('A'))  # Expected Output: -1 (Key not found)
cache.put('A', 1)
print("Put 'A': 1")
print("Get 'A':", cache.get('A'))  # Expected Output: 1
print()

# Test Case 2: Full Cache with Eviction
cache = LRUCache(3)
print("Test Case 2:")
print("Cache Capacity:", cache.capacity)
cache.put('A', 1)
print("Put 'A': 1")
cache.put('B', 2)
print("Put 'B': 2")
cache.put('C', 3)
print("Put 'C': 3")
print("Get 'A':", cache.get('A'))  # Expected Output: 1
cache.put('D', 4)
print("Put 'D': 4 (Evicting 'B')")
print("Get 'B':", cache.get('B'))  # Expected Output: -1 (Evicted)
print()

# Test Case 3: Large Cache and Values
cache = LRUCache(10000)
print("Test Case 3:")
print("Cache Capacity:", cache.capacity)
for i in range(10000):
    cache.put(f'Key{i}', i)
print("Put 10000 key-value pairs")
print("Get 'Key0':", cache.get('Key0'))  # Expected Output: 0
print("Get 'Key5000':", cache.get('Key5000'))  # Expected Output: 5000
print("Get 'Key9999':", cache.get('Key9999'))  # Expected Output: 9999
print()
