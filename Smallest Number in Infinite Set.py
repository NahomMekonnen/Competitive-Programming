class SmallestInfiniteSet:

    def __init__(self):
        self.infinite_set = [i for i in range(1,1001)][::-1]
        self.cnt = Counter(self.infinite_set)

    def popSmallest(self) -> int:
        smallest = self.infinite_set.pop()
        self.cnt[smallest] -= 1
        return smallest

    def addBack(self, num: int) -> None:
        if not self.cnt[num] :
            self.infinite_set.append(num)
            self.infinite_set.sort(reverse = True)
            self.cnt[num] += 1
        

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
