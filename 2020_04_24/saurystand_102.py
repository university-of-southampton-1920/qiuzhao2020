# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []

        def helper(self, node, level):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                helper(self, node.left, level + 1)
            if node.right:
                helper(self, node.right, level + 1)

        helper(self, root, 0)

        return res