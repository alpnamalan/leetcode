### AUG 2, 2025 -- P134: GAS STATION ###

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        # O(n^2) -- not ideal
        # i = 0
        # while i < len(gas):
        #     tank = gas[i] - cost[i]
        #     j = (i + 1) % len(gas)
        #     while tank >= 0:
        #         if i == j:
        #             return i
        #         tank += gas[j]
        #         tank -= cost[j]
        #         j += 1
        #         j = j % len(gas)
        #     i += 1

        # OPTIMIZED
        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i+1 # skip all the way past this pt
                tank = 0
        return start
