class Product:
    def __init__(self, name, manufacturer, product_code, price, quantity, ordered=0):
        self.name = self.set_name(name)
        self.manufacturer = self.set_manufacturer(manufacturer)
        self.product_code = self.set_product_code(product_code)
        self.price = self.set_price(price)
        self.quantity = quantity
        self.ordered = ordered

    def get_name(self):
        return self.name

    def set_name(self, value):
        if not type(value) == str:
            raise ValueError("Name must be string!")

        return value

    def get_manufacturer(self):
        return self.manufacturer

    def set_manufacturer(self, value):
        if not type(value) == str:
            raise ValueError("Manufacturer must be string!")

        return value

    def get_product_code(self):
        return self.product_code

    def set_product_code(self, value):
        if not type(value) == int:
            raise ValueError("Product code must only contain numbers!")

        return value

    def get_price(self):
        return self.price

    def set_price(self, value):
        if value <= 0:
            raise Exception("Price must be over 0")

        return value

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, value):
        if value < 0:
            raise Exception("Price cannot be less than 0")

        return value

    def get_ordered(self):
        return self.ordered


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product_to_cart(self, product, amount=1):
        if amount > product.get_quantity():
            raise Exception("We currently don't have enough quantity of the product for your order!")

        product.ordered += amount
        self.items.append(product)

    def display_cart(self):
        shipment_cost = 0.0
        total = 0.0
        for product in self.items:
            price = product.get_price()
            ordered = product.get_ordered()
            total += price * ordered

        if total < 90:
            shipment_cost = 5.00
        elif total < 200:
            shipment_cost = 3.20
        else:
            shipment_cost = 1.00

        print(f'''
----------------
Total Price (no VAT included): {total:,.2f}
Total Price (with VAT): {total * 1.20:,.2f}
Price of shipment: {shipment_cost:,.2f}
----------------
        ''')


router = Product("Router Xiaomi Mi Router 4C", "Xiaomi", 2447089, 600.89, 10)
laptop = Product("Laptop HP Pavilion", "HP", 5501234, 1200.50, 5)
smartphone = Product("Smartphone Samsung Galaxy S21", "Samsung", 7890123, 899.99, 15)
headphones = Product("Wireless Headphones Sony WH-1000XM4", "Sony", 9876543, 299.95, 8)

shopping_cart = ShoppingCart()
shopping_cart.add_product_to_cart(router, 2)
shopping_cart.add_product_to_cart(laptop)
shopping_cart.add_product_to_cart(smartphone, 5)
shopping_cart.add_product_to_cart(headphones)

shopping_cart.display_cart()
