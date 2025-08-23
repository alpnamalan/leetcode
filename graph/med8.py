### AUG 16, 2025 -- P433: MINIMUM GENETIC MUTATION ###

class Solution:
    from collections import deque
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Initial checks && cast bank as set for O(1) lookups
        if startGene == endGene: return 0
        bank = set(bank)
        if endGene not in bank: return -1
        # Use BFS
        bases = ['A', 'T', 'G', 'C']
        q = deque([(startGene, 0)])
        seen = {startGene}
        while q:
            gene, muts = q.popleft()
            for i in range(8):
                for b in bases:
                    if b == gene[i]: continue # skip if same base
                    cand = gene[:i] + b + gene[i+1:]
                    if cand == endGene: return muts+1
                    if cand in bank and cand not in seen:
                        q.append((cand, muts+1)); seen.add(cand)
        return -1
