# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = ListNode(0)
        curr = pre
        carry = 0
        while l1 != None or l2 != None:
            if l1 == None:
                x = 0
            else:
                x = l1.val
            if l2 == None:
                y = 0
            else:
                y = l2.val
            sum_v = x + y + carry
            carry = sum_v // 10
            sum_v %= 10
            curr.next = ListNode(sum_v)
            curr = curr.next
            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next
        if carry == 1:
            curr.next = ListNode(carry)
        return pre.next