class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # key: count, value: nums

        frequency = [[] for i in range (len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get (i,0)

        for n,c in count.items():
            frequency[c].append(n)

        results = []

        # Going backwards in hashmap
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                results.append(n)
                if len(results) == k:
                    return results