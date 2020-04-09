class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        dp = [0 for _ in range(len(books)+1)]
        dp[0] = 0
        dp[1] = books[0][1]
        for i in range(2, len(books)+1):
            dp[i] = dp[i-1] + books[i-1][1]
            for j in range(i-2, -1, -1):
                s = 0
                max_h = 0
                for k in range(j, i):
                    s += books[k][0]
                    max_h = max(max_h, books[k][1])
                if s > shelf_width:
                    break
                else:
                    dp[i] = min(dp[i], max_h + dp[j])
        return dp[-1]
