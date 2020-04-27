# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack = [[root,0]]
        result = []
        while(stack):
            cur,label = stack[-1]
            if label==0:
                if cur.left:
                    stack.append([cur.left,0])
                else:
                    stack.pop()
                    stack.append([cur,1])
            elif label==1:
                if cur.right:
                    stack.append([cur.right,0])
                else:
                    stack.pop()
                    stack.append([cur,2])
            else:
                result.append(cur.val)
                stack.pop()
                if stack:
                    stack[-1][-1] += 1
        return result
                
                