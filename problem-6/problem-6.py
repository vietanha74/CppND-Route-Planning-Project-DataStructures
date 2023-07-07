class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    
    union_set = set()
    # Traverse through the first linked list and add each element to the set
    current  = llist_1.head
    while current:
        union_set.add(current.value)
        current = current.next
    # Traverse through the second linked list and add each element to the set
    current  = llist_2.head
    while current:
        union_set.add(current.value)
        current = current.next
    
    union_list = LinkedList ()
    for value in union_set:
        union_list.append(value)

    return union_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    item_set = set()
    intersection_list = LinkedList()
    # Traverse through the first linked list and add each element to the set
    current  = llist_1.head
    while current:
        item_set.add(current.value)
        current = current.next
    # Traverse through the second linked list and add each element to the set
    current  = llist_2.head
    while current:
        if current.value in item_set:
            intersection_list.append(current.value)
        current = current.next

    return intersection_list


## Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21,1]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

## Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,4,9,11,21,1,23]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))
#Expected Output:
#None
#None
## Test Case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

linked_list_3.append(5)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
#Expected Output:
#5 -> None
#None

## Test Case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

elements = [1, 2, 3, 4, 5]

for element in elements:
    linked_list_5.append(element)
    linked_list_6.append(element)

print(union(linked_list_5, linked_list_6))
print(intersection(linked_list_5, linked_list_6))
#Expected Output:
#1 -> 2 -> 3 -> 4 -> 5 -> None
#1 -> 2 -> 3 -> 4 -> 5 -> None
