"""Menu management for the restaurant.
"""

class Menu:
    def __init__(self):
        # predefined items, but could be loaded from a database/file later
        self.items = {
            'pizza': 250,
            'coffee': 150,
            'salad': 100,
            'pasta': 120,
            'burger': 180,
            'fries': 80,
            'soup': 90,
            'icecream': 70,
            'tea': 50,
            'juice': 60,
            'rice bowl': 110,
            'sandwich': 130,
            'noodles': 140,
            'steak': 300,
            'paneer': 200,
            'fried rice': 160,
            'dosa': 90,
            'idli': 50,
            'vada': 60,
            
        }

    def display(self):
        print("\n-- MENU --")
        for name, price in self.items.items():
            print(f"{name:10} : {price}")
        print()

    def is_available(self, item: str) -> bool:
        return item in self.items

    def get_price(self, item: str) -> int:
        return self.items.get(item, 0)

    def add_item(self, item: str, price: int):
        self.items[item] = price

    def remove_item(self, item: str):
        self.items.pop(item, None)
