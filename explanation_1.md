### Reasoning
While it is possible to iterate over a range and check each value, this is slow -- for a number like 25, finding the square root would take 5 iterations.  Using the Babylonian method which starts from an estimate and iteratively gets closer to the actual answer by cutting the numbers available to guess in halve each iteration is much more efficient.

### Big-O Complexity
Both the time and space complexity for this method is O(log n), because every loop we divide the area of guessable square roots in half.
