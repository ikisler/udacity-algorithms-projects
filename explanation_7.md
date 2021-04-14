### Reasoning
The Router class itself is a thin wrapper for the RouteTrie class, with some logic around splitting the paths -- all the algorthmically interesting bits happen in the RouteTrie class, which follows a pretty conventional Trie pattern, as in problem 5 -- on insert, iterate down adding new portions of a path, and on find, iterate through paths looking for nodes that contain handlers.

### Big-O
#### RouteTrie::insert
This method has a time and space complexity of O(n), since in the worst case we have to iterate through every single node and store all of them.

#### RouteTrie::find
This method has a time and space complexity of O(n), since in the worst case (the item isn't in the tree at all) we have to iterate through the whole list.

