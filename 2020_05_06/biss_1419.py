class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        arr = [[] for i in range(5)]
        # 0:c, 1:r, 2:o, 3:a, 4:k
        res = 0
        for s in croakOfFrogs:
            if s == "c":
                arr[0].append(s)
            elif s == "r":
                if len(arr[0]) == 0:
                    return -1
                arr[0].pop()
                arr[1].append(s)
            elif s == "o":
                if len(arr[1]) == 0:
                    return -1
                arr[1].pop()
                arr[2].append(s)
            elif s == "a":
                if len(arr[2]) == 0:
                    return -1
                arr[2].pop()
                arr[3].append(s)
            else:
                if len(arr[3]) == 0:
                    return -1
                arr[3].pop()
            res = max(res, len(arr[0]) + len(arr[1]) + len(arr[2]) + len(arr[3]))
        for a in arr:
            if len(a) != 0:
                return -1
        return res