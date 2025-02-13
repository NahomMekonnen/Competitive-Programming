# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.array = defaultdict(int)  # array of numbers
        self.freq = defaultdict(int)  # array of frequencies 

    def add(self, number: int) -> None:
        self.freq[self.array[number]] -= (1 if self.freq[self.array[number]] > 0 else 0)
        self.array[number] += 1
        self.freq[self.array[number]] += 1

    def deleteOne(self, number: int) -> None:
        self.freq[self.array[number]] -= (1 if self.freq[self.array[number]] > 0 else 0)
        self.array[number] -= (1 if self.array[number] > 0 else 0)
        self.freq[self.array[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return bool(self.freq[frequency])


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)