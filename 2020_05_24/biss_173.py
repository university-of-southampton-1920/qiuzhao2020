# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        stack = []
        while root:
            stack.append(root)
            root = root.left
        self.stack = stack

    def next(self) -> int:
        """
        @return the next smallest number
        """
        top = self.stack.pop()
        tmp = top.right
        while tmp:
            self.stack.append(tmp)
            tmp = tmp.left
        return top.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()