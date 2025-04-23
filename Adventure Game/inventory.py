# inventory.py
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        print(f"You have obtained: {item}")
        self.items.append(item)

    def show_inventory(self):
        print("\nYour Inventory:")
        for item in self.items:
            print(f"- {item}")