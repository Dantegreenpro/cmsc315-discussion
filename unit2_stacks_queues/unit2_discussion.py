"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # List stores the stack values; the last index is always the top
        self.items = []

    def push(self, value):
        # Append adds to the end (top), so the most recent item is the next one removed (LIFO)
        self.items.append(value)

    def pop(self):
        # Remove and return the most recently added value
        if self.is_empty():
            print("Cannot pop: stack is empty")
            return None
        return self.items.pop()

    def peek(self):
        # Return the top value without removing it
        if self.is_empty():
            print("Cannot peek: stack is empty")
            return None
        return self.items[-1]

    def is_empty(self):
        # True if the stack has no values
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # Deque gives efficient add-to-back and remove-from-front
        self.items = deque()

    def enqueue(self, value):
        # Append adds to the back; the first item added stays at the front until removed (FIFO)
        self.items.append(value)

    def dequeue(self):
        # Remove and return the value from the front of the queue
        if self.is_empty():
            print("Cannot dequeue: queue is empty")
            return None
        return self.items.popleft()

    def front(self):
        # Return the front value without removing it
        if self.is_empty():
            print("Cannot view front: queue is empty")
            return None
        return self.items[0]

    def is_empty(self):
        # True if the queue has no values
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # STACK DEMO
    print("\n=== STACK DEMO ===")
    stack = Stack()
    print("Created empty stack. is_empty():", stack.is_empty())

    print("\nPushing 4 values (last pushed will be first popped):")
    for val in [10, 20, 30, 40]:
        stack.push(val)
        print(f"  Pushed {val} | Top is now {stack.peek()}")

    print("\nDemonstrating LIFO (popping until empty):")
    while not stack.is_empty():
        print(f"  Popped {stack.pop()}")

    print("\nTrying to pop from empty stack:")
    stack.pop()

    print("\nTrying to peek at empty stack:")
    stack.peek()

    print("\nSingle-item edge case:")
    stack.push(99)
    print(f"  Pushed 99 | is_empty(): {stack.is_empty()}")
    stack.pop()
    print(f"  Popped the only item | is_empty(): {stack.is_empty()}")

    # QUEUE DEMO
    print("\n=== QUEUE DEMO ===")
    queue = Queue()
    print("Created empty queue. is_empty():", queue.is_empty())

    print("\nEnqueuing 4 values (first enqueued will be first dequeued):")
    for val in ["A", "B", "C", "D"]:
        queue.enqueue(val)
        print(f"  Enqueued {val} | Front is now {queue.front()}")

    print("\nDemonstrating FIFO (dequeuing until empty):")
    while not queue.is_empty():
        print(f"  Dequeued {queue.dequeue()}")

    print("\nTrying to dequeue from empty queue:")
    queue.dequeue()

    print("\nTrying to view front of empty queue:")
    queue.front()

    print("\nSingle-item edge case:")
    queue.enqueue("Z")
    print(f"  Enqueued Z | is_empty(): {queue.is_empty()}")
    queue.dequeue()
    print(f"  Dequeued the only item | is_empty(): {queue.is_empty()}")


if __name__ == "__main__":
    main()