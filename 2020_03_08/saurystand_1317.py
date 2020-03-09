class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        A = 1
        while True:
            B = n - A
            if self.checkZero(A) and self.checkZero(B):
                return [A,B]
            A += 1
    
    def checkZero(self, n):
        if '0' in str(n):
            return False
        else:
            return True
        # while n > 0:
        #     t = n % 10  
        #     if t == 0:
        #         return True
        #     n /= 10
        # return False


# class Solution:
#     def findTheLongestSubstring(self, s: str) -> int:
#         ss = {0:-1}
#         res = 0
#         d = {"a":1, "e": 2, "i":4, "o": 8, "u":16}
#         cur = 0
#         for i in range(len(s)):
#             if s[i] in d:
#                 cur ^= d[s[i]]
#                 if cur in ss:
#                     res = max(res, i - ss[cur])
#                 else:
#                     ss[cur] = i
#             else:
#                 res = max(res, i - ss[cur])
#         return res