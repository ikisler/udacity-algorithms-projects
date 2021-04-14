### Reasoning
By first sorting the numerals largest to smallest using a merge sort, it's easy to then iterate through the list and just grab the largest numeral to iteratively build the resulting two numbers.

### Big-O Complexity
Time complexity is O(n log n) because the merge sort has this complexity and the iteration over the list is O(n), and O(n log n) + O(n) is O(n log n) all together.

Space complexity is O(n), since the merge sort has space requirements this size and the resulting array also takes no more space than O(n).

