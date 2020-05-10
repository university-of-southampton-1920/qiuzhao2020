# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None: return True

        # slow = ListNode(head)
        # fast = ListNode(head)
        # while fast != None and fast.next != None:
        #     slow = slow.next
        #     fast = fast.next.next
        # if fast != None: #if its odd
        #     slow = slow.next
        # left = head
        # right = self.traverse(slow)

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = self.reverse(slow.next)
        slow.next = None
        left = head

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def reverse(self, head):
        if not head or not head.next:
            return head
        last = None
        while head:
            temp = head.next
            head.next = last
            last = head
            head = temp
        return last

        # newH = None
        # p = head
        # while p:
        #     p.next, p, newH = newH, p.next, p
        # return newH

        # wrong reverse
        # prev = ListNode(None)
        # next = ListNode(None)
        # curr = head
        # while curr != None:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        # return prev

