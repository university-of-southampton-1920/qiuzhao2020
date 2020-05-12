# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # write your code here
        def build(inorder,in_start,in_end,postorder,post_start,post_end):
            if in_start >= in_end:
                return None
            i = in_start
            while i < in_end:
                if inorder[i] == postorder[post_end-1]:
                    break
                i += 1
            left_len = i-in_start
            root = TreeNode(inorder[i])
            root.left = build(inorder,in_start,i,postorder,post_start,post_start+left_len)
            root.right = build(inorder,i+1,in_end,postorder,post_start+left_len,post_end-1)
            return root
        return build(inorder,0,len(inorder),postorder,0,len(postorder))