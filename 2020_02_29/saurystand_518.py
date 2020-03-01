class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin,amount + 1):
                dp[i] += dp[i - coin]
        print(dp)
        return dp[amount]


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         dp = [0 for i in range(amount+1)]
#         dp[0] = 1
#         for c in coins:
#             for j in range(amount+1):
#                 if j - c >= 0:
#                     dp[j] += dp[j - c]
#         print(dp)              
#         return dp[amount]