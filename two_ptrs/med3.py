### JULY 25, 2025 -- P151: REVERSE WORDS IN A STRING ###

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words = [w for w in words if w != '']
        newS = ""
        for i in range(len(words) - 1, -1, -1):
            newS += words[i]
            if i != 0:
                newS += " "
        return newS
