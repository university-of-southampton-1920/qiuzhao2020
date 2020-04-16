# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        if root is None:
            return None
        while (root is not None) or (len(stack)!=0):
            while(root is not None):
                stack.append(root)
                #print(root.val)
                root = root.left
            #print(root.val)
            root = stack.pop()
            result.append(root.val)
            root = root.right
            #print(root is not None)
            
        return result
