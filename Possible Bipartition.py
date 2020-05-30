class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def dfs(i):
            open_list = [i]
            colors[i] = 1
            while open_list:
                i = open_list.pop()
                for v in connections[i]:
                    if v in colors:
                        if colors[v] != -colors[i]:return False
                    else:
                        colors[v] = -colors[i]
                        open_list.append(v)
            return True
        connections = collections.defaultdict(list)
        for a, b in dislikes:
            connections[a].append(b)
            connections[b].append(a)
        colors = {}
        for i in range(1, N+1):
            if i not in colors and not dfs(i):return False
        return True
  
