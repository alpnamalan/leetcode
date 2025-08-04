### AUG 4, 2025 -- P649: DOTA2 SENATE ###

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        n = len(senate)
        # indices of R and D senators
        r = deque(i for i, ch in enumerate(senate) if ch == 'R')
        d = deque(i for i, ch in enumerate(senate) if ch == 'D')
        while r and d: # while both are present in senate
            ri, di = r.popleft(), d.popleft()
            if ri < di: # if one R is before another D
                r.append(ri + n) # R bans D makes it to next rnd
            else:
                d.append(di + n) # same thing but inversed
        return "Radiant" if r else "Dire"
