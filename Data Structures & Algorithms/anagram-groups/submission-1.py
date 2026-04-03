class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)  #map charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 #a-z

            for c in s:
                count[ord(c) - ord("a")] += 1 # go char by char and increment count

            res[tuple(count)].append(s) # add charcount to result list with value of strs[s]
        return list(res.values())
