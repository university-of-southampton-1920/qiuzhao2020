# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
###结束条件是pre,tin都为空
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)==0 or len(tin) == 0:
            return None
        n = pre[0]        
        index = tin.index(n)
        left = self.reConstructBinaryTree(pre[1:1+index],tin[:index]) ##list[:0]返回空[]
        right = self.reConstructBinaryTree(pre[1+index:len(pre)],tin[index+1:len(tin)])
        root = TreeNode(n)
        root.left = left
        root.right = right
        return root  #每次递归都返回一个完整的子树