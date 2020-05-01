# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #         # 每次 O(K)O(K) 比较 K个指针求 min, 时间复杂度：O(NK)O(NK)
        #         # 超时
        #         k = len(lists)
        #         dummy = ListNode(0)
        #         tail = dummy
        #         while True:
        #             minNode = None
        #             minPoint = -1
        #             for i in range(k):
        #                 if lists[i] == None:
        #                     continue
        #                 if minNode == None or lists[i].val < minNode.val:
        #                     minNode = lists[i]
        #                     minPoint = i
        #             if minPoint == -1:
        #                 break
        #             tail.next = minNode
        #             tail = tail.next
        #             lists[minPoint] = lists[minPoint].next

        #         return dummy.next

        if not lists: return
        k = len(lists)
        return self.merge(lists, 0, k - 1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwo(l1, l2)

    def mergeTwo(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwo(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwo(l1, l2.next)
            return l2



