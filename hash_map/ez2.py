### AUG 3, 2025 -- P2085: COUNT COMMON WORDS WITH ONE OCCURRENCE ###

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        from collections import Counter
        c1, c2 = Counter(words1), Counter(words2)
        total = 0
        for key in list(c1.keys()):
            if c1[key] == 1 and key in c2:
                if c2[key] == 1:
                    total += 1
        return total
