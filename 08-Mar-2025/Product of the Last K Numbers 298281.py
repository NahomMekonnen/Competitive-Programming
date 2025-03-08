# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.prods = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prods = [1]
        else:
            self.prods.append(num * self.prods[-1])

    def getProduct(self, k: int) -> int:
        k += 1
        if len(self.prods) < k:
            return 0
        return self.prods[-1] // self.prods[-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)