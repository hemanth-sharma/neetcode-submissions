class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = []
        i, j, n = 0, 1, len(temperatures)
        while i < n:
            if j < n and temperatures[i] < temperatures[j]:
                results.append(j-i)
                i += 1
                j = i + 1
            elif j > n:
                results.append(0)
                i += 1
                j = i + 1
            else:
                j += 1
        
        return results
        