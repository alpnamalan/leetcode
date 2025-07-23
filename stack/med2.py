### JULY 22, 2025 -- P394: DECODE STRING ###

class Solution:
    def decodeString(self, s: str) -> str:
        def helper(idx):
            res = ""
            k = 0
            while idx < len(s):
                ch = s[idx]
                if ch.isdigit():
                    # ints can be more than one digit
                    k = k * 10 + int(ch)
                elif ch == '[':
                    idx, new_s = helper(idx + 1)
                    res += k * new_s
                    k = 0
                elif ch == ']':
                    return idx, res
                else:
                    res += ch
                idx += 1
            return res

        final_s = helper(0)
        return final_s if isinstance(final_s, str) else final_s[1]
