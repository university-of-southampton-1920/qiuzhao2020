from functools import lru_cache
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty): return -1
        arr = jobDifficulty
        
        @lru_cache(None)
        def helper(st, k):           
		    # only one day left so we have to finish rest of the unfinished jobs 
            if k == 1: 
                return max(arr[st:]) 
            
			# cur_max is max from i to j'th index, which is value on k'th day
            cur_max, ret = 0, float('inf')
            for i in range(st,len(arr)-k+1):
                cur_max = max(cur_max, arr[i])
                ret = min(ret, cur_max + helper(i+1, k - 1))                
            return ret
        
        return helper(0, d)