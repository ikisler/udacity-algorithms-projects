def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    length = len(input_list)
    right = length - 1
    left = 0

    last = input_list[right]
    first = input_list[left]

    while left <= right:
        center = (left + right) // 2
        if number == input_list[center]:
            return center
        elif center+1 < length and input_list[center+1] < input_list[center]:
            # Start of a sequence -- see if this is the right direction
            if input_list[center+1] <= number <= last:
                left = center + 1
                right = len(input_list) - 1
                first = input_list[center+1]
            elif first >= number and number <= input_list[center]:
                left = 0
                right = center - 1
                last = input_list[center-1]
            else:
                # Number is not in either sequence
                return -1
        elif center-1 > 0 and input_list[center-1] > input_list[center]:
            # End of a sequence
            if input_list[center-1] >= number >= first:
                left = 0
                right = center - 1
                last = input_list[center-1]
            elif input_list[center] <= number <= last:
                left = center + 1
                right = len(input_list) - 1
                first = input_list[center+1]
            else:
                return -1
        elif input_list[center] > number:
            if first > number:
                left = center + 1
            else:
                right = center - 1
        elif input_list[center] < number:
            if last < number:
                right = center - 1
            else:
                left = center + 1
    return -1

def binary_search(arr, left, right, number):
    while left <= right:
        center = left + (right - left) // 2
        if arr[center] < number:
            left = center + 1
        elif arr[center] > number:
            right = center - 1
        else:
            return center
    return -1

def regular_binary_search(arr, number):
    left = 0
    right = len(arr) - 1

    while left <= right:
        center = (left + right) // 2
        if arr[center] > number:
            left = center + 1
        elif arr[center] < number:
            right = center - 1
        else:
            return center
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

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


test_function([[10,11,1,2,3,4,5,6,7,8,9], 10])
test_function([[10,11,0,1,2,3,4,5,6,7,8,9], 8])
