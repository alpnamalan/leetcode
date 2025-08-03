### AUG 2, 2025 -- P227: BASIC CALCULATOR II ###

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "") # Get rid of all spaces
        stack = [] 
        curr = "" # Track current number
        last_op = "" # Track last operation
        for i, ch in enumerate(s):
            # cont until you hit a new operator or end of string
            if ch in ['+','-','*','/'] or (i + 1) == len(s):
                # if last char it must be a digit so add it
                if (i+1) == len(s):
                    curr += ch
                # if no last op or it was + or -, defer its calc and push it to stack
                if last_op == '+' or not last_op:
                    stack.append(int(curr))
                elif last_op == '-':
                    stack.append(int(curr) * -1)
                # if * or / do the calculation immediately
                else:
                    # get the top of the stack (i.e., left-hand side of the operation)
                    left = stack.pop()
                    # right-hand side is our current num
                    right = int(curr) 
                    if last_op == '*': result = left * right
                    else: result = int(left / right)
                    stack.append(result)
                last_op = ch
                curr = ""
            else:
                curr += ch
        return sum(stack)
