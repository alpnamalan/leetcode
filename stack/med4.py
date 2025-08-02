### AUG 1, 2025 -- P735: ASTEROID COLLISION ###

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ### BETTER SOLUTION (A LOT MORE ELEGANT & EFFICIENT) ###
        stack = []
        for a in asteroids:
            alive = True
            # The only cases where a collision can happen
            while alive and a < 0 and stack and stack[-1] > 0:
                top = stack[-1]
                if top < -a: # abs(a) is larger, so continue
                    stack.pop()
                    continue
                if top == -a: # both explode
                    stack.pop()
                alive = False # a dies if it's equal or smaller than top
            if alive: # if the new ast stays alive it gets added
                stack.append(a)
        return stack
        ### INITIAL SOLUTION WITH RECURSION ###
        # def collide(stack, new):
        #     if len(stack) == 0:
        #         stack.append(new)
        #         return stack
        #     # last one moves left, or it moves right but so is the new one
        #     elif (stack[-1] < 0) or (stack[-1] > 0 and new > 0):
        #         stack.append(new)
        #         return stack
        #     # collision happens when last one moves right but new one moves left
        #     else:
        #         # equal, both destroyed
        #         if abs(new) == abs(stack[-1]):
        #             stack.pop()
        #             return stack
        #         # new ast smaller so it gets destroyed immediately
        #         elif abs(new) < abs(stack[-1]):
        #             return stack
        #         # new ast larger so it proceeds recursively
        #         else:
        #             stack.pop()
        #             return collide(stack, new)
        # asts = []
        # for ast in asteroids:
        #     collide(asts, ast)
        # return asts
