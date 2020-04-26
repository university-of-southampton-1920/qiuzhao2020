# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def maxPathSum(self, root: TreeNode) -> int:
        if not root: return 0
        #D = collections.defaultdict(int)
        self.result = -inf
        def cal_sum(node):
            if not node: return 0
            l = cal_sum(node.left)
            r = cal_sum(node.right)
            self.result = max(self.result,
                              node.val,
                             l+node.val,
                             r+node.val,
                             r+l+node.val,)
            return max(node.val,node.val+l,node.val+r)
        cal_sum(root)
        return self.result