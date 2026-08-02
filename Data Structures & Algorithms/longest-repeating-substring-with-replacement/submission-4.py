class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        count_map = {}
        left = 0
        # shift right pointer and match the condition 
        # (right - left + 1) - max in count_map > k
        # length of window - count of most frequent char in that window
        maxf = 0 # for making it more optimal by removing the count hashmap
        for right in range(len(s)):
            count_map[s[right]] = 1 + count_map.get(s[right], 0)
            maxf = max(maxf, count_map[s[right]])
            while (right-left+1) - maxf > k: 
                count_map[s[left]] -= 1
                left += 1

            result = max(result, right-left+1)
        
        return result
