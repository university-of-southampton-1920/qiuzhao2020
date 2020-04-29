"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            
            return []
        
        q = collections.deque()
        q.append(root)
        ans = []
        
        while q:
            size = len(q)
            tmp = []
            
            for i in range(size):
                poped = q.popleft()
                tmp.append(poped.val)
                if poped.children:
                    for each in poped.children:
                        q.append(each)
            ans.append(tmp)
            
        return ans