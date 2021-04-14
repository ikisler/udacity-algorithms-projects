def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    i = 0
    zeroes_index = 0
    twos_index = len(input_list) - 1

    while i <= twos_index:
        if input_list[i] == 0:
            # Swap this 0 to the front
            input_list[i] = input_list[zeroes_index]
            input_list[zeroes_index] = 0
            zeroes_index += 1
            i += 1
        elif input_list[i] == 2:
            # Swap this 2 to the end
            input_list[i] = input_list[twos_index]
            input_list[twos_index] = 2
            twos_index -= 1
        else:
            # Leave the ones alone, since they just take up the space left between the zeroes and twos
            i += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Base cases included with boilerplate
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Test empty array
test_function([])

# Test array containing only ones
test_function([1, 1, 1, 1, 1, 1])

# Test array containing just one element
test_function([0])

