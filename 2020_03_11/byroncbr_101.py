"""
Name: byron_101.py
Author: bangrenc
Time: 11/3/2020 3:12 PM
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(L,R):
            if not L and not R: #梯度已经在最深一层，可以return true
                return True
            if L and R and L.val == R.val: #判断这一层是否存在 并且数值相等，继续梯度传下去
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root, root)


