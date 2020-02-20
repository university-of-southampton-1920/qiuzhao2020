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
		
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set: #确保没有重复判断的值 hashset查找只需要O(1)复杂度
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set: #为什么复杂度为O(n+n)因为外循环最多n次而，在那种情况下内循环每次只有可能为1因为没有加一还在nums中的情况了，实际上只有n+n最多
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak