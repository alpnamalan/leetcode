### AUG 3, 2025 -- P973: K CLOSEST POINTS TO ORIGIN ###

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # FINAL APPROACH: QUICK AND EFFICIENT
        # BEATS 99.2% IN RUNTIME, 94.5% IN MEMORY
        points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
        return points[:k]

        # APPROACH #1: INCORRECT, DOES NOT ACCOUNT FOR DUPLICATES
        # def calcDist(pt: List[int]) -> float:
        #      return sqrt(pt[0]**2 + pt[1]**2)
        # dist_map = {tuple(p): calcDist(p) for p in points}
        # print(dist_map)
        # closest = [list(p[0]) for p in sorted(dist_map.items(), key=lambda x:x[1])]
        # print(closest)
        # return closest[:k]

        # APPROACH #2: WORKS BUT A BIT SLOW COMPARED TO OTHER SOLUTIONS
        # from functools import cmp_to_key
        # def cmp(p1: List[int], p2: List[int]) -> int:
        #     if (p1[0]**2 + p1[1]**2) > (p2[0]**2 + p2[1]**2): return 1
        #     elif (p1[0]**2 + p1[1]**2) < (p2[0]**2 + p2[1]**2): return -1
        #     else: return 0
        # points.sort(key=cmp_to_key(cmp))
        # return points[:k]
