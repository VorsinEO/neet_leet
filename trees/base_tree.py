from typing import Optional, List


class TreeNode:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"

    def __str__(self) -> str:
        return str(self.val)


def to_binary_tree(items: List[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return []

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


def to_list_from_tree(tree, templist=[]):
    """
    >>> tree = BinaryTree(2, BinaryTree(29, BinaryTree(26)), BinaryTree(4, None, BinaryTree(2, BinaryTree(9))))
    >>> create_list(tree)
    [2, 29, 4, 26, None, None, 2, None, None, None, None, None, None, 9, None]

    """
    if not tree:
        return []
    items = []
    queue = [tree]

    while queue:
        copy = queue[:]
        queue = []

        for item in copy:
            if item is None:
                items.append(None)
                queue.append(None)
                queue.append(None)
            else:
                items.append(item.val)
                queue.append(item.left)
                queue.append(item.right)

        if all((x is None for x in queue)):
            break

    return items
