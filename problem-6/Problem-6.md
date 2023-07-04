## UNION LIST ##
    Union : Traversing the first linked list, traversing the second linked list . Iterate through the unique elements then Append each element to the union_list.
    Intersection : 
        - Traverse through the first linked list, Add the value of each node to the item_set.
        - traverse through the first linked list, Check if the value of each node exists in the item_set
            => If the value is present, it means it is an intersecting element, so append it to the intersection_list.
            
### Run time complexity ###
Union Function:

1. Traversing the first linked list: O(N1), where N1 is the number of nodes in the first linked list.
2. Traversing the second linked list: O(N2), where N2 is the number of nodes in the second linked list.
3. Creating the union linked list: O(K), where K is the number of unique elements in the set.
=> All operation take is O(N1 + N2 + K).

Intersection Function:

1. Traversing the first linked list: O(N1), where N1 is the number of nodes in the first linked list.
2. Traversing the second linked list and checking for intersection: O(N2), where N2 is the number of nodes in the second linked list.
3. Creating the intersection linked list: O(K), where K is the number of common elements in the sets.
=> All operation take is O(N1 + N2 + K).

### Space complexity ###
1. Union Function: space complexity of the union function is O(N).Where N is the total number of elements in both linked lists combined.
2. Intersection Function: 
    - Set to store unique elements: O(N1), where N1 is the number of nodes in the first linked list
    - Linked list to store the intersection: O(K), where K is the number of common elements in the sets.
    - space complexity of the intersection function is O(N1 + K).
