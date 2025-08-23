### AUG 16, 2025 -- P1146: SNAPSHOT ARRAY ###

class SnapshotArray:
    """ BEATS 80%+ :: INTUITION: ONLY RECORD CHANGES 
        WHEN THEY ARE MADE; NO NEED FOR A WHOLE ARR """
    def __init__(self, length: int):
        # Keep a history for each index: arr[index] = [(snap_id, val), …]
        self.history = [[(0, 0)] for _ in range(length)]
        self.last = 0
        
    def set(self, index: int, val: int) -> None:
        if self.history[index][-1][0] == self.last:
            # overwrite if a change was made at the same snap_id
            self.history[index][-1] = (self.last, val)
        else:
            self.history[index].append((self.last, val))

    def snap(self) -> int:
        self.last += 1
        return self.last-1

    def get(self, index: int, snap_id: int) -> int:
        # Binary search to fetch the val
        arr = self.history[index]
        lo, hi = 0, len(arr) -1
        while lo <= hi:
            mid = (lo+hi) // 2
            if arr[mid][0] <= snap_id:
                lo = mid+1
            else:
                hi = mid-1
        return arr[hi][1]
