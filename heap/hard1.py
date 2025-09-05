### AUG 10, 2025 -- P295: FIND MEDIAN FROM DATA STREAM ###

class MedianFinder:
    import heapq
    """TWO HEAP APPROACH"""
    def __init__(self):
        self.lhp = [] # max heap for <= med
        self.rhp = [] # min heap for >= med
        
    def addNum(self, num: int) -> None:
        # convention: when odd, keep the extra in left heap
        # first push to left
        heapq.heappush(self.lhp, -num)
        # ensure left[0] ≤ right[0]
        if self.rhp and -self.lhp[0] > self.rhp[0]:
            heapq.heappush(self.rhp, -heapq.heappop(self.lhp))
        # balance sizes; len(lhp) can be len(rhp)+1
        if len(self.lhp) > len(self.rhp)+1:
            heapq.heappush(self.rhp, -heapq.heappop(self.lhp))
        elif len(self.rhp) > len(self.lhp): # right CAN'T be larger
            heapq.heappush(self.lhp, -heapq.heappop(self.rhp))

    def findMedian(self) -> float:
        if len(self.lhp) == len(self.rhp):
            return (self.rhp[0]-self.lhp[0]) / 2.0
        else: return float(-self.lhp[0]) # median in the left heap
