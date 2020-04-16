class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = []
        self.total = 0
        for i in nums:
            self.total += i
            self.dp.append(self.total)

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.dp[j]
        return self.dp[j] - self.dp[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)