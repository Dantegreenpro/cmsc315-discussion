# Unit 5 Discussion: Searching and Algorithm Analysis

## Overview

This assignment compares linear search and binary search on sorted data.

## Requirements

Completed all sections:

1. Implemented linear search that scans from start to finish and returns the index or -1. Worst case is O(n) because every element may need to be checked.
2. Implemented binary search that repeatedly halves the remaining range. Each step discards half the search space, giving O(log n) on a sorted list.
3. Tested both algorithms on a small sorted list with a present value and a missing value.
4. Tested both on a larger sorted list (1000 elements) and compared results.
5. Covered edge cases: empty list, single-element list, value at the first position, and value at the last position.

## Implementation Notes

Linear search walks the list in order with no assumptions about sorting. Binary search requires the list to be sorted and narrows the window with left/right pointers. Comments explain the complexity difference and why binary becomes more efficient as the data set grows. The main function prints clear results for the small list, large list, and edge cases.