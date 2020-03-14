# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        res = self.subrob(root)
        return max(res[0], res[1])

    def subrob(self, root):
        if root is None:
            return [0, 0]
        left = self.subrob(root.left)
        right = self.subrob(root.right)
        res = [0, 0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        return res

    #     if root == None:
    #         return 0
    #     return max(self.robInclude(root), self.robExclude(root))
    # def robInclude(self, node):
    #     if node == None:
    #         return 0
    #     return self.robInclude(node.left) + self.robInclude(node.right) + node.val
    # def robExclude(self, node):
    #     if node == None:
    #         return 0
    #     return self.robExclude(node.left) + self.robExclude(node.right)