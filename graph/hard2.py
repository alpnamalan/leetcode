### AUG 7, 2025 -- P2246: LONGEST PATH WITH DIFFERENT ADJACENT CHARACTERS ###

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # First build a tree
        from collections import defaultdict
        tree = defaultdict(list)
        for i, p in enumerate(parent): # i->node; p->parent
            if p != -1: tree[p].append(i)
        # Longest path -> DFS
        longest = 1
        def dfs(node):
            nonlocal longest # make it mutable
            child1 = child2 = 0 
            # can go child1->node->child2
            # child1: best child path, child2: second best
            for child in tree[node]:
                child_len = dfs(child)
                if s[child] != s[node]: 
                    # extend the path if diff char
                    # if same char, child1 & child2 are automatically zeroed
                    if child_len > child1:
                        child1, child2 = child_len, child1
                    elif child_len > child2:
                        child2 = child_len
            longest = max(longest, child1+child2+1)
            return child1+1 # add curr node to the best child path
        dfs(0)
        return longest
