class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ss = {0:-1}
        res = 0
        d = {"a":1, "e": 2, "i":4, "o": 8, "u":16}
        cur = 0
        for i in range(len(s)):
            if s[i] in d:
                cur ^= d[s[i]]
                if cur in ss:
                    res = max(res, i - ss[cur])
                else:
                    ss[cur] = i
            else:
                res = max(res, i - ss[cur])
        return res