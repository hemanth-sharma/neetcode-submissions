class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        window, countT = {}, {}
        for c in t: 
            countT[c] = countT.get(c, 0) + 1
            
        have, need = 0, len(countT)
        resIdx, resultLen = [-1, -1], float('infinity')
        l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need: 
                # update the result 
                if (r - l + 1) < resultLen:
                    resIdx = [l, r]
                    resultLen = (r - l + 1)
                # pop from left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = resIdx
        return s[l : r + 1] if resultLen != float("infinity") else ""
                