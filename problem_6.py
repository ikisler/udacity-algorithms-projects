def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = None
    max = None
    for num in ints:
        if min == None or num < min:
            min = num

        if max == None or num > max:
            max = num
    return (min, max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail", get_min_max(l))

# Test when list contains only one element
print(get_min_max([1]))
# Returns (1, 1)

# Test when list contains only one number
print(get_min_max([1, 1, 1, 1]))
# Returns (1, 1)

# Test when list contains negative numbers
print(get_min_max([-1, -6, -3, -4, -5, -9]))
# Returns (-9, -1)

# Test when list is only zeroes
print(get_min_max([0, 0, 0, 0, 0, 0, 0]))
# Returns (0, 0)

# Test mixed set with negatives and non-negatives
print(get_min_max([1, 5, 9, -1, 100]))
# Returns (-1, 100)

# Test empty list
print(get_min_max([]))
# Returns (None, None)

