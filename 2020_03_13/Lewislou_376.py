class Solution(object):
    def wiggleMaxLength(self, nums):
        ## O(n) solution
        
        if not nums:
            return 0
        if len(nums)<2:
            return 1
        
        last_num = nums[0]
        state=None
        length=1
        
        for i in range(1,len(nums)):
            if nums[i]!=last_num:
                if last_num>num[i]:
                    if state=="up" or state==None:
                        state="down"
                        length +=1
                        last_num = nums[i]
                    else: #state=="down"
                        last_num = min(last_num, nums[i])
                else:
                    if state=="down" or state==None:
                        state="up"
                        length +=1
                        last_num = nums[i]
                    else: #state=="up"
                        last_num = max(last_num, nums[i])
        return length