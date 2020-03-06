class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        val_index = {x:i for i, x in enumerate(A)}
        length = len(A)
        # dp table is the length of longest fb ends with A[i], A[j]
        result = 0
        dp = [[2 for i in range(0, length)] for j in range(0, length)]
        for end in range(0, length):
            for start in range(0, end):
                possible_pre = A[end] - A[start]
                if possible_pre in val_index and possible_pre < A[start]:
                    dp[end][start] = dp[start][val_index[possible_pre]]+1
                    result = max(result, dp[end][start])
                    
        
        return result if result >= 3 else 0 