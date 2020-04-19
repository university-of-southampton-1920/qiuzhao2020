# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        result = []
        if root is not None:
            queue.append([root])
        else:
            return None
        while(queue):
            tempqueue = []
            temp_result = []
            for node in queue.pop(0):
                temp_result.append(node.val)
                if node.left is not None:
                    tempqueue.append(node.left)
                if node.right is not None:
                    tempqueue.append(node.right)
                    
            if (temp_result):     
                result.append(temp_result)
                queue.append(tempqueue)
                
        return result