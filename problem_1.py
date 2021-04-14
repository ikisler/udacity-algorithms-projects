def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Uses the Babylonian method descibed here:
    # https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method

    # Edge case
    if number < 0:
        return None

    guess = number
    quotient = 1 # if number is 0 or 1, skip the `while` and just return that value

    while quotient < guess:
        guess = (guess + quotient) // 2
        quotient = number / guess
    return guess

# Given cases from the problem
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Edge case - negative numbers
print(sqrt(-100))
# Returns None

# Large number with an exact square
print(sqrt(1522756))
# Returns 1234

# Large number without an exact square
print(sqrt(1234000))
# Returns 1110

