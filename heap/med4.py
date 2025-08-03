### AUG 4, 2025 -- P378: KTH SMALLEST ELEMENT IN A SORTED MATRIX ###

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # HEAP-MERGE APPROACH (BEATS 97% IN MEMORY)
        # n = len(matrix[0])
        # h = [(matrix[r][0], r, 0) for r in range(min(k, n))]
        # import heapq
        # heapq.heapify(h)
        # smallest = []
        # while h and len(smallest) < k:
        #     num, r, c = heapq.heappop(h)
        #     smallest.append(num)
        #     if c + 1 < n:
        #         heapq.heappush(h, (matrix[r][c+1], r, c+1))
        # return smallest[-1]

        # BINARY-SEARCH APPROACH (BEATS 100% IN RUNTIME)
        import bisect
        n = len(matrix[0])
        lo, hi = matrix[0][0], matrix[n-1][n-1]
        while lo < hi:
            mid = (lo + hi) // 2
            # count how many elements in the whole matrix are ≤ mid
            ct = 0
            for row in matrix:
                ct += bisect.bisect_right(row, mid) 
                # see where this 'mid' would place on a given row
                # meaning that there are that many nums smaller than 'mid'
            if ct >= k: # if 'mid' is higher than more numbers than we want
                hi = mid
            else:
                lo = mid + 1
        return lo
