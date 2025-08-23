### AUG 17, 2025 -- P76: MINIMUM WINDOW SUBSTRING ###

class Solution:   
    from collections import Counter
    def minWindow(self, s: str, t: str) -> str:
        """ INTUITION: Think in terms of 'deficit' """
        need, missing = Counter(t), len(t)
        st, e, ln = -1, -1, len(s)+1 # start & end indices
        l = 0
        for r, ch in enumerate(s):
            need[ch] -= 1
            if need[ch] >= 0:
                missing -= 1
            while missing == 0: # (missing == 0) == covers
                if (r-l+1) < ln: 
                    ln = r-l+1
                    st, e = l, r
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1 
        return "" if st == -1 else s[st:e+1]
