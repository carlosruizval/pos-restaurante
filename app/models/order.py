from dataclasses import dataclass, field
from typing import Optional

@dataclass
class OrderItem:
    product_id: str
    product_name: str
    unit_price: float
    quantity: int = 1

    @property
    def subtotal(self) -> float:
        return self.unit_price * self.quantity

@dataclass
class OrderDraft:
    table_id: str
    items: list[OrderItem] = field(default_factory=list)
    notes: str = ""

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self.items)

    def add_item(self, product_id: str, name: str, price: float):
        for item in self.items:
            if item.product_id == product_id:
                item.quantity += 1
                return
        self.items.append(OrderItem(product_id, name, price))

    def remove_item(self, product_id: str):
        self.items = [i for i in self.items if i.product_id != product_id]