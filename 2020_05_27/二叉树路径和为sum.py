# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        path = []
        if not root: return []
        def recur(root,remain):
            if not root: return
            path.append(root.val)
            remain -= root.val
            if remain == 0 and (not root.left) and (not root.right):
                #print(path)
                result.append(list(path))
            recur(root.left,remain)
            recur(root.right,remain)
            path.pop()
        recur(root,sum)
        return result


