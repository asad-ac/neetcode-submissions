class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in x:
                x[key] = []
            x[key].append(word)
        return list(x.values())