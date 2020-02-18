class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def dfs(n, i):
            if n not in dic or dic[n]:
                return 0
            dic[n] = True
            s = dfs(n+1, i+1) + dfs(n-1, i+1) + 1 #从nums中存在的数字开始对前后进行搜索如果存在就会返回加一，不存在就会返回0
            return s   
        
        dic = {}
        for n in nums:
            dic[n] = False  #利用字典特性，把需要遍历的数字改为索引
        maxx = 0
        for n in nums:
            if not dic[n]:
                maxx = max(dfs(n, 1), maxx)
        
        return maxx