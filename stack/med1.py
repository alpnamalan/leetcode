### JULY 22, 2025 -- P2390: REMOVING STARS FROM A STRING ###

class Solution:
    def removeStars(self, s: str) -> str:
        char_stack = []
        for ch in s:
            if ch == "*":
                char_stack.pop()
            else:
                char_stack.append(ch)
        res = ''
        for element in char_stack:
            res += element
        return res
