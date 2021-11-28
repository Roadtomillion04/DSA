'''A Factorial is a best example for recursion

'''
def factorial(n):
    if n == 1: # base case
        return 1
    return n * factorial(n - 1) # recursive case
    # you have to use return or at 1 it will always return 1

print(factorial(4))
# use debugger(step into) for better understanding
