class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        res = tmp = 0
        keep = {}
        for j in range(len(s)):
            if s[j] in keep.keys():
                i = keep[s[j]]
            else:
                i = -1
            keep[s[j]] = j
            if tmp < (j-i):
                tmp = tmp + 1
            else:
                tmp = j-i
            res = max(res,tmp)
        return res
