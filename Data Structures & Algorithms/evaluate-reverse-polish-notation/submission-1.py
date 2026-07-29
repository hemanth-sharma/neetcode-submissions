class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+-*/":
                t1 = int(stack.pop())
                t2 = int(stack.pop())
                if i == '+':
                    val = t2 + t1
                    stack.append(val)
                elif i == '-':
                    val = t2 - t1
                    stack.append(val)
                elif i == '*':
                    val = t2 * t1
                    stack.append(val)
                else:
                    val = t2/t1
                    stack.append(int(val))
            else:
                stack.append(i)
        
        return int(stack[-1])