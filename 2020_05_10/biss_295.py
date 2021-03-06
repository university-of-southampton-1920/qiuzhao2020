import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = [10**8]
        self.min_heap = [10**8]

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            if num >= -self.min_heap[0]:
                heapq.heappush(self.max_heap, num)
            else:
                heapq.heappush(self.min_heap, -num)
                heapq.heappush(self.max_heap, -self.min_heap[0])
                heapq.heappop(self.min_heap)
        else:
            if num < self.max_heap[0]:
                heapq.heappush(self.min_heap, -num)
            else:
                heapq.heappush(self.max_heap, num)
                heapq.heappush(self.min_heap, -self.max_heap[0])
                heapq.heappop(self.max_heap)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0] + (-self.min_heap[0]) ) / 2
        else:
            return self.max_heap[0]