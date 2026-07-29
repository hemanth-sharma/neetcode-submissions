class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            sorted_string = ''.join(sorted(string))
            result[sorted_string].append(string)
        
        return list(result.values())