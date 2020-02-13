class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        unequal_equations = list()
        group = dict()
        i = 0
        for e in equations:
            if e[0] == e[-1] and e[1] == '!':
                return False
            if e[1] == '=':
                if not e[0] in group and not e[-1] in group:
                    group[e[0]] = i
                    group[e[-1]] = i
                    i = i + 1
                elif e[0] in group and not e[-1] in group:
                    group[e[-1]] = group[e[0]]
                elif not e[0] in group and e[-1] in group:
                    group[e[0]] = group[e[-1]]
                    
                elif group[e[0]] != group[e[-1]]:
                    min_index = min(group[e[0]], group[e[-1]])
                    max_index = max(group[e[0]], group[e[-1]])
                    for g in group:
                        if group[g] == max_index:
                            group[g] = min_index
            else:
                unequal_equations.append(e)
        
        conflict = list()
        print(group)
        print(unequal_equations)
        for u in unequal_equations:
            if not u[0] in group and not u[-1] in group:
                group[u[0]] = i
                i = i + 1
                group[u[-1]] = i
                i = i + 1
                conflict.append((group[u[0]], group[u[-1]]))
            elif u[0] in group and not u[-1] in group:
                group[u[-1]] = i
                i = i + 1
                conflict.append((group[u[0]], group[u[-1]]))
            elif not u[0] in group and u[-1] in group:
                group[u[0]] = i
                i = i + 1
                conflict.append((group[u[0]], group[u[-1]]))
            elif u[0] in group and u[-1] in group:
                if group[u[0]] == group[u[-1]]:
                    return False
                else:
                    conflict.append((group[u[0]], group[u[-1]]))

        return True
