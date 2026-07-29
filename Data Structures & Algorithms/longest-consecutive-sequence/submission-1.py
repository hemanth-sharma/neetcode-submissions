class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0
        maxcounter = 0
        # print(nums)
        # [0, 1, 1, 2, 3, 4, 5, 6]
        if len(nums) < 1:
            return maxcounter
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i]-1 == nums[i-1]:
                counter += 1
                # print(counter)
            elif nums[i]-1 != nums[i-1]:
                maxcounter = max(maxcounter, counter+1)
                counter = 0

        maxcounter = max(maxcounter, counter+1)
        return maxcounter        