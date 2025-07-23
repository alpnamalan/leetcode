### JULY 22, 2025 -- P1657: DETERMINE IF TWO STRINGS ARE CLOSE ###

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        c1, c2 = Counter(word1), Counter(word2)
        keys1, keys2, vals1, vals2 = list(c1.keys()), list(c2.keys()), list(c1.values()), list(c2.values())
        keys1.sort(), keys2.sort(), vals1.sort(), vals2.sort()
        return (vals1 == vals2) and (keys1 == keys2)
