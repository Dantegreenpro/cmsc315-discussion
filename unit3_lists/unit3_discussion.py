"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.
    """
    # list.insert shifts every element at and after the index one position to the right
    # Inserting near the front is slower because more elements have to move
    # Inserting at the end is faster because almost nothing has to shift
    lst.insert(index, value)


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.
    """
    # Validate the index so we don't crash on bad input
    # Safe deletion matters because an invalid index would raise an IndexError
    if index < 0 or index >= len(lst):
        print(f"Cannot delete: index {index} is out of range")
        return None
    # pop removes the item and shifts everything after it left to fill the gap
    return lst.pop(index)


def search_value(lst, value):
    """
    Search for a value within the list.
    """
    # Linear search: start at the beginning and check each item one by one
    # Has to scan sequentially because a regular list has no faster lookup structure
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # INSERTION TESTS
    print("\n=== INSERTION TESTS ===")
    songs = ["Song A", "Song B", "Song C"]
    print("Original list:", songs)

    # Insert at the beginning (shifts everything right)
    insert_at(songs, 0, "Song X")
    print("After insert at beginning:", songs)

    # Insert in the middle
    insert_at(songs, 2, "Song Y")
    print("After insert in middle:", songs)

    # Insert at the end
    insert_at(songs, len(songs), "Song Z")
    print("After insert at end:", songs)

    # DELETION TESTS
    print("\n=== DELETION TESTS ===")
    # Delete from the beginning
    removed = delete_at(songs, 0)
    print(f"Deleted from beginning: {removed}")
    print("List now:", songs)

    # Delete from the middle
    removed = delete_at(songs, 1)
    print(f"Deleted from middle: {removed}")
    print("List now:", songs)

    # Delete from the end
    removed = delete_at(songs, len(songs) - 1)
    print(f"Deleted from end: {removed}")
    print("List now:", songs)

    # SEARCH TESTS
    print("\n=== SEARCH TESTS ===")
    # Search for a value that exists
    idx = search_value(songs, "Song B")
    print(f"Search for 'Song B': found at index {idx}" if idx != -1 else "Search for 'Song B': not found")

    # Search for a value that does not exist
    idx = search_value(songs, "Song Q")
    print(f"Search for 'Song Q': found at index {idx}" if idx != -1 else "Search for 'Song Q': not found")

    # EDGE CASES
    print("\n=== EDGE CASES ===")
    # Invalid index on delete
    delete_at(songs, 99)

    # Delete from empty list
    empty = []
    delete_at(empty, 0)

    # Insert into empty list
    insert_at(empty, 0, "First Song")
    print("After insert into empty list:", empty)

    # Search on empty list
    print("Search on empty list:", search_value([], "anything"))


if __name__ == "__main__":
    main()