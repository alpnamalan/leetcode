### JULY 6, 2025 -- P392: IS SUBSEQUENCE ###

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        target = t
        for i in range(len(s)):
            if s[i] not in target:
                return False
            else:
                t_idx = target.index(s[i])
                target = target[t_idx + 1:]
        return True
        
