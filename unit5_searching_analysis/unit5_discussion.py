"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    Linear search: check every element from start to finish.
    """
    # O(n) because in the worst case we look at every item once
    # No way to skip ahead if the list is unsorted
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    """
    Binary search: repeatedly cut the remaining search space in half.
    Assumes the list is already sorted.
    """
    # Each step discards half the remaining elements
    # That's why it runs in O(log n) on a sorted list
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            # Target is in the right half
            left = mid + 1
        else:
            # Target is in the left half
            right = mid - 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # SMALL DATASET
    print("\n=== SMALL DATASET TEST ===")
    small = [2, 5, 8, 12, 16, 23, 38, 45]
    print("Small sorted list:", small)

    # Value that exists
    print("Linear search for 12:", linear_search(small, 12))
    print("Binary search for 12:", binary_search(small, 12))

    # Value that does not exist
    print("Linear search for 99:", linear_search(small, 99))
    print("Binary search for 99:", binary_search(small, 99))

    # LARGE DATASET
    print("\n=== LARGE DATASET TEST ===")
    # 1000 sorted numbers
    large = list(range(0, 10000, 10))
    print(f"Large sorted list size: {len(large)}")

    # Search for a value near the end so linear has to do more work
    target = 9990
    print(f"Linear search for {target}:", linear_search(large, target))
    print(f"Binary search for {target}:", binary_search(large, target))

    # Missing value
    print("Linear search for 9995:", linear_search(large, 9995))
    print("Binary search for 9995:", binary_search(large, 9995))

    # Binary stays fast even as the list grows because it keeps cutting the space in half
    # Linear has to walk further on average

    # EDGE CASES
    print("\n=== EDGE CASE TESTS ===")

    # Empty list
    empty = []
    print("Linear on empty:", linear_search(empty, 5))
    print("Binary on empty:", binary_search(empty, 5))

    # Single-element list
    single = [42]
    print("Linear on single (hit):", linear_search(single, 42))
    print("Binary on single (hit):", binary_search(single, 42))
    print("Linear on single (miss):", linear_search(single, 7))
    print("Binary on single (miss):", binary_search(single, 7))

    # Value at first and last position
    print("Linear for first element (2):", linear_search(small, 2))
    print("Binary for first element (2):", binary_search(small, 2))
    print("Linear for last element (45):", linear_search(small, 45))
    print("Binary for last element (45):", binary_search(small, 45))


if __name__ == "__main__":
    main()