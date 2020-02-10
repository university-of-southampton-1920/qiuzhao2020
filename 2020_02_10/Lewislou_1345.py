class Solution:
    def minJumps(self, arr: List[int]) -> int:
        import collections
        nei = collections.defaultdict(list)
        _ = [nei[x].append(i) for i, x in enumerate(arr)]# dict[100:{0,4},-23:{1,2}...]
        frontier = collections.deque([(0,0)]) #新建queue
        num_met, pos_met = set(), set()
        while frontier:
            pos, step = frontier.popleft() # state: position, step； popleft() 队首元素出队列
            if pos == len(arr) - 1: 
                return step
            num = arr[pos]
            pos_met.add(pos) # track explored positions
            for p in [pos - 1, pos + 1] + nei[num] * (num not in num_met):
                if p in pos_met or not 0 <= p < len(arr): continue
                frontier.append((p, step + 1))
            num_met.add(num) # track explored values
        