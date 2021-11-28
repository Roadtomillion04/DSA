'''
Bubble sort is swapping of greater than elements
t/c - O(n^2) we need two loops
'''

def bubble_sort(my_list):
          # as index starts from 0
    for i in range(len(my_list) - 1, 0, -1): # outer loop waits until inner loop finished
        for j in range(i): # inner loop
            print(i, j)
            # swap process
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                # basically re-indexing
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list

my_list = [4, 2, 6, 5, 1, 3, 2]
print(bubble_sort(my_list))
