### AUG 14, 2025 -- P207: COURSE SCHEDULE ###

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # in req: key is a prereq for its values
        from collections import defaultdict
        graph = defaultdict(list)
        for c, pre in prerequisites:
            graph[pre].append(c)

        """ NOW BASICALLY --> DETECT CYCLE IN GRAPH USING DFS """
        # curr: on the current DFS path
        # safe: fully processed and now safe
        curr, safe = set(), set()
        def dfs(u):
            if u in curr: return False
            if u in safe: return True
            curr.add(u) # --> Enter this node's recursion path
            for v in graph[u]:
                if not dfs(v): return False
            curr.remove(u) # --> Leaving this path
            safe.add(u) # --> Fully processed with no cycles
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
