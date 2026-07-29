class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_char = [0]*26
        for i in range(len(s)):
            counter_char[ord(s[i])-ord('a')] += 1
            counter_char[ord(t[i])-ord('a')] -= 1
        
        # return all(val == 0 for val in counter_char)
        # return not any(val != 0 for val in counter_char)
        return set(counter_char) == {0}


        