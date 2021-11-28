'''LL, DLL, Trees are all form of graph with limitations

A node in graph is vertex
The two nodes connected to each called vertices
The connection is also called Edge
A connection also can have weights
                                                 \ | /
A vertex can have infinite connections like      - 4 -

A connection b/w two vertices can be one-direction(->, <-)/bidirectional(--)

We can use adjacency matrix or adjacency lists to store graphs

adjacency matrix is          A B C
                          A  0 1 1      for   A
                          B  1 0 1          /  \
                          C  1 1 0         B __ C

As we have to store zeros, for a big graph it is not efficient
space complexity is O(|V|^2) vertex square

adjacency list is     {
                        "A" : [B, C],
                        "B" : [A, C],
                        "C" : [A, B]
                       }

We store inside dictionary
space complexity is O(|V| + |E|) vertex + connection
'''