class Solution:
    def isPalindrome(self, s: str) -> bool:
        isAlphabet = lambda c: (ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))

        i, j = 0, len(s)-1

        while i < j:
            while not isAlphabet(s[i].lower()) and i < j:
                i += 1
            while not isAlphabet(s[j].lower()) and i < j:
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
        
        return True
