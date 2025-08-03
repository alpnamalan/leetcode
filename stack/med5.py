### AUG 2, 2025 -- P1249: MINIMUM REMOVE TO MAKE VALID PARENTHESES ###

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Two-pass approach where left -> right drops extra ')'
        # and right -> left drops extra '('
        res, opn = [], 0
        # First pass l -> r
        for ch in s:
            if ch == '(':
                opn += 1
                res.append(ch)
            elif ch == ')':
                if opn == 0:
                    continue
                else:
                    opn -= 1
                    res.append(ch)
            else:
                res.append(ch)
        # Second pass r -> l
        final = []
        for ch in reversed(res):
            if ch == '(' and opn > 0:
                opn -= 1
                continue
            final.append(ch)
        return ''.join(reversed(final))
