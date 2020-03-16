class Solution:  # donot finish because of the 0 element corners case
    def splitArraySameAverage(self, A: List[int]) -> bool:
        total = sum(A)
        if total == 0:
            if len(A) % 2 == 0: return True
            else: return False
        dp = [0 for j in range(total+1)]
        dp[0] = 1
        cur_s = 0
        for a in A:
            cur_s += a
            for s in range(cur_s, a-1, -1):
                # total * num == s * len(A)
                dp[s] |= (dp[s - a] << 1)
                if (s * len(A)) % total == 0:
                    num = int(s * len(A) / total)
                    # print(s, len(A), total,num,  dp)
                    if num != 0 and num != len(A) and  ((dp[s] >> num) & 1): return True   
        # print(dp)
        return False