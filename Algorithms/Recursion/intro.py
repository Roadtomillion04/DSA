'''A recursion is
 Function calls itself ...
 ... until it doesn't

 A recursion must have base case & recursive case
 or else it leads to stack overflow(continuous looping)

 An example is
 '''
import random
def open_gift_box():
    ball = random.randint(0, 1)
    if ball: # base case
        return True
    open_gift_box() # recursive case
