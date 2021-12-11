class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Creating empty tree
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # inserts value in left or right, t/c - O(log n)
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        # for non empty tree
        temp = self.root
        while True: # loops until value is placed
            if new_node.value == temp.value: # duplicates
                return False
            # left
            if new_node.value < temp.value:
                if temp.left is None: # empty
                    temp.left = new_node
                    return True
                temp = temp.left # goes further left
            else: # right
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def in_order_dfs(self) -> list:
        results:list = []

        def traverse(current_node:Node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value) # This is for ascending sort
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)


print(my_tree.in_order_dfs())