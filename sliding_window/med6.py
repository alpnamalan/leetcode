### AUG 14, 2025 -- P3: LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS ###

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = best = 0
        for r, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[l])
                l += 1
            seen.add(ch)
            best = max(best, r-l+1)
        return best   
