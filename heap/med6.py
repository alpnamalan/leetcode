### AUG 4, 2025 -- P2336: SMALLEST NUMBER IN INFINITE SET ###

class SmallestInfiniteSet:
    import heapq
    # NAIVE APPROACH WHICH IS NOT IDEAL
    # def __init__(self):
    #     self.h = [i for i in range(1, 1001)]
    #     heapq.heapify(self.h)

    # def popSmallest(self) -> int:
    #     return heapq.heappop(self.h)
    
    # def addBack(self, num: int) -> None:
    #     if num in self.h: return
    #     else: heapq.heappush(self.h, num)

    # OPTIMIZED SOLUTION
    def __init__(self):
        self.next = 1 # ptr to next NEVER-USED-BEFORE int
        self.h = [] # this is for pop/addBack functionality
        self.in_heap = set()
    
    def popSmallest(self) -> int:
        if self.h:
            x = heapq.heappop(self.h)
            self.in_heap.remove(x)
            return x
        x = self.next
        self.next += 1
        return x

    def addBack(self, num: int) -> None:
        # only useful when num was popped previously
        if num < self.next and num not in self.in_heap:
            heapq.heappush(self.h, num)
            self.in_heap.add(num)
