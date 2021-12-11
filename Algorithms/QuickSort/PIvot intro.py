'''
Pivot is a helper function for quickSort
It returns the swap index for quickSort
'''

def swap(my_list:list, index1:int, index2:int):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list:list, pivot_index:int, end_index:int) -> int:
    swap_index:int = 0
                  # we don't wanna check same ele again
    for i in range(pivot_index + 1, end_index + 1): # we want to include the end one
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            # swapping i and swap index values
            swap(my_list, swap_index, i)

    # At end of for loop swap index will be a middle
    swap(my_list, pivot_index, swap_index) # To take 4 to the middle
    return swap_index

# This works when 4 is at beginning
my_list:list = [4, 6, 1, 7, 3, 2, 5]
print(pivot(my_list, 0, 6))

'''
It pushes lower elements in left & higher ele in right
And returns the index of 4
The reason is when we run quick sort 
In left we take from (0 to swap_index)
In right we take from (swap_index + 1 to end)
As 4 is already at middle
'''
