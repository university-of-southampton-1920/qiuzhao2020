class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        #failed answer
#         viralMap = set()
#         for node in initial:
#             viralMap.add((node, True))
        
#         initial = sorted(initial)
#         maxChange = 0
#         nodeMax = initial[0]
        
#         for node in initial:
#             viralMap.add((node, False))
#             visited = [False] * len(graph)
#             change = self.find(graph, node, viralMap, 0, visited)
#             if change > 0 and change > maxChange:
#                 maxChange = change
#                 nodeMax = node
#             viralMap.add((node, True))
#         return nodeMax
    
#     def find(self, graph, node, viralMap, count, visited):
#         visited[node] = True
#         if node in viralMap and viralMap.get(node) == True:
#             return -1
#         maxc = count
#         unions = graph[node]
#         ulength = len(unions)
#         for i in range(ulength - 1):
#             i += 1
#             if unions[i] == 1 and i != node:
#                 if not visited[i]:
#                     viralFound = self.find(graph, i ,viralMap, count + 1, visited)
#                      if viralFound == -1:
#                         return -1
#                     maxc = max(viralFound, maxc)
#         return maxc
        
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
                    
                    
                    
                    
                    
                    