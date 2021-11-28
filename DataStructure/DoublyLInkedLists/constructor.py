# container class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# similar to LL
class DoublyLinkedLists:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # To see all the values in list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Adds value at end, t/c - O(1)
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    # removes the last value, t/c - O(1)
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        # for 1 ele
        if self.length == 1:
            self.head = None
            self.tail = None
        else: # more than 1 ele
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value

    # Adds value at beginning, t/c - O(1)
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    # removes first value, t/c - O(1)
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        # for 1 ele
        if self.length == 1:
            self.head = None
            self.tail = None
        else: # more than 1 ele
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value

    # returns index value, t/c - O(n)
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # Let's optimize with prev
        if index < (self.length/2): # first half
            for _ in range(index):
                temp = temp.next
        else: # second half
            temp = self.tail
            for _ in range(self.length - 1, index, -1): # reverse loop
                temp = temp.prev
        return temp

    # sets new value in given index, t/c - O(n)
    def set_value(self, index, value):
        # using existing methods
        temp = self.get(index)
        if temp: # index not out of range
            temp.value = value

    # inserts value in given index, t/c - O(n)
    def insert(self, index, value):
        if index < 0 or index > self.length: # we can insert at last
            return False
        # Taking advantage of existing methods & in get() we used >= for index
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        # for middle scenario
        new_node = Node(value)
        before = self.get(index - 1) # get previous value
        after = before.next # prev for new node

        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node

        self.length += 1

    #
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == (self.length - 1):
            return self.pop()
        # for middle scenario
        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp


my_doubly_linked_list = DoublyLinkedLists(7)
#print(my_doubly_linked_list.head.value)

my_doubly_linked_list.append(5)

# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop())

my_doubly_linked_list.prepend(1)
#my_doubly_linked_list.print_list()

#print(my_doubly_linked_list.pop_first())

#print(my_doubly_linked_list.get(2))

#print(my_doubly_linked_list.set_value(2, 6))

my_doubly_linked_list.insert(1, 9)

print(my_doubly_linked_list.remove(2),'\n')
my_doubly_linked_list.print_list()
