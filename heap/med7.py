### AUG 4, 2025 -- P2462: TOTAL COST TO HIRE K WORKERS ###

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        import heapq
        n = len(costs)
        h = []
        left, right = 0, n-1
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(h, (costs[left], left, "l"))
                left += 1
            # same check again because it could change after adding one to left
            if left <= right:
                heapq.heappush(h, (costs[right], right, "r"))
                right -= 1    
        total = 0
        while k > 0:
            cost, idx, side = heapq.heappop(h)
            total += cost
            k -= 1
            # you can still add to the heap from initial list
            if left <= right:
                if side == 'l': pos = left; left += 1
                else: pos = right; right -= 1
                heapq.heappush(h, (costs[pos], pos, side))
        return total
