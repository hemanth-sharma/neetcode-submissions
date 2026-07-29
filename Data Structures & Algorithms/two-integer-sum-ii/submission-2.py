class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers = [1, 2, 3, 4, 5, 7, 8, 9]
        # target = 15
        i, j = 0, len(numbers)-1
        while i < j:
            temp = numbers[i] + numbers[j]
            if temp == target:
                return [i+1, j+1]
            if temp < target:
                i += 1
            elif temp > target: 
                j -= 1
        
        return [-1, -1]


