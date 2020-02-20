class Solution:
    def minMalwareSpread(self, graph, initial):        
        parent = [u for u in range(len(graph))]
        size = [1 for u in range(len(graph))]
        inits = set(initial)
        sizeinf = [(1 if u in inits else 0) for u in range(len(graph))]

        for u in range(len(graph)):
            for v in range(u + 1, len(graph[u])):
                if graph[u][v]:
                    pu,pv = self.get(u,parent),self.get(v,parent)
                    if size[pu] > size[pv]:
                        pu,pv = pv,pu
                    if pu != pv:
                        parent[pu] = pv
                        size[pv] += size[pu]
                        sizeinf[pv] += sizeinf[pu]
                        
        
        return min([ (-size[self.get(u,parent)], u) for u in inits if sizeinf[self.get(u,parent)] == 1] or [(0,uu) for uu in initial])[1]
                
    def get(self, u , parent):
        if u!= parent[u]:
            parent[u] = self.get(parent[u],parent)
        return parent[u]
        