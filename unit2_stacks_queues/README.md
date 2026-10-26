# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Completed all TODO sections:

1. Implemented stack operations using a Python list (append for push, pop from the end for pop, last-element access for peek).
2. Implemented queue operations using collections.deque (append for enqueue, popleft for dequeue, index 0 for front).
3. Demonstrated LIFO behavior by pushing multiple values and popping them in reverse order.
4. Demonstrated FIFO behavior by enqueuing multiple values and dequeuing them in the original order.
5. Created and tested edge cases including empty structures (pop, peek, dequeue, front) and single-item structures that become empty after removal.
6. Created a real-world scenario in the discussion post (text editor undo for stack, coffee shop line for queue).

## Implementation Notes

Used a list for the Stack class so the last added item is always at the end and can be removed first. Used a deque for the Queue class so items can be added to the back and removed from the front efficiently. Both classes check is_empty before removal or peek operations and print a clear message if the structure is empty. The main function walks through four-item demos, empty-structure handling, and the single-item edge case for both structures.
