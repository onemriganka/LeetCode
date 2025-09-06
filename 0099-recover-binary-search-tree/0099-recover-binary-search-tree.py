# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        first = second = prev = None
        stack = []
        node = root

        # Iterative in-order traversal
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()

            if prev and node.val < prev.val:
                if not first:
                    first = prev
                second = node

            prev = node
            node = node.right

        # Swap the values of the two nodes
        if first and second:
            first.val, second.val = second.val, first.val


        