from abc import abstractmethod

from django.shortcuts import render

class DiscountCalculator():
    @abstractmethod
    def get_discounted_price(self):
        pass


class DiscountCalculatorAmount(DiscountCalculator):
    def __init__(self, price, amount_discount):
        self.price = price
        self.amount_discount = amount_discount

    def get_discounted_price(self):
        return self.price * ((100 - self.amount_discount) / 100)



