# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next != None and head.val == head.next.val:
            while head.next != None and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
        return head

        # if head is None:
        #     return None
        # fakehead = ListNode(0)
        # fakehead.next = head
        # prev = fakehead
        # curr = head
        # while curr is not None:
        #     while curr.next is not None and curr.val == curr.next:
        #         curr = curr.next
        #     if prev.next == curr:
        #         prev = prev.next
        #     else:
        #         prev.next = curr.next
        #     curr = curr.next
        # return fakehead.next

    # class Solution:
    #     def deleteDuplicates(self, head: ListNode) -> ListNode:
    #         dummy = pre = ListNode(0)  # 为了处理链表的第一个数值，设置的虚拟0。pre和dummy一样！
    #         dummy.next = head
    #         while head and head.next:
    #             if head.val == head.next.val:
    #                 while head and head.next and head.val == head.next.val:
    #                     head = head.next  # 需要一步一步的跳
    #                 head = head.next  # 把下一个跳掉，直接连接 下一个的下一个
    #                 pre.next = head
    #             else:
    #                 pre = pre.next
    #                 head = head.next
    #         return dummy.next