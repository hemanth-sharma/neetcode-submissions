class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            counter = [0]*26
            for ch in string:
                counter[ord(ch) - ord('a')] += 1

            result[tuple(counter)].append(string)

        return list(result.values())        