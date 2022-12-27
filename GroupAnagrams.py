class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for n in strs:
            x = ''.join(sorted(n))
            if x in result:
                result[x].append(n)
            else:
                result[x] = [n]
        return result.values()