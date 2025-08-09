### AUG 7, 2025 -- P2285: MAXIMUM TOTAL IMPORTANCE OF ROADS ###

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # The gist is that the more roads that lead to a city
        # the higher value it should have
        from collections import defaultdict
        freq = defaultdict(int)
        for rd in roads:
            freq[rd[0]] += 1
            freq[rd[1]] += 1
        sfreq = sorted(freq.items(), key=lambda x:x[1])
        # now importances [1,2,..,n] correspond with sfreq
        maxval = 0
        # some cities may be isolated so you might need to skip
        # some values
        st = n-len(sfreq)
        for i in range(st ,n): 
            maxval += (i+1) * sfreq[i-st][1]
        return maxval
