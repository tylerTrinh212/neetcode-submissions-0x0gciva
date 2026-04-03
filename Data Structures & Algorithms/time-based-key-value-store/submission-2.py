class TimeMap:

    def __init__(self):
        self.dictionary = {} # key: list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = []
        self.dictionary[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Use binary search to find most recent timestamp that is less than or equal to given timestamp
        answer = ""
        values = self.dictionary.get(key,[]) # Get a list of all pairs related to key we are searching
        left = 0
        right = len(values) -1

        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] <= timestamp: # If we are less than timestamp, continue to the right
                answer = values[mid][0] # Latest answer so far
                left = mid + 1
            else: 
                right = mid - 1

        return answer
