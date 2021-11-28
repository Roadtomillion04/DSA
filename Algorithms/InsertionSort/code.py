'''
InsertionSort is taking i + 1 element and comparing to all previous elements with while loop
t/c - O(n^2)
but for sorted/almost-sorted lists t/c is O(n)
'''

def insertion_sort(my_list):
        # starting from 2nd ele
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1 # previous ele
        while temp < my_list[j] and j > -1: # for index 1 & 0 swap the j will be -1
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

my_list = [4, 2, 6, 5, 1, 3]
print(insertion_sort(my_list))
