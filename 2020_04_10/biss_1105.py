class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        books = [0] + books
        dp = [10**8 for i in range(len(books))]
        dp[0] = 0
        for i in range(1, len(books)):
            maxw = 0
            maxh = 0
            for j in range(i, 0, -1):
                maxw += books[j][0]
                maxh = max(maxh, books[j][1])
                if maxw > shelf_width:
                    break
                dp[i] = min(dp[i], dp[j-1] + maxh)
        # print(dp)
        return dp[len(books)-1]