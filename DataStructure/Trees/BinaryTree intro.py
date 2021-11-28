'''Binary trees are unsorted
can be unstructured
each node has left and right pointers
has only one root/parent node, below nodes pointing to next are called child,
below node that don't point to next are called leaves

                4    root
              /  \
            7     6   child
           / \   / \
           3  5  8  12   leaves
'''

# Let's see about binary search trees(BST)
'''BST are sorted binary trees
can  be unstructured
The node value < root goes left
The node value > root goes right

            47
           /  \
          21   76
         /     / \
        18    52  82

Cannot have duplicates!

we have lookup(), remove() & insert() methods
  t/c  - O(log n ) for all we use divide and conquer

for worst case scenarios tree like 
            47    It's basically a linked lists
              \
               76
                 \
                  82
                    \
                    91
        
Only for this case we can't divide and conquer so t/c - O(n)

in comparison with LL and lists
lookup() & remove() are O(log n) in BST which is better than O(n) in LL and lists
but for insert() in LL & lists at worst case i.e at last we can use append() which is O(1)
better than BST which is still O(log n)
'''

