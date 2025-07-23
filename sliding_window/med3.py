### JULY 22, 2025 -- P1456: MAXIMUM NUMBER OF VOWELS IN A SUBSTRING OF GIVEN LENGTH ###

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        num = 0
        for i in range(k):
            if s[i] in vowels:
                num += 1
        ans = num

        for r in range(k, len(s)):
            l = r - k
            if s[r] in vowels:
                num += 1
            if s[l] in vowels:
                num -= 1
            ans = max(ans, num)

        return ans
