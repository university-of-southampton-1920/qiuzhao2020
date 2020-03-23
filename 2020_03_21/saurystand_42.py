from queue import Queue


class Solution:
    def trap(self, height: List[int]) -> int:
        waterlevel = []
        left = 0
        right = 0
        for h in height:
            left = max(left, h)
            waterlevel += [left]  # it said: over-fill it into height
        for i, h in reversed(list(enumerate(height))):
            right = max(right, h)
            waterlevel[i] = min(waterlevel[i], right) - h
        return sum(waterlevel)

        # time limit issue
        # if len(height) == 0: return 0
        # a = len(height)
        # s = Queue()
        # i = 0
        # maxwater = 0
        # maxbotwater = 0
        # while i < a:
        #     if s is None or height[i] < height[s.get()]:
        #         s.put(i)
        #         i += 1
        #     else:
        #         bot = s.pop()
        #         if s is None:
        #             maxbotwater = 0
        #         else:
        #             maxbotwater = min(height[s.get()], height[i] - height[bot]) * (i - s.get() - 1)
        #             maxwater += maxbotwater
        # return maxwater