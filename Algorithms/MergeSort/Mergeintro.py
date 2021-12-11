'''Merge is a helper function of Merge Sort it does combine two sorted lists'''

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

# This won't work because it combines only two sorted lists
# print(merge([4, 2, 6], [5, 1, 3]))

print(merge([5, 7, 9], [1, 2, 3]))
