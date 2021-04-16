def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    left = 0
    right = len(input_list) - 1

    first = input_list[left]
    last = input_list[right]

    while left <= right:
        center = (left + right) // 2
        if number == input_list[center]:
            return center
        elif input_list[center] > number:
            if first > number:
                # Usually we'd want to search the left half of the array
                # But if the left most value is bigger than the number we have, then
                # search in the other direction
                left = center + 1
                first = input_list[center + 1] # Reset the first value to our new one
            else:
                right = center - 1
        elif input_list[center] < number:
            if last < number:
                right = center - 1
                last = input_list[center - 1]
            else:
                left = center + 1
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Test when the rotation point is in the center
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])

# Test when number is not in array
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Test when the rotation point is way off to one side (so just one or two elements, then another sequence starts)
test_function([[10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10])
test_function([[10, 11 , 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8])

# Test when array hasn't been rotated at all (regular binary search in this case)
test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7])

