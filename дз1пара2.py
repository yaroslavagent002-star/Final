class Product:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        if product.available:
            self.items.append((product, quantity))
            print(f"{product.name} додано у кошик ({quantity} шт.)")
        else:
            print(f"{product.name} недоступний")

    def remove_product(self, product_name):
        self.items = [item for item in self.items if item[0].name != product_name]
        print(f"{product_name} видалено з кошика")

    def total_price(self):
        total = sum(item[0].price * item[1] for item in self.items)
        return total

    def show_cart(self):
        if not self.items:
            print("Кошик порожній")
        else:
            print("Ваш кошик:")
            for product, quantity in self.items:
                print(f"{product.name} - {quantity} шт. - {product.price * quantity} грн")
            print("Загальна вартість:", self.total_price(), "грн")

p1 = Product("Чайник", 500)
p2 = Product("Кава", 150)
cart = Cart()
cart.add_product(p1)
cart.add_product(p2, 2)
cart.show_cart()
cart.remove_product("Кава")
cart.show_cart()
