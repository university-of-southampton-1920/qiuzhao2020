class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(),key=counts.get)
		
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.defaultdict(int)
        for i in nums:
            count[i] += 1
        return max(count,key=count.get)