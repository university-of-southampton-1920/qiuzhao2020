"""
Name: byroncbr_111.py
Author: bangrenc
Time: 9/3/2020 10:59 AM
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left == None or root.right == None:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1
        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1




