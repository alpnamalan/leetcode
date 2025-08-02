### AUG 1, 2025 -- P49: GROUP ANAGRAMS ###

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # from collections import defaultdict, Counter
        # groups = defaultdict(list) # EACH ITEM IS INIT AN EMPTY LIST
        # for s in strs:
        #     # KEY: SORTED COUNTS OF EACH LETTER (SO ORDER DOES NOT MATTER)
        #     key = tuple(sorted(Counter(s).items()))
        #     # IF IT HAS THE SAME COUNTS (I.E., ANAGRAM) ADD IT TO CURR GROUP
        #     groups[key].append(s)
        # return list(groups.values())

        # BETTER APPROACH FOR RUNTIME 
        from collections import defaultdict
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - 97] += 1 # ASCII val to index 'a' -> 0 and 'z' -> 25
            key = tuple(count) # key with len 26
            groups[key].append(s)
        return list(groups.values())
