class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9+7
        A0L0, A1L0, A0L1, A1L1, A0L2, A1L2 = 1, 1, 1, 0, 0, 0
        for _ in range(2,n+1):
            A0L0, A1L0, A0L1, A1L1, A0L2, A1L2 = (
                (A0L0 + A0L1 + A0L2) % MOD,
                (A0L0 + A1L0 + A0L1 + A1L1 + A0L2 + A1L2) % MOD,
                A0L0,
                A1L0,
                A0L1,
                A1L1,
            )
        return (A0L0 + A1L0 + A0L1 + A1L1 + A0L2 + A1L2) % MOD