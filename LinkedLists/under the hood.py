'''List are contiguous stored in same place in memory so it has indices
   LinkedLists are non-contiguous stored in different location and no index
   LL has head and tail
   LL has pointers that points to a next node'''

# Node is a {'value': 4, 'next': None}

# This is a example how LL works
head = {
    'value': 11,
    'next':{
        'value': 7,
        'next': {
            'value': 23,
            'next':{
                'value': 7,
                'next': None
            }
        }
    }
}

print(head['next']['next']['value'])

# For LL
# print(LL.head.next.next.value)
