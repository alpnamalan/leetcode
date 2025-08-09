### AUG 5, 2025 -- P239: SLIDING WINDOW MAXIMUM ###

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # find a way to avoid taking the max every time
        from collections import deque
        q = deque() # contains the indices of the candidates for the max value
                    # in decreasing order, so q[0] is the absolute max
        out = [] # len is the num of all sliding windows
        for i in range(len(nums)):
            if q and q[0] == i-k: # i.e., we're kicking out the curr max
                q.popleft()
            # if new num is greater than some candidates kick those out
            # and insert new cand into appropriate place
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k-1:
                out.append(nums[q[0]]) 
        return out
