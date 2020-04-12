class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            elif stack[-1][1] + 1 < k:
                stack[-1][1] += 1
            else:
                stack.pop()
        res = ''
        for c, l in stack:
            res += c * l
        return res

#         n = len(s)
#         length = -1

#         while length != n:
#             length = n
#             count = 1
#             for i in range(n):
#                 if i == 0 or s[i] != s[i-1]:
#                     count = 1
#                 count += 1
#                 if count == k:
#                     s.replace(s[i - count + 1:i + 1], '')
#                     break
#         return s