# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root: return []
        D = collections.defaultdict(int)
        def cal_sum(node):
            if not node: return 0
            num = node.val + cal_sum(node.left) + cal_sum(node.right)
            D[num] += 1
            return num
        cal_sum(root)
        maxnum = max(D.values())
        return [k for k,v in D.items() if v == maxnum]