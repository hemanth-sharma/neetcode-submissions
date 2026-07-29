class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for item in strs:
            char_counter = [0]*26
            for j in range(len(item)):
                char_counter[ord(item[j]) - ord('a')] += 1
            
            result[tuple(char_counter)].append(item)
        
        return list(result.values())        




