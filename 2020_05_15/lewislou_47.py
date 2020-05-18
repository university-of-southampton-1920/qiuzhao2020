class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtracking(first,curr):
            if (first == len(curr)-1) and (curr not in output):
                output.append(curr)
            for j in range(first,len(curr)):
                curr[j],curr[first] = curr[first],curr[j]
                backtracking(first+1,curr[:])
        backtracking(0,nums)
        return output