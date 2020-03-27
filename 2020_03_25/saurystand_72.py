class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1) + 1, len(word2) + 1
        pre = [0 for _ in range(l2)]
        for j in range(l2):
            pre[j] = j
        for i in range(1, l1):
            cur = [i] * l2
            for j in range(1, l2):
                cur[j] = min(cur[j - 1] + 1, pre[j] + 1, pre[j - 1] + (word1[i - 1] != word2[j - 1]))
            pre = cur[:]
        return pre[-1]
#         l1 = len(word1)
#         l2 = len(word2)

#         if (l1 + l2) == 0:
#             return 0
#         if l1 + l2 <=2:
#             if l1 + l2 == 1:
#                 return 1
#             elif l1 == 1 and l2 == 1 and word1 != word2:
#                 return 1
#             elif l2 == 1 or l1 == 1:
#                 return 0
#             return 1

#         if word1 == word2:
#             return 0
#         f = [0] * (l2 + 1)
#         for i in range(1, l2):
#             f[i] = i

#         for i in range(1, l1):
#             prev = i
#             for j in range(1, l2):
#                 curr = 0
#                 if word1[i-1] == word2[j-1]:
#                     curr = f[j-1]
#                 else:
#                     curr = min(min(f[j-1], prev), f[j]) + 1
#                 f[j-1] = prev
#                 prev = curr
#             f[l2] = prev
#         return f[l2]