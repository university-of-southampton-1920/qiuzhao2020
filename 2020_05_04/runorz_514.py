class Solution:
    def finding(self, ring, key, dp, index):
        if ring in dp and dp[ring][index] != -1:
            return dp[ring][index]
        else:
            if not ring in dp:
                dp[ring] = [-1 for _ in range(len(key))]
            left_step = 0
            for i in range(len(ring)):
                if ring[i] == key[index]:
                    break
                left_step += 1
            right_step = 1
            for i in range(len(ring)-1, -1, -1):
                if ring[i] == key[index]:
                    break
                right_step += 1
                
                
            if index == len(key) - 1:
                if left_step <= right_step:
                    dp[ring][index] = left_step + 1
                    return left_step+1
                else:
                    dp[ring][index] = right_step+1
                    return right_step+1
            else:
                dp[ring][index] = min(left_step+1+self.finding(ring[left_step:]+ring[0:left_step], key, dp, index+1), right_step+1+self.finding(ring[len(ring)-right_step:]+ring[0:len(ring)-right_step], key, dp, index+1))
                return dp[ring][index]
                
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = dict()
        res = self.finding(ring, key, dp, 0)
        return res
