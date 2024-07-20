from typing import NamedTuple, Optional
from decimal import Decimal
from collections.abc import Sequence
from abc import ABC, abstractmethod


class Customer(NamedTuple):
    name: str
    fidelity: int

class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.price * self.quantity

class Order(NamedTuple):
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional['Promotion'] = None

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, Decimal(0))
    
    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self):
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'
    
class Promotion(ABC):
    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        pass

class FidelityPromo(Promotion):

    def discount(self, order: Order) -> Decimal:
        rate = Decimal(.05)
        if order.customer.fidelity >= 1000:
            return order.total() * rate
        return Decimal(0)
    
class BulkPromo(Promotion):
    def discount(self, order: Order) -> Decimal:
        discount = Decimal(0)
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * Decimal(.1)
        return discount
    
class LargeOrderPromo(Promotion):
    def discount(self, order: Order) -> Decimal:
        products = {item.product for item in order.cart}
        if len(products) >= 10:
            return order.total() * Decimal(.07)
        return Decimal(0)
    