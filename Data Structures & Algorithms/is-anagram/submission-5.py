class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counter = [0]*26
        for i in range(len(s)):
            char_counter[ord(s[i]) - ord('a')] += 1
            char_counter[ord(t[i]) - ord('a')] -= 1
            
        for val in char_counter:
            if val != 0:
                return False

        return True