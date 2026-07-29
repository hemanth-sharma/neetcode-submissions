class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Backward Strategy :)
        n = len(temperatures)
        results = [0] * n
        # [30,38,30,36,35,40,28]
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[i] >= temperatures[j]:
                if results[j] == 0:
                    break
                j += results[j]
            if j < n and temperatures[i] < temperatures[j]:
                results[i] = j - i
                
        return results

        