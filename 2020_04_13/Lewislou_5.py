class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        for i in range(len(s), 0, -1):
            for j in range(len(s)-i+1):
                if s[j:j+i] == s[j:j+i][::-1]: ##[::-1]意思是倒序 搜索长度从全部长度到长度为0的所有可能集合
                    return s[j:j+i]