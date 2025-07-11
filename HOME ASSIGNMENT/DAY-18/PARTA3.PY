# Problem 3: Create Product class with private price.
# Add method to apply discount.

class Product:
    def __init__(self, price):
        self.price = price

    def apply_discount(self, percent):
        if 0 <= percent <= 100:
            self.price -= (self.price * percent / 100)

    def get_price(self):
        return self.price

# Example usage:
p = Product(1000)      # Original price = 1000
p.apply_discount(10)   # Apply 10% discount
print(p.get_price())   # Output: 900.0
