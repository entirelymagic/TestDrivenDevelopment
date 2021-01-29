class Discount:
    def __init__(self, number_of_items, price):
        self.number_of_items = number_of_items
        self.price = price


class Checkout:
    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.checkout_basket = {}

    def addDiscount(self, item, number_of_items, price):
        discount = Discount(number_of_items, price)
        self.discounts[item] = discount

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")
        if item in self.checkout_basket:
            self.checkout_basket[item] += 1
        else:
            self.checkout_basket[item] = 1

    def calculateTotal(self):
        total = 0
        for item, quantity in self.checkout_basket.items():
            total += self.calculateItemTotal(item, quantity)
        return total

    def calculateItemTotal(self, item, quantity):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if quantity >= discount.number_of_items:
                total += self.calculateItemDiscountedTotal(item, quantity, discount)
            else:
                total += self.prices[item] * quantity
        else:
            total += self.prices[item] * quantity

        return total

    def calculateItemDiscountedTotal(self, item, quantity, discount):
        total = 0
        number_of_items = quantity / discount.number_of_items
        total += number_of_items * discount.price
        remaining = quantity % discount.number_of_items
        total += remaining * self.prices[item]
        return total
