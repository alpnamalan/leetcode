### AUG 2, 2025 -- P670: MAXIMUM SWAP ###

class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        last = {int(d): i for i, d in enumerate(s)} # (digit: index) dict
        for i, digit in enumerate(s):
            curr = int(digit)
            for d in range(9, curr, -1): # look for a larger digit 
                if d in last and last[d] > i: # it has to appear later for a good swap
                    j = last[d] 
                    s[i], s[j] = s[j], s[i] # swap old and new indices
                    return int(''.join(s))
        return num # if nothing changed
