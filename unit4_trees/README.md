# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment explores Binary Search Tree insertion, search, and in-order traversal.

## Requirements

Completed all sections:

1. Implemented Node with value, left, and right references.
2. Implemented recursive insert so smaller values go left and larger values go right.
3. Implemented recursive search that returns True or False. Each comparison discards an entire subtree.
4. Implemented in-order traversal (left-node-right) that produces sorted output because of the BST property.
5. Built a tree with at least 7 personnel IDs, starting near the middle so both subtrees fill.
6. Demonstrated in-order traversal and verified the result is sorted.
7. Searched for two existing IDs and two missing IDs.
8. Tested edge cases: empty tree traversal and search, single-node tree, and duplicate insert.

## Implementation Notes

Used recursive helpers for insert, search, and in-order. Comments explain why smaller values go left, why search is faster than linear when the tree is balanced, and why in-order produces sorted output. The main function uses a personnel-ID example and walks through construction, traversal, search, and the edge cases with clear print statements.