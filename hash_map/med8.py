### AUG 3, 2025 -- P874: WALKING ROBOT SIMULATION ###

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos, maxdist = (0, 0), 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        di = 0
        dr = dirs[di]
        obst = set(tuple(o) for o in obstacles)
        for cm in commands:
            if cm == -1:
                di = (di + 1) % 4
                dr = dirs[di]
            elif cm == -2:
                di = (di - 1) % 4
                dr = dirs[di]
            # move forward
            else:
                while cm > 0:
                    new = (pos[0] + dr[0], pos[1] + dr[1])
                    if new in obst:
                        break
                    else:
                        pos = new
                        maxdist = max(maxdist, new[0]*new[0] + new[1]*new[1])
                    cm -= 1
        return maxdist
