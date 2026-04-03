
class MedianFinder:

    def __init__(self):
        # 2 heaps
        # both heaps should be equal size

        self.small = [] # max heap
        self.large = [] # min heap
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1* num) # Push to max heap/small heap
        #every heap is auto min heap, so mult by -1 to do max heap

        # Make sure every num in small is <= evey num in large
        if (self.small and self.large and 
            (-1 * self.small[0]) > self.large[0]):
            value = -1 * heapq.heappop(self.small) # Move num from small to large heap
            heapq.heappush(self.large, value)

        # Uneven size check
        if len(self.small) > len(self.large) + 1: # If size difference of more than 1
            value = -1 * heapq.heappop(self.small) # Move num from small to large heap
            heapq.heappush(self.large, value)
        if len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large) # Move num from large to small heap
            heapq.heappush(self.small, -1 * value)

    def findMedian(self) -> float:
        # If one heap is larger than other, return its max/min value
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        # Else return the avg of the 2 middle vals
        return (-1 * self.small[0] + self.large[0]) / 2
        