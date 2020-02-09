from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        q = deque()
        d = dict() # value: [i1, i2, i3]
        for i, n in enumerate(arr):
            if not (n in d):
                d[n] = [i]
            else:
                d[n].append(i)
        visite = [False for i in range(len(arr))]
        q.append( (0, 0) )
        res = 0
        while len(q) != 0:
            index, c = q.popleft()
            visite[index] = True
            if index == len(arr) - 1:
                res = c
                break

            # i + 1 action
            if index + 1 < len(arr) and (not visite[index+1]):
                q.append( (index + 1, c+1) )
            if index - 1 >= 0 and (not visite[index-1]):
                q.append( (index - 1, c+1) )
            for next_index in d[arr[index]]:
                if not visite[next_index]:
                    q.append( (next_index, c+1) )
            d[arr[index]] = []
        return res