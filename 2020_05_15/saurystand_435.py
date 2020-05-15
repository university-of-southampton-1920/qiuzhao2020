class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        return n - self.intervalSchedule(intervals)

    def intervalSchedule(self, intvs):
        if len(intvs) == 0:
            return 0
        #intvs = sorted(intvs)
        intvs = sorted(intvs, key=lambda x:x[1])
        count = 1
        x_end = intvs[0][1]
        for inv in intvs:
            start = inv[0]
            if start >= x_end:
                count += 1
                x_end = inv[1]
        return count
