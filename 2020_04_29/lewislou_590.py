"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root: return ans
        
        stack = []
        stack.append(root)
        
        while stack:
            temp = []
            node = stack.pop()
            temp.append(node.val)
            #print(temp)
            
            for child in node.children:
                #print(child.val)
                stack.append(child)
            
            ans = temp + ans
            
        return ans