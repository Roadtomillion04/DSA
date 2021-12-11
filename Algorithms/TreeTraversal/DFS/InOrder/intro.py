'''
inOrder returns Sorted Binary Search trees
Uses call stack


                    42  (4)
                  /    \
           (2)  21     76 (6)
               / \    /  \
         (1) 18   27 52  82 (7)
                 (3) (5)


Goes to last left & adds 18
Visits previous 21 & adds it
Goes Right & adds it
Back to 47 & adds it
Visits 76 & goes away to last 52 & adds it
Adds 76
Adds 82
'''