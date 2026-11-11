# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Code Documentation

### Implementation

I completed the starter file `unit4_discussion.py` by implementing a `Node` class and a `BST` class, and I kept all of the original TODO prompts and comments in place.

- **Node:** I created the `Node` class to store a value along with references to its left and right children, which both started as `None`.
- **Insert:** I implemented `insert` as a public method that called the recursive helper `_insert_recursive`. The helper created a new node when it reached an empty position, inserted smaller values into the left subtree, inserted larger values into the right subtree, and returned the updated node. I chose to ignore duplicate values so each value appeared only once.
- **Search:** I implemented `search` and `_search_recursive` to return `True` when a value was found and `False` when the search reached an empty spot. Each comparison skipped an entire subtree, which is why BST search can be faster than a linear search.
- **In-order traversal:** I implemented `inorder` and `_inorder_recursive` to visit the left subtree, then the current node, then the right subtree. This produced the values in sorted order.
- **Height (extra):** I added a `height` method to measure how many levels the tree had, which let me compare balanced and unbalanced trees.

### Demonstration in `main()`

- **Tree construction:** I inserted the values `[50, 30, 70, 20, 40, 60, 80, 35]`, which placed values in both the left and right subtrees.
- **In-order traversal:** The traversal returned `[20, 30, 35, 40, 50, 60, 70, 80]`, which was sorted even though the insertion order was not.
- **Search tests:** I searched for 60 and 35 (both found) and for 65 and 10 (both not found).
- **Edge cases:** I tested an empty tree, where traversal returned an empty list and search returned `False`, and I tested duplicate insertions, where the duplicates were ignored.

### Real-World Example: Employee IDs

I modeled an employee record system that looked up employees by ID number. I inserted the same seven IDs (1001-1007) in two different orders. Inserting them in sequential order created a tree with a height of 7, which behaved like a linked list. Inserting them in a balanced order (1004, 1002, 1006, 1001, 1003, 1005, 1007) created a tree with a height of 3. Both trees contained identical data and produced the same in-order output, but the balanced tree required far fewer steps to search.

### Sample Output

```
=== UNIT 4: BINARY SEARCH TREES ===

=== TREE CONSTRUCTION ===
Values inserted: [50, 30, 70, 20, 40, 60, 80, 35]
Tree height: 4

=== IN-ORDER TRAVERSAL ===
In-order result: [20, 30, 35, 40, 50, 60, 70, 80]

=== SEARCH TESTS ===
Search 60: True
Search 35: True
Search 65: False
Search 10: False

=== EDGE CASES ===
Empty tree in-order: []
Search empty tree for 5: False
Duplicates inserted [10, 5, 10, 5, 15] -> [5, 10, 15]

=== REAL-WORLD EXAMPLE: EMPLOYEE IDs ===
Sequential insertion height: 7
Balanced insertion height:   3
Both trees in-order: True
```

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150â€“200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
