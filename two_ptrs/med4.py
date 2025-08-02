### AUG 1, 2025 -- P167: TWO SUM II - INPUT ARRAY IS SORTED ###

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = set(numbers)
        for i, num in enumerate(numbers):
            need = target - num
            if need in s:
                j = numbers[i+1:].index(need) + (i+1)
                return [i+1, j+1]
        return []
