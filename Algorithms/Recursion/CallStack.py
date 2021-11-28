'''callStack is similar to stack with functions

Example
'''
def call_three():
    print('three')

def call_two():
    call_three() # Then it calls and wait from func three() to finish
    print('two')

def call_one():
    call_two() # First it calls and wait from func two() to finish
    print('one')

call_one() # we get 3, 2, 1

'''Run debugger(step into) to get better understanding'''
