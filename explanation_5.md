### Reasoning
The two most complex algorithms here is the TrieNode::suffixes method and the Trie::find method.  The TrieNode::suffixes method uses a recursive depth first search because this consumes less memory at one time -- one letter may branch off to many words, and storing references to all these nodes at once could be more expensive than storing just the number of nodes in depth we are currently at.  The Trie::find method simply iterates down into the tree in a depth first search manner, since a BFS doesn't make sense when there's only ever one valid route in the tree.

### Big-O
#### TrieNode::suffixes
This method has a time complexity of O(n), since we have to traverse over every child node in the tree to find all possible words.  The space complexity is also O(n), since we have to store nodes equal to the number of levels deep, and in the worst case we have a single line of nodes.

#### Trie::find
This method has a time complex of O(n), since in the worst case we have to traverse the entire tree to find the node.  It also consumes O(n) space for the same reason as TrieNode::suffixes -- in the case where a tree isn't really a tree, but a line of nodes, we have to store the entire tree before returning.

