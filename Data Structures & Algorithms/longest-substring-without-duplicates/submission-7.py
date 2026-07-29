class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Map to store the last seen index of each character
        char_map = {}
        left = 0         # 01  3
        max_length = 0   # 01 2345 
        # dvdf # pwwkeiw # pw wkeiw
        
        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
                
            char_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
            
        return max_length
