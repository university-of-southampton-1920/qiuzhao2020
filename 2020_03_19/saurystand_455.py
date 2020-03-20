class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        i = 0
        res = 0
        if len(s) == 0:
            return 0
        for n in s:
            if n >= g[n]:
                res += 1
                i += 1
        return res

# int i = 0;
# for(int j=0;i<g.length && j<s.length;j++) {
# 	if(g[i]<=s[j]) i++;
# }
# return i;