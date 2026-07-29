class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Recursion Method
        def dfs():
            token = tokens.pop()
            if token not in "+-/*":
                return int(token)
            
            right = dfs() # finds the rightmost int
            left = dfs() # 

            if token == '+': return left + right
            elif token == '-': return left - right
            elif token == '*': return left * right
            else: return int(left/right)
        
        value = dfs()
        return value

