### AUG 2, 2025 -- P179: LARGEST NUMBER ###

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # WORKING APPROACH BUT NOT AS EFFICIENT
        # strs = list(map(str, nums))
        # out = []
        # while strs:
        #     best = strs[0]
        #     for s in strs[1:]:
        #         if s + best > best + s:
        #             best = s
        #     out.append(best)
        #     strs.remove(best)
        # if out[0] == '0':
        #     return "0"
        # return ''.join(out)

        # BETTER EFFICIENCY AND ELEGANCE
        from functools import cmp_to_key
        strs = list(map(str, nums))
        def cmp(a: str, b: str):
            if a + b > b + a: return -1
            if b + a > a + b: return 1
            return 0
        strs.sort(key=cmp_to_key(cmp))
        out = ''.join(strs)
        return "0" if out[0] == '0' else out
