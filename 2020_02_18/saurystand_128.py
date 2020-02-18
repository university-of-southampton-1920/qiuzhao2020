class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)# n*log(n)
        count = 0
        nlength = len(nums)
        if nlength == 0:
            return 0
        duplicate = 0 # for duplicate consecutive element
        base = 0 # which is the first element index
        for i in range(nlength):
            if nums[i] != nums[base] + (i - base) - duplicate:
                if nums[i] == nums[i-1]:
                    duplicate += 1
                else:
                    count = max(count, i - base - duplicate)
                    base = i #i th element
                    duplicate = 0 # no duplicate
        return max(count, nlength - base -duplicate)

    
       # dict = {x: False for x in nums}
       #  maxlen = 1
       #  for i in dict:
       #      if dict[i] == False:
       #          temp_streak = i - 1
       #          lenleft = 0
       #          while temp_streak in dict:
       #              lenleft += 1
       #              dict[temp_streak] = True
       #              temp_streak -= 1
       #          current_streak = i + 1
       #          lenright = 0
       #          while current_streak in dict:
       #              lenright += 1
       #              dict[current_streak] = True
       #              current_streak += 1
       #      maxlen = max(maxlen, lenleft+lenright)     
       #  return maxlen
               
#         mySet = set()
#         for i in nums:
#             mySet.add(i)
        
#         longest = 0
#         for i in nums:
#             length = 1
#             for j in range(len(mySet)):
#                 if j in mySet:
#                     mySet.remove(j)
#                     length += 1
#                 j -= 1
#             for j in range(len(mySet)):
#                 if j in mySet:
#                     mySet.remove(j)
#                     length += 1
#                 j += 1
#             longest = max(longest, length)
#         return longest








# other answer
# from collections import Counter
# class Solution:  
#     def __init__(self):
#         self.t = {}
    
#     def longestConsecutive(self, nums: List[int]) -> int:
#         # init
#         if nums == []:
#             return 0
#         self.t = {i:i for i in nums}
#         for n in nums:
#             if n-1 in self.t:
#                 self.union(n, n-1)
#             if n+1 in self.t:
#                 self.union(n, n+1)
#         c = Counter()
#         for k in self.t:
#             c[self.find(k)] += 1
#         return c.most_common()[0][1]
            
#     def find(self, x):
#         # O(1)
#         if self.t[x] != x:
#             self.t[x] = self.find(self.t[x])
#         return self.t[x]
    
#     def union(self, x, y):
#         self.t[self.find(x)] = self.find(y)