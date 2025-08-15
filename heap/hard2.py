### AUG 15, 2025 -- P630: COURSE SCHEDULE III ###

class Solution:
    import heapq
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """ SORTING + GREEDY + HEAP :: BEATS 86%"""
        # courses = [[d, l] for d, l in courses if d <= l]
        courses.sort(key=lambda x:x[1])
        time = 0 # Total time of all courses taken till now
        h = [] # GREEDY :: Max heap for longest courses
        for d, l in courses:      
            time += d
            heapq.heappush(h, -d)
            if time > l: 
                biggest = -heapq.heappop(h)
                time -= biggest
            # IF instead of WHILE because...
            # sorted by deadline and always drop the single longest course
            # remove that one; guaranteed to be under the curr deadline again
            # never need to drop more than one at a time !!
        return len(h)
