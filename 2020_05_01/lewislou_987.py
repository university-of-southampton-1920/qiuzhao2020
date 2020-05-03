# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        seen = collections.defaultdict(lambda:collections.defaultdict(list))
        def dfs(node,x=0,y=0):
            if node:
                seen[x][y].append(node)
                dfs(node.left,x-1,y+1)
                dfs(node.right,x+1,y+1)
        dfs(root)
        result = []
        for x in sorted(seen):
            temp = []
            for y in sorted(seen[x]):
                temp.extend(sorted(node.val for node in seen[x][y]))
            result.append(temp)
        return result