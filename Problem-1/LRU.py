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
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
