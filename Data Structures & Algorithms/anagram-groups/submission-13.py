class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # loop through strs
        # sort word
        # hashmap
        # if word not in hashmap add it
        # if it is add it to that
        # return list vals

        mp = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in mp:
                mp[sortedWord] = [word]
            elif sortedWord in mp:
                mp[sortedWord] += [word]
        return list(mp.values())


        