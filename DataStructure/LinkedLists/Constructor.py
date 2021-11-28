'''Lets create a container class for new nodes'''
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None # you can also create attributes like this

class LinkedList():
    def __init__(self, value):
        self.value = value
        new_node = Node(value) # you can also create variables inside constructor
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
            self.tail = new_node
        self.length += 1

    # removes and returns the last element, t/c - O(n)
    def pop(self):
        if self.length == 0: # for no element
            return None

        temp = self.head
        pre = self.head
        while temp.next: # stops at last node
            pre = temp # stops at last before node
            temp = temp.next
        self.tail = pre
        self.tail.next = None # pre has next of temp
        self.length -= 1
        # for one element scenario we have to remove both tail & head
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value # remember you have to return the entire node, not like this for testing

    # Adds value at beginning, t/c - O(1)
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    # removes & returns the first value, t/c - O(1)
    def pop_first(self):
        if self.length == 0: # for no items
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None # As it has next for new head
        self.length -= 1
        if self.length == 0: # for 1 ele
            self.tail = None
        return temp.value

    # returns value of the index, t/c - O(n)
    def get(self, index):
        if index < 0 or index >= self.length: # check validation
            return None
        temp = self.head # we should not disturb the original head
        for _ in range(index): # that many times the temp will move
            temp = temp.next
        return temp

    # sets new value in given index, t/c - O(n)
    def set_value(self, index, value):
        temp = self.get(index) # we can call method inside the method
        # returns none or node
        if temp:
            temp.value = value # changing the existing value to new

    # inserts a value at given index, t/c - O(n) as using get()
    def insert(self, index, value):
        if index < 0 or index > self.length: # we can insert at last
            return False
        # Taking advantage of existing methods & in get() we used >= for index
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        # append & prepend calls it
        new_node = Node(value)
        temp = self.get(index - 1) # because the next should point inserted value
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

    # removes value of given index, t/c - O(n) as using get()
    def remove(self, index):
        if index < 0 or index >= self.length: # index starts from 0
            return None
        # Taking advantage of existing methods
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        # for middle scenario
        prev = self.get(index - 1)
        temp = prev.next # more efficient i.e constant time O(1)
        prev.next = temp.next
        temp.next = None # break the pointer
        self.length -= 1
        return temp

    # reversing, t/c - O(n)
    def reverse(self):
        # Assign the variables
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        # iteration
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = LinkedList(1)
#print(my_linked_list.head.value)

my_linked_list.append(2)
#my_linked_list.print_list()

'''# 2 ele
print(my_linked_list.pop())
# 1 ele
print(my_linked_list.pop())
# 0 ele
print(my_linked_list.pop())
'''

#my_linked_list.prepend(5)
#my_linked_list.print_list()

'''
# 2 ele
print(my_linked_list.pop_first())
# 1 ele
print(my_linked_list.pop_first())
# 0 ele
print(my_linked_list.pop_first())
'''

#print(my_linked_list.get(1))

#print(my_linked_list.set_value(index=1, value=7))
#my_linked_list.print_list()

my_linked_list.insert(2, 3)
#my_linked_list.print_list()

# my_linked_list.remove(index=1)
#my_linked_list.print_list()

my_linked_list.reverse()
my_linked_list.print_list()


