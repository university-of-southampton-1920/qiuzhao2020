# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        node_first=None
        node_last=None
        current=head
        count=1
        if m==1:
            node_first=head
            prev_node=head
            while current:
                if count==n:
                    node_last=current.next
                count+=1
                current=current.next
        else:
            while current:
                if count==m-1:
                    prev_node=current
                    node_first=current.next
                if count==n:
                    node_last=current.next
                count+=1
                current=current.next
            
            #print(node_first.val)
            #print(node_last.val)
            #print(prev_node.val)
            
        prev=node_last
        current=node_first
        while current!=node_last:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        
        if m==1:
            return prev
        else:
            prev_node.next=prev
            return head
                
                