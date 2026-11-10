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
        # Each node holds one value and can point to at most two children
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Empty tree starts with no root
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.
        """
        # Smaller values go left, larger go right. This lets later
        # searches discard an entire subtree after one comparison.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Recursive BST insertion.
        """
        # Found an empty spot, place the new node here
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            # Larger or equal values go right so the BST property holds
            node.right = self._insert_recursive(node.right, value)

        return node

    def search(self, value):
        """
        Search for a value in the BST.
        """
        # Linear search checks every record. A BST comparison eliminates
        # one whole subtree, so a balanced tree is roughly O(log n).
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Recursive BST search.
        """
        # Reached a missing child, value is not in the tree
        if node is None:
            return False

        if value == node.value:
            return True

        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return a list containing the values from an in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        In-order traversal: left, current, right.
        """
        if node is None:
            return

        # Left first: all smaller values
        self._inorder_recursive(node.left, values)
        # Current node
        values.append(node.value)
        # Right last: all larger values
        # Because left < node < right, the result comes out sorted
        self._inorder_recursive(node.right, values)


# Real-world example: personnel records organized by ID
PERSONNEL = {
    1001: "SPC Team Leader",
    1002: "PFC Bridge Operator",
    1003: "SGT Maintenance NCO",
    1004: "SPC Equipment Mechanic",
    1005: "PFC Driver",
    1006: "SPC Welder",
    1000: "PV2 New Arrival",
    1007: "SPC Senior Operator"
}


def personnel_name(pid):
    return PERSONNEL.get(pid, "Unknown personnel")


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # TREE CONSTRUCTION
    print("\n=== TREE CONSTRUCTION ===")
    bst = BST()

    # Start near the middle so both left and right subtrees fill.
    # Sequential inserts would have turned this into a linked list.
    insertion_order = [1003, 1002, 1005, 1001, 1004, 1006, 1000, 1007]

    print("Personnel IDs inserted:")
    for pid in insertion_order:
        print(f"  {pid}: {personnel_name(pid)}")

    # Each insert walks one path and cuts the remaining search space
    for pid in insertion_order:
        bst.insert(pid)
        print(f"  Inserted {pid}")

    # IN-ORDER TRAVERSAL
    print("\n=== IN-ORDER TRAVERSAL ===")
    # Left-node-right visits smaller IDs first, so the result is sorted
    traversal_result = bst.inorder()
    print("In-order traversal (sorted IDs):", traversal_result)

    print("Personnel in sorted ID order:")
    for pid in traversal_result:
        print(f"  {pid}: {personnel_name(pid)}")

    # SEARCH TESTS
    print("\n=== SEARCH TESTS ===")
    # These two IDs were inserted, so search returns True
    print("Search 1002 (exists):", bst.search(1002))
    print("Search 1005 (exists):", bst.search(1005))

    # These two were never inserted, so search returns False
    print("Search 1008 (does not exist):", bst.search(1008))
    print("Search 999 (does not exist):", bst.search(999))

    # EDGE CASES
    print("\n=== EDGE CASES ===")

    # Empty tree: no root, so traversal is empty and search returns False
    empty_bst = BST()
    print("In-order on empty tree:", empty_bst.inorder())
    print("Search 1001 on empty tree:", empty_bst.search(1001))

    # Single-node tree: insert and search still work
    single_bst = BST()
    single_bst.insert(1002)
    print("Single-node in-order:", single_bst.inorder())
    print("Search 1002 on single-node tree:", single_bst.search(1002))
    print("Search 1001 on single-node tree:", single_bst.search(1001))

    # Duplicate goes right in this version; in-order stays sorted
    print("Inserting duplicate 1003:")
    bst.insert(1003)
    print("In-order after duplicate insert:", bst.inorder())


if __name__ == "__main__":
    main()