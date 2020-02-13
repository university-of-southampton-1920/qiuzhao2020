class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        union = {}
        queue = [n for n in equations if n[1]=='='] + [n for n in equations if n[1]=='!'] #O(N)
        def find(x):
            if union[x] != x: union[x] = find(union[x]) 
            return union[x]
        def unite(x,y):
            union[find(y)] = find(x)  #set x 和 y字典值相等
            
        for A,relation1,relation2,B in queue:   #O(N)
            union.setdefault(A,A)
            union.setdefault(B,B)            
            if relation1 == '!':
                if find(A) == find(B):
                    return False
            else:
                unite(A,B)    
        return True

                
            