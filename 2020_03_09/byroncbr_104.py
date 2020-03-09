"""
Name: byroncbr_104.py
Author: bangrenc
Time: 9/3/2020 10:15 AM
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# s = Solution()
# a = [3,9,20,None,None,15,7]
#
# root = TreeNode(a)
# result = s.maxDepth(root)
# print(result)



