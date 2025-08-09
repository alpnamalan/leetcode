### AUG 5, 2025 -- P621: TASK SCHEDULER ###

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter, deque
        import heapq
        # use a priority queue with the most frequent tasks
        freq = Counter(tasks)
        h = [(-ct, task) for task, ct in freq.items()] # negate for max-heap
        heapq.heapify(h)
        q = deque() # cooldown queue
        cpu = 0
        while h or q: # if there still are tasks to perform somewhere
            if h: # task to execute now
                ct, task = heapq.heappop(h)
                if ct+1 < 0: q.append((ct+1, task, cpu+n)) # stores with the time it'll be ready
            else: # idle time
                cpu = q[0][2] # wait until the first task to be ready
            if q and cpu >= q[0][2]:
                ct, task, _ = q.popleft()
                heapq.heappush(h, (ct, task))
            cpu += 1
        return cpu        
