from typing import NamedTuple, Optional, Callable
from collections.abc import Sequence
from decimal import Decimal

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
    card: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], Decimal]] = None

    def total(self) -> Decimal:
        totals = (item.total() for item in self.card)
        return sum(totals, Decimal(0))
    
    def due(self):
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(self)
        return self.total() - discount
    
    def __repr__(self):
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'
    
def fidelity_promo(order: Order) -> Decimal:
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal(.05)
    else :
        return Decimal(0)
    
def bulk_promo(order: Order) -> Decimal:
    discount = Decimal(0)
    for item in order.card:
        if item.quantity >= 20:
            discount += item.total * Decimal(.1)
    return discount

def large_order_promo(order: Order) -> Decimal:
    products = {item.product for item in order.card}
    if len(products) >= 10:
        return order.total() * Decimal(.07)
    return Decimal(0)

