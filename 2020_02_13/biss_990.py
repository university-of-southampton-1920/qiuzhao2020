from collections import defaultdict, Counter
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        table = dict()
        for a, _, _, b in equations:
            table[a] = a
            table[b] = b
        for e in equations:
            if e[1] == "=":
                table[self.find(table, e[0])] = self.find(table, e[3])
        for e in equations:
            if e[1] == "!":
                if self.find(table, e[0]) == self.find(table, e[3]):
                    return False
        return True
    
    def find(self, table, x):
        if x != table[x]:
            table[x] = self.find(table, table[x])
        return table[x]