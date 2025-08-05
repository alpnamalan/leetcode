### AUG 5, 2025 -- P923: 3SUM WITH MULTIPLICITY ###

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        from collections import Counter
        from math import comb
        MOD = 10**9 + 7
        cts = Counter(arr)
        keys = sorted(cts)
        total = 0
        for i, x in enumerate(keys): # First num in triplet
            for j, y in enumerate(keys[i:], start=i): # Second number, ≥ x
                z = target - x - y 
                if z < y or z not in cts: # Ensure x ≤ y ≤ z and z exists
                    continue
                # Frequencies of x, y, and z
                fx, fy, fz = cts[x], cts[y], cts[z]
                # Gotta apply diff approaches for diff scenarios
                if x == y == z:
                    total += comb(fx, 3)
                elif x == y != z:
                    total += comb(fx, 2) * fz
                elif x < y == z:
                    total += fx * comb(fy, 2)
                elif x < y < z:
                    total += fx * fy * fz
        return total % MOD
