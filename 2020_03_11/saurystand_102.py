# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# from queue import Queue
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root: return []
        queue, res = deque([root]), []
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res

        # time limit exceeded
        # queue = Queue()
        # wraplist = []
        # if root == None:
        #     return wraplist
        # queue.put(root)
        # while queue.qsize() != 0:
        #     levelNum = queue.qsize()
        #     sublist = set()
        #     for i in range(levelNum):
        #         if queue.get().left != None:
        #             queue.put(queue.get().left)
        #         if queue.get().right != None:
        #             queue.put(queue.get().right)
        #         sublist.add(queue.poll().val)
        # return wraplist