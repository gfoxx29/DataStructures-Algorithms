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
    # Solution Here

    setA = set()
    setB = set()

    # Add members of both the sets A and B
    def add_sets_members(llist, sets):
        current_node = llist.head
        while current_node:
            sets.add(current_node.value)
            current_node = current_node.next

    add_sets_members(llist_1, setA)
    add_sets_members(llist_2, setB)

    result_llist = LinkedList()
    for member in setA.union(setB):
        result_llist.append(member)

    return result_llist

def intersection(llist_1, llist_2):
    # Solution Here

    setA = set()
    setB = set()

    # Add members of both the sets A and B
    def add_sets_members(llist, sets):
        current_node = llist.head
        while current_node:
            sets.add(current_node.value)
            current_node = current_node.next

    add_sets_members(llist_1, setA)
    add_sets_members(llist_2, setB)

    result_llist = LinkedList()
    for member in setA.intersection(setB):
        result_llist.append(member)
    return result_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))