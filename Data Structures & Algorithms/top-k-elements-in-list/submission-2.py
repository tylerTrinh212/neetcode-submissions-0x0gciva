class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Key: num value: count

        freq = [[] for i in range(len(nums) + 1)] # Buckets to group by frequency

        # Populate count with the value and how many times it appears
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        # Populate frequency buckets with index = count and num as its value
        for num, count in count.items():
            freq[count].append(num)

        result = []

        # Go from highest to lowest frequency until we have k nums
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
