'''
In mergeSort we gonna write a code that
1. Breaks lists in half
2. Base case: when len(list) is 1
3. Uses merge() to put lists together
'''

def merge(list1:list, list2:list) -> list:
    combined:list = []
    # pointers
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    # Either one of the list going to be non-empty so
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list1):
        combined.append(list2[j])
        j += 1

    return combined


# using recursion
def merge_sort(my_list:list) -> list:
    if len(my_list) == 1: # Base case
        return my_list

    # Break my_list into half
    mid:int = len(my_list)//2 # for odd
    left:list = my_list[:mid]
    right:list = my_list[mid:]

    # As merge works for only sorted lists
    # So we run mergeSort again for left & right
    # until it reaches len is 1
    # when at len(1) the merge will return combined version of left & right
                 # gets 3              gets 2
    return merge(merge_sort(left), merge_sort(right))

print(merge_sort([3, 2, 1, 4]))

'''
space complexity - O(n) as we combining again the broken lists
time complexity: 
O(n) for merge as it checks every element
O(log n) for mergeSort(divide and conquer)
That's were we get O(n log n)
'''