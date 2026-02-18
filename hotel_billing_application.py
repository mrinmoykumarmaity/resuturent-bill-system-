"""Command‑line interface for the restaurant billing system.  Uses
`restaurant.menu.Menu` and `restaurant.order.Order` to manage state.
"""

from restaurant.menu import Menu
from restaurant.order import Order


def run_cli():
    menu = Menu()
    order = Order(menu)

    print("\nWelcome to Pure Veg Restaurant!")
    print("Type 'help' to see available commands.\n")

    while True:
        menu.display()
        print("Commands: add, remove, view, finish, clear, help, quit")
        cmd = input("Enter command: ").strip().lower()

        if cmd in ("add", "a"):
            item = input("Item name: ").strip().lower()
            if not menu.is_available(item):
                print(f"'{item}' is not on the menu.")
                continue
            qty_str = input("Quantity (default 1): ").strip()
            qty = int(qty_str) if qty_str.isdigit() and int(qty_str) > 0 else 1
            try:
                order.add_item(item, qty)
                print(f"Added {qty} x {item} to your order.")
            except Exception as e:
                print("Error:", e)

        elif cmd in ("remove", "r"):
            item = input("Item to remove: ").strip().lower()
            order.remove_item(item)
            print(f"Removed {item} from order (if it was present).")

        elif cmd in ("view", "v"):
            if order.is_empty():
                print("Your order is currently empty.")
            else:
                print(order.receipt())

        elif cmd in ("finish", "f"):
            if order.is_empty():
                print("You have no items in your order.\n")
            else:
                print(order.receipt())
                print("Thank you for dining with us!")
                break

        elif cmd in ("clear", "c"):
            order.clear()
            print("Order cleared.")

        elif cmd in ("help", "h"):
            print(
                "add - add an item to your order\n"
                "remove - remove an item from your order\n"
                "view - show current order and total\n"
                "finish - finalize and print receipt\n"
                "clear - empty the order\n"
                "quit - exit without finishing\n"
            )

        elif cmd in ("quit", "q"):
            print("Goodbye!")
            break

        else:
            print("Unknown command; type 'help' for list of commands.\n")


if __name__ == "__main__":
    run_cli()

