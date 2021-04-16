### Reasoning
For this problem, I used a modified binary search -- since we know that the array has been cut in half at some random point, we have to check if the half that we'd normally recurse down into actually contains the value we are searching for.

### Big-O
The time efficiency for this O(log n) in the worst case, since every time we iterate we cut the area we have to search in half.  The space complexity in the worst case is O(1), since for any size array we only have to maintain 5 points of data in addition to the space of the input.

