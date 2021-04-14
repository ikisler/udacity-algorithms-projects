def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    result = [0, 0]
    input_list = mergesort(input_list)

    for index, num in enumerate(input_list):
        if index % 2 == 0:
            result[0] = int(str(result[0]) + str(num))
        else:
            result[1] = int(str(result[1]) + str(num))
    return result

def mergesort(input_list):
    length = len(input_list)
    if length <= 1:
        return input_list
    center = length // 2
    left = mergesort(input_list[0:center])
    right = mergesort(input_list[center:])
    return merge(left, right)

def merge(left, right):
    result = []
    right_len = len(right)
    left_len = len(left)
    result_len = left_len + right_len
    result_index = 0
    left_index = 0
    right_index = 0

    while result_index < result_len and right_index < right_len and left_index < left_len:
        if left[left_index] < right[right_index]:
            result.append(right[right_index])
            right_index += 1
        else:
            result.append(left[left_index])
            left_index += 1
        result_index += 1

    if left_index < left_len:
        result.extend(left[left_index:])
    elif right_index < right_len:
        result.extend(right[right_index:])
    return result

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail", output)

# Basic tests that were already included
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Test when empty array
test_function([[], [0, 0]])

# Test array containing just zeroes
test_function([[0, 0, 0], [0, 0]])

# Test array with duplicate numbers
test_function([[4, 4, 4, 4, 4, 4], [444, 444]])

# Test array of length 1
test_function([[1], [1, 0]])

