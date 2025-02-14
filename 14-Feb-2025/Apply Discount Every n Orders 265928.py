# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:
    customers = 0
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.items = dict(zip(products,prices))
        self.discount = discount
        self.give_discount = n

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customers += 1
        bill = 0
        for i in range(len(product)) :
            bill += (amount[i] * self.items[product[i]])
        if (self.customers % self.give_discount )== 0 :
            bill *= ((100 - self.discount)/100)
        return bill

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)