# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:return True
        def dfs(root,minvalue,maxvalue):
            if not root: return True
            if root.val <= minvalue or root.val >= maxvalue:
                return False
            return dfs(root.left,minvalue,root.val) and dfs(root.right,root.val,maxvalue)
        return dfs(root,float("-inf"),float("inf"))
                