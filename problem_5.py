## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self._is_word = False
        self._children = {}
    
    def set_is_word(self):
        self._is_word = True
    
    def get_is_word(self):
        return self._is_word
    
    def get_children(self):
        return self._children

    def insert(self, char):
        ## Add a child node in this Trie
        if self._children.get(char) is None:
            self._children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        result = []
        for char, child in self._children.items():
            if child.get_is_word():
                result.append(suffix + char)
            
            if child.get_children():
                result.extend(child.suffixes(suffix + char))
        return result

    def __repr__(self):
        out = "Word ending: " + str(self._is_word) + "\n"
        out += "Children: " + str(self._children)
        return out

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self._root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        if len(word) <= 0:
            # Do not add empty word
            return

        current = self._root
        for char in word:
            current.insert(char)
            current = current.get_children()[char]
        current.set_is_word()

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current = self._root
        for char in prefix:
            if char not in current.get_children():
                return False
            current = current.get_children()[char]
        return current

# Create Trie and add some words
words = [
    "ant", "anthology", "antonym",
    "fact", "factual", "fun", "function",
    "trie", "trigger", "trigonometry", "tripod"
]
trie = Trie()

for word in words:
    trie.insert(word)

# Tests
# Find a node
found = trie.find("ant")
print(found)
"""
Returns output of:
Word ending: True
Children: {'h': Word ending: False
Children: {'o': Word ending: False
Children: {'l': Word ending: False
Children: {'o': Word ending: False
Children: {'g': Word ending: False
Children: {'y': Word ending: True
Children: {}}}}}}, 'o': Word ending: False
Children: {'n': Word ending: False
Children: {'y': Word ending: False
Children: {'m': Word ending: True
Children: {}}}}}
"""

# Show possible options from suffix
print()
print(found.suffixes())
# Returns ['hology', 'onym']

# Find empty string
print()
found = trie.find("")
print(found)
# Find the root node and prints the whole tree

# Show all possible words
print()
print(found.suffixes())
# Returns ['ant', 'anthology', 'antonym', 'fact', 'factual', 'fun', 'function', 'trie', 'trigger', 'trigonometry', 'tripod']

# Add an empty string to the trie -- ensure that it adds no nodes
print(len(found.get_children()))
# Returns 3 (for a, f, t)
trie.insert("")
found = trie.find("")
print(len(found.get_children()))
# Returns 3 (for a, f, t)

