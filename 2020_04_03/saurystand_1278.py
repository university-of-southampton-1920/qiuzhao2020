class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        memo = {}
        # calculate the cost of transferring one substring into palindrome string
        def cost(s, i, j):
            r  = 0
            while i < j:
                if s[i] != s[j]:
                    r += 1
                i += 1
                j -= 1
            return r
        def dfs(i, k):
            if (i, k) in memo: return memo[(i, k)]
            if n-i == k:
                # base case that each substring just have one character
                return 0
            if k == 1:
                # case that needs to transfer the whole substring into palidrome
                return cost(s, i, n-1)
            res = float('inf')
            for j in range(i+1, n-k+2):
                # keep making next part of substring into palidrome
                #compare different divisions to get the minimum cost
                res = min(res, dfs(j, k-1) + cost(s, i, j-1))
            memo[(i, k)] = res
            return res
        return dfs(0, k)# start from 0