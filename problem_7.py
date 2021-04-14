# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self._root = RouteTrieNode()
        self._root.set_handler(root_handler)

    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self._root
        for path in paths:
            current.insert(path)
            current = current.get_children()[path]
        current.set_handler(handler)

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current = self._root
        for path in paths:
            if path not in current.get_children():
                return None
            current = current.get_children()[path]

        if current.get_handler() == None:
            return None
        return current

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self._children = {}
        self._handler = None

    def insert(self, path):
        # Insert the node as before
        if self._children.get(path) is None:
            self._children[path] = RouteTrieNode()

    def get_children(self):
        return self._children

    def set_handler(self, handler):
        self._handler = handler

    def get_handler(self):
        return self._handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self._routes = RouteTrie(root_handler)
        self._not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self._routes.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        found = self._routes.find(self.split_path(path))
        if found == None:
            return self._not_found_handler
        return found.get_handler()

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        path = path.strip("/")
        if path == "":
            return []
        return path.strip("/").split("/") # Ignore leading and trailing "/"


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# Test add first-level end point
router.add_handler("/home", "home handler")
print(router.lookup("/home")) # now prints "home handler"

# Test reset root handler to another path
router.add_handler("/", "new root handler")
print(router.lookup("/")) # should print "new root handler"

# Test empty path
print(router.lookup("")) # should print "new root handler"

# Test long path that does not exist
print(router.lookup("/long/path/to/nowhere/should/be/not/found")) # should print "not found handler"

# Test adding a path that does not start with "home"
router.add_handler("/blog", "blog end point")
print(router.lookup("/blog")) # should print "blog end point"

# Test adding path that includes a trailing "/"
router.add_handler("/classes/", "classes end point")
print(router.lookup("/classes")) # should print "classes end point"

