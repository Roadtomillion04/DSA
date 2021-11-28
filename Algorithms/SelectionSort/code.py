'''
SelectionSort is swapping greater than elements but with index
t/c - O(n^2) we need two loops
'''

def selection_sort(my_list):  # 4
    for i in range(len(my_list) - 1): # because it'll be sorted on 4 iteration
        min_index = i # 0 to 5
        # stacking it with inner loop
        for j in range(i + 1, len(my_list)): # we don't wanna compare same element
            if my_list[j] < my_list[min_index]:
                min_index = j # we store the lowest value index
        # To be more efficient we don't want this process when min index don't change
        if min_index != i:
            # we swap in outer loop or two times sorting occurs with both min_index of j & i
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp

    return my_list

my_list = [4, 2, 6, 5, 1, 3]
print(selection_sort(my_list))
