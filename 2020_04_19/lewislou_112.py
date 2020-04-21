# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
##recursive
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        sum -= root.val
        if not root.left and not root.right:
            if sum == 0:
                return True
            return False
        left = self.hasPathSum(root.left,sum)
        right = self.hasPathSum(root.right,sum)
        
        return left or right
##BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:return False
        q = collections.deque([(root,sum-root.val)])
        while(q):
            for _ in range(len(q)):
                cur,total = q.popleft()
                if total == 0 and not (cur.left or cur.right):
                    return True
                if cur.left:
                    q.append((cur.left,total-cur.left.val))
                if cur.right:
                    q.append((cur.right,total-cur.right.val))
        return False
		
#DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:return False
        stack = [(root,sum-root.val)]
        while stack:
            cur,total = stack.pop()
            if total==0 and not (cur.left or cur.right):
                return True
            if cur.left:
                stack.append((cur.left,total-cur.left.val))
            if cur.right:
                stack.append((cur.right,total-cur.right.val))
        return False