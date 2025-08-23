### AUG 17, 2025 -- P399: EVALUATE DIVISION ###

class Solution:
    from collections import defaultdict
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """ 1. SET UP THE GRAPH """
        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            v1, v2 = eq # v1 = values[i] * v2
            graph[v1].append((v2, values[i]))
            graph[v2].append((v1, 1 / values[i]))
        """ 2. DEFINE DFS FUNC SPECIFIC TO THE PROBLEM """
        def dfs(val, coef, target, visited):
            if val == target:
                return coef
            visited.add(val)
            for v, cf in graph[val]:
                if v not in visited:
                    res = dfs(v, coef*cf, target, visited) #
                    if res != -1.0: return res #
            return -1.0 # dead end
        """ 3. EVALUATE EACH QUERY """
        out = []
        for q1, q2 in queries:
            if q1 not in graph or q2 not in graph: #
                out.append(-1.0)
            else:
                out.append(dfs(q1, 1.0, q2, set()))
        return out
