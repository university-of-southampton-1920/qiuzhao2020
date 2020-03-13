# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.robbing(root, dict())
    def robbing(self, root, robmap):
        if root == None:
            return 0
        if root in robmap:
            return robmap[root]
        val = 0
        if root.left != None:
            val += self.robbing(root.left.left, robmap) + self.robbing(root.left.right, robmap)
        if root.right != None:
            val += self.robbing(root.right.left, robmap) + self.robbing(root.right.right, robmap)
        val = max(root.val + val, self.robbing(root.left, robmap)+self.robbing(root.right, robmap))
        robmap[root] = val
        return val
