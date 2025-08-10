#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.previous_transactions.append((title, price, quantity))

    def apply_discount(self):
        if self.discount:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There are no transactions to void.")
            return
        title, price, quantity = self.previous_transactions.pop()
        self.total -= price * quantity
        for _ in range(quantity):
            self.items.pop()


