"""
Name: byroncbr_203.py
Author: bangrenc
Time: 7/3/2020 10:03 AM
"""

# No complete

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        dummy_head = ListNode(-1)  # 从-1开始，后面就是输入的数组
        dummy_head.next = head

        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next  # 如果下一个a和下下一个b相等，那直接指向b，这样就可以删除掉a了！
            else:
                current_node = current_node.next  # 不相等，指向下一个数

        return dummy_head.next  # 返回，但除掉第一个数-1.






