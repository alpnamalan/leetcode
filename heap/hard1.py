### AUG 10, 2025 -- P295: FIND MEDIAN FROM DATA STREAM ###

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        from collections import Counter
        ctr = Counter(words)
        middle = False
        length = 0
        for syl in list(ctr.keys()):
            comp = syl[1]+syl[0]
            if comp == syl: # either same or another copy
                incr = ctr[syl] // 2
                length += incr*4
                ctr[syl] -= incr*2
                if ctr[syl] == 1:
                    middle = True
                    ctr[syl] -= 1
            elif comp in ctr: 
                incr = min(ctr[syl], ctr[comp])
                length += incr*4
                ctr[syl] -= incr
                # if ctr[syl] == 0: del ctr[syl]
                ctr[comp] -= incr
                # if ctr[comp] == 0: del ctr[comp]
        if middle: length += 2
        return length
