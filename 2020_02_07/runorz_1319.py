class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        connections = sorted(connections)
        label = [-1 for _ in range(n)]
        redun = 0
        index = 0
        for e in connections:
            if label[e[0]] == label[e[1]] and label[e[0]] >= 0:
                redun = redun + 1
                continue
            if label[e[0]] >= 0 and label[e[1]] >= 0:
                min_l = min(label[e[0]], label[e[1]])
                c = [label[e[0]], label[e[1]]]
                for i in range(len(label)):
                    if label[i] in c:
                        label[i] = min_l
                continue
            if label[e[0]] >= 0:
                label[e[1]] = label[e[0]]
                continue
            if label[e[1]] >= 0:
                label[e[0]] = label[e[1]]
                continue
            else:
                label[e[0]] = index
                label[e[1]] = index
                index = index + 1

        group = 0
        label = sorted(label)
        for i in range(len(label)):
            if label[i] == -1:
                group = group + 1
                continue
            if i == 0:
                group = group + 1
                continue
            if label[i] != label[i-1]:
                group = group + 1
        if group == 1:
            return 0
        if group-1 > redun:
            return -1
        if group-1 <= redun:
            return group-1
