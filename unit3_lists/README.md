# Unit 3 Discussion: List Operations

## Overview

This assignment explores how Python lists handle insertion, deletion, and search.

## Requirements

Completed all sections:

1. Implemented insert_at using list.insert, which shifts later elements right. Insertion near the front moves more items and is slower; insertion at the end moves almost nothing.
2. Implemented delete_at with index validation. Returns the removed value or None if the index is invalid, and uses pop which shifts later elements left.
3. Implemented search_value as a linear scan that returns the index or -1. It must check every element in order because a plain list has no faster lookup.
4. Demonstrated insertions at the beginning, middle, and end.
5. Demonstrated deletions from the beginning, middle, and end.
6. Demonstrated successful and unsuccessful searches.
7. Tested edge cases: invalid index, empty list deletion, insert into empty list, and search on empty list.

## Implementation Notes

Used Python’s built-in list for all operations. Comments explain the shifting behavior on insert and delete and why search is linear. The main function walks through each required test with clear print statements so the output shows exactly what changed.