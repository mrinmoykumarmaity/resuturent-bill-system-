"""Order handling for the restaurant billing system."""

from typing import Dict


class Order:
    def __init__(self, menu):
        self.menu = menu
        self.items: Dict[str, int] = {}  # item name -> quantity

    def add_item(self, item: str, quantity: int = 1) -> None:
        if not self.menu.is_available(item):
            raise KeyError(f"Item '{item}' not on the menu")
        if quantity < 1:
            raise ValueError("Quantity must be positive")
        self.items[item] = self.items.get(item, 0) + quantity

    def remove_item(self, item: str) -> None:
        self.items.pop(item, None)

    def update_quantity(self, item: str, quantity: int) -> None:
        if item not in self.items:
            raise KeyError(f"Item '{item}' not in order")
        if quantity <= 0:
            self.remove_item(item)
        else:
            self.items[item] = quantity

    def subtotal(self) -> int:
        """Amount before any discount or tax."""
        return sum(self.menu.get_price(item) * qty for item, qty in self.items.items())

    def discount(self) -> int:
        """Simple discount: 10% off if subtotal exceeds 1000."""
        sub = self.subtotal()
        if sub > 1000:
            return int(sub * 0.10)
        return 0

    def total(self) -> int:
        """Total after subtracting discount."""
        return self.subtotal() - self.discount()

    def receipt(self) -> str:
        lines = ["\n--- RECEIPT ---"]
        for item, qty in self.items.items():
            price = self.menu.get_price(item)
            lines.append(f"{item:10} x{qty:<3} = {price * qty}")
        lines.append(f"SUBTOTAL: {self.subtotal()}")
        disc = self.discount()
        if disc:
            lines.append(f"DISCOUNT: -{disc}")
        lines.append(f"TOTAL: {self.total()}")
        return "\n".join(lines)

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def clear(self) -> None:
        self.items.clear()
