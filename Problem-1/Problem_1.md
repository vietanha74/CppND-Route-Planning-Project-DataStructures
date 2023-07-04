## LRU CACHE ##

### Database designe###
I implement this LRU cache by Double linked List compination with HashMap. 
    - Hashmap provides efficient key lookup and insertion operation.
    - Double linked list handling adding, remove, and moving nodes base on HashMap LRU Cache.

### Run time complexity ###
1. The get() operation also has a runtime complexity of O(1) on average because it allow access to the corresponding node in the doubly linked list in constant time.
2. The put() operation also has a runtime complexity of O(1) on average it allow (insert,remove,moving) to the corresponding node in the doubly linked list in constant time.

 => All operations take O(1) 

### Space complexity ###

The space complexity of LRU cache is sum of Cache Dictionary + Double linked list 
1. Cache Dictionary has a space complexity is O(capacity). Where capacity is max number Cache can hold .
2. Double linked list  has a space complexity is O(n). Where n is number of items in cache.

=> All operations take O(capacity + n) 