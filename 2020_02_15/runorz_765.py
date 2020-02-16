class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        group = list(row)
        for i in range(0,len(row),2):
            group[i] = i
            group[i+1] = i
        for i in range(0,len(row),2):
            if abs(row[i] - row[i+1]) == 1 and min(row[i], row[i+1]) % 2 ==0:
                continue
            else:
                if group[row[i]] > group[row[i+1]]:
                    temp = group[row[i]]
                    for j in range(len(group)):
                        if group[j] == temp:
                            group[j] = group[row[i+1]]
                else:
                    temp = group[row[i+1]]
                    for j in range(len(group)):
                        if group[j] == temp:
                            group[j] = group[row[i]]
        d = dict()
        for e in group:
            if not e in d:
                d[e] = 1
            else:
                d[e] = d[e] + 1
        result = 0
        for e in d:
            result = result + int(d[e]/2) - 1
        return result
