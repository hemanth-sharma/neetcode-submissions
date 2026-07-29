class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stack strategy
        stack = []
        results = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stkTemp, stkIndex = stack.pop()
                results[stkIndex] = i - stkIndex
            stack.append((temp, i))

        return results