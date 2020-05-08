class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        memo = [0 for i in range(len(arr))]
        for i in range(len(arr)):
            self.dfs(i, d, arr, memo)
        return max(memo)
    
    def dfs(self, cur_i, d, arr, memo):
        if memo[cur_i]:
            return memo[cur_i]
        last_i = len(arr)-1
        depth = 1
        # to right and find the best index 
        for i in range( min(last_i, cur_i+1), min(last_i, cur_i+d)+1 ):
            if arr[cur_i] <= arr[i]:
                break
            depth = max(1 + self.dfs(i, d, arr, memo), depth)
        
        # to left
        for i in range( max(0, cur_i-1), max(0, cur_i-d)-1, -1 ):
            if arr[cur_i] <= arr[i]:
                break
            depth = max(1 + self.dfs(i, d, arr, memo), depth)
        memo[cur_i] = depth
        return depth