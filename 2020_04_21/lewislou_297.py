# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return 'Null'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        
        return str(root.val)+','+left+','+right
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def DFS(Queue):
            if Queue[0] == 'Null':# if X is found it's removed from queue
                Queue.popleft() 
                return
            root = TreeNode(Queue.popleft())      #make current node as the root
            l = DFS(Queue)           #DFS on left subtree
            r = DFS(Queue)           #DFS on rigtt subtree
            root.left = l
            root.right = r
            return root
        data = data.split(',')      # Split the data by ',' (This handles negative values too)
        queue = collections.deque(data)    
        return DFS(queue)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))