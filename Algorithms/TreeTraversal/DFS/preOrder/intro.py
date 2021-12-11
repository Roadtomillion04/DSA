'''
preOrder is where we start from root node
Uses call stack

                    42  (1)
                  /    \
           (2)  21     76 (5)
               / \    /  \
         (3) 18   27 52  82 (7)
                 (4) (6)

Adds every node straight away to last left (1 to 3)
visits back to 21 and adds 27(4)
From 21 visits back to root node
Then visits right & adds 76(5)
Adds every node straight away to last left & adds 52(6)
visiting previous nodes & adding right
'''