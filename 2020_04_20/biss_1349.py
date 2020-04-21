class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        row = len(seats)
        col = len(seats[0])
        N = (1<<col)
        dp = [[0 for j in range(N)] for i in range(row)]
        for i in range(row):
            for cur in range(N):
                if self.self_ok(seats, i, cur):
                    if i == 0:
                        dp[i][cur] = max(dp[i][cur], self.count(cur))
                    else:
                        for pre in range(N):
                            if self.self_ok(seats, i-1, pre) and self.cross_ok(cur, pre, col):
                                dp[i][cur] = max(dp[i][cur], dp[i-1][pre]+self.count(cur))
        res = 0
        for i in range(N):
            res = max(res, dp[row-1][i])
        return res
    def self_ok(self, seats, row, cur):
        N = len(seats[row])
        tmp = []
        for i in range(N):
            tmp.append(cur%2)
            cur >>=1
        for i in range(N):
            if tmp[i] == 1 and seats[row][i] == "#":
                return False
            if tmp[i] == 1 and i-1 >=0 and tmp[i-1] == 1:
                return False
        return True
    
    def cross_ok(self, cur, pre, N):
        tmp1 = []
        tmp2 = []
        for i in range(N):
            tmp1.append(cur%2)
            tmp2.append(pre%2)
            cur >>= 1
            pre >>= 1
        for i in range(N):
            if tmp1[i] == 1 and i-1 >= 0 and tmp2[i-1] == 1:
                return False
            if tmp1[i] == 1 and i+1 < N and tmp2[i+1] == 1:
                return False
        return True
        
    def count(self, cur):
        res = 0
        while cur != 0:
            res += cur%2
            cur>>=1
        return res