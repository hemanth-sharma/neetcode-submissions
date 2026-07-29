class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += s + '.'
        
        return result

    def decode(self, s: str) -> List[str]:
        result = s.split('.')
        return result[:-1]
