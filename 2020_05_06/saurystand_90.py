class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        n = len(nums)
        nums = sorted(nums)
        res = []

        def dfs(i, temp):
            res.append(temp)
            if i == n:
                return
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:  # 去重
                    continue
                dfs(j + 1, temp + [nums[j]])

        dfs(0, [])
        return res

#         n = len(nums)
#         res = []
#         visited = [0] * n
#         if not nums:
#             return
#         def backtrack(track, length):
#             if length == n:
#                 res.append(track)
#                 return
#             for i in range(n):
#                 if visited[i]:
#                     continue
#                 visited[i] = 1
#                 backtrack(track + [nums[i]], length + 1)
#                 visited[i] = 0  # 回溯
#         backtrack([], 0)
#         return re
