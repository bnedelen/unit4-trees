"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value   # the data held by this node
        self.left = None     # left child: will hold values SMALLER than this node
        self.right = None    # right child: will hold values LARGER than this node


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The public method hides the recursion from the caller. We start at
        # the root and let the helper return the (possibly new) root, which
        # handles the empty-tree case automatically.
        # Insertion depends on smaller vs. larger because the BST rule says
        # everything on the left is smaller and everything on the right is
        # larger. Comparing to the current node tells us which half of the
        # tree the new value belongs in, so we never have to look at the other half.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case: we found an empty spot, so create the new node here.
        if node is None:
            return Node(value)

        if value < node.value:
            # Smaller values belong in the left subtree.
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            # Larger values belong in the right subtree.
            node.right = self._insert_recursive(node.right, value)
        # If value == node.value it is a duplicate. We ignore it so each
        # value appears only once in the tree.

        # Return the node so the parent can re-link its child reference.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # A linear search may check every item (O(n)). In a BST each
        # comparison lets us discard an entire subtree. If the tree is
        # reasonably balanced, the search space is cut roughly in half at every
        # step, giving O(log n) time instead of O(n).
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Base case 1: we ran off the tree, so the value is not present.
        if node is None:
            return False
        # Base case 2: the current node matches, so the value was found.
        if value == node.value:
            return True
        # Recursive case: go left or right, ignoring the other subtree.
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values  # an empty tree returns an empty list

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # In-order traversal produces sorted output because every value in
        # the left subtree is smaller than the node, and every value in the
        # right subtree is larger. Visiting left, then node, then right
        # always outputs smaller values first, then the node, then larger values.
        if node is None:      # base case: nothing to visit
            return
        self._inorder_recursive(node.left, values)    # 1. left subtree
        values.append(node.value)                     # 2. current node
        self._inorder_recursive(node.right, values)   # 3. right subtree

    def height(self):
        # Extra helper (not part of the TODOs): the height is the number of
        # levels in the tree. It shows how well-balanced the tree is.
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_recursive(node.left),
                       self._height_recursive(node.right))


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    tree = BST()
    values_to_insert = [50, 30, 70, 20, 40, 60, 80, 35]
    for v in values_to_insert:
        tree.insert(v)
    print("Values inserted:", values_to_insert)
    # 50 is the root. 30, 20, 40, 35 go left (smaller than 50) and
    # 70, 60, 80 go right (larger than 50), so both subtrees are used.
    # Efficiency: at each step one comparison eliminates a whole subtree.
    # Looking for 35: at 50 we skip the entire right side, at 30 we skip
    # the left side, at 40 we skip the right side, and we find 35 in
    # 4 steps instead of scanning all 8 values.
    print("Tree height:", tree.height())

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    result = tree.inorder()
    print("In-order result:", result)
    # The output is sorted even though the insert order was not. Left
    # subtrees hold smaller values and right subtrees hold larger ones, so
    # visiting left, node, right always yields ascending order.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # Values that exist: found by following one path from the root down.
    print("Search 60:", tree.search(60))   # True: 50 -> right to 70 -> left to 60
    print("Search 35:", tree.search(35))   # True: 50 -> 30 -> 40 -> 35
    # Values that do not exist: the search falls off the tree (reaches
    # None), which means the value is not in the tree.
    print("Search 65:", tree.search(65))   # False: 50 -> 70 -> 60 -> right is None
    print("Search 10:", tree.search(10))   # False: 50 -> 30 -> 20 -> left is None

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    # Edge case 1: empty tree. There is no root, so traversal returns an
    # empty list and a search returns False instead of crashing.
    empty = BST()
    print("Empty tree in-order:", empty.inorder())
    print("Search empty tree for 5:", empty.search(5))

    # Edge case 2: duplicate values. The duplicate is ignored, so the tree
    # keeps only one copy of each value.
    dup = BST()
    for v in [10, 5, 10, 5, 15]:
        dup.insert(v)
    print("Duplicates inserted [10, 5, 10, 5, 15] ->", dup.inorder())

    # ===============================
    # REAL-WORLD EXAMPLE: EMPLOYEE IDs
    # ===============================
    # Employee records are looked up by ID number. The SAME IDs are
    # inserted in two different orders to show how insertion order
    # affects the shape of the tree.
    print("\n=== REAL-WORLD EXAMPLE: EMPLOYEE IDs ===")
    ids = [1001, 1002, 1003, 1004, 1005, 1006, 1007]

    # Sequential order: each ID is larger than the last, so every node goes
    # to the right. The tree becomes a linked list (height 7), and a
    # search can take O(n) steps.
    sequential = BST()
    for emp_id in ids:
        sequential.insert(emp_id)

    # Balanced order: start with the middle value, then the middles of
    # each half. The tree stays short and wide (height 3), so searches take
    # about O(log n) steps.
    balanced = BST()
    for emp_id in [1004, 1002, 1006, 1001, 1003, 1005, 1007]:
        balanced.insert(emp_id)

    print("Sequential insertion height:", sequential.height())
    print("Balanced insertion height:  ", balanced.height())
    print("Both trees in-order:", sequential.inorder() == balanced.inorder())
    # Both trees hold identical data, but the balanced one is far more
    # efficient to search. This is why unbalanced BSTs degrade, and why
    # self-balancing trees (AVL, Red-Black) exist.



if __name__ == "__main__":
    main()