# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(node):
            if not node:
                return 0, True

            left_height, left_balanced = check(node.left)
            right_height, right_balanced = check(node.right)

            height = 1 + max(left_height, right_height)
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            return height, balanced

        _, result = check(root)
        return result

        