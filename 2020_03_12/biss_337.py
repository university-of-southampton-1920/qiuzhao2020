# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.mark = dict()
    
    def rob(self, root: TreeNode) -> int:
        node = root
        if node == None:
            return 0
        t1 = self.helper(node.left, 0) + self.helper(node.right, 0)
        t2 = self.helper(node.left, 1) + self.helper(node.right, 1) + node.val
        return max(t1, t2)
    
    def helper(self, node, rob):
        if (node, rob) in self.mark:
            return self.mark[(node, rob)]
        if node == None:
            return 0
        if rob == 1:
            self.mark[(node, rob)] = self.helper(node.left, 0) + self.helper(node.right, 0)
        else: # no rob
            t1 = self.helper(node.left, 0) + self.helper(node.right, 0)
            t2 = self.helper(node.left, 1) + self.helper(node.right, 1) + node.val
            self.mark[(node, rob)] =  max(t1, t2)
        return self.mark[(node, rob)]