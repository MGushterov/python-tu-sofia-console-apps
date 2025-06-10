class Restaurant:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.menu = []

    def add_to_menu(self, dish, price):
        self.menu.append([dish, price])


    def get_order_data(self):
        number_of_table = input("Номер на маса: ")
        ordered_dishes = input("Поръчани ястия: ").split(", ")
        return number_of_table, ordered_dishes


    def calculate_order_value(self, order):
        total = 0.0
        prices = []
        for dish in order[1]:
            for item in self.menu:
                dish_name = item[0]
                if dish_name == dish:
                    total += item[1]
                    prices.append(item[1])
        return total, prices


    def generate_receipt(self):
        order_details = self.get_order_data()
        order_price = self.calculate_order_value(order_details)
        print(f"""
        **Регистрация/Касов бон**
        Ресторант: {self.name}
        Адрес: {self.address}
        Поръчка: {order_details[0]}
        """)
        for i in range(len(order_details[1])):
            print(f"* {order_details[1][i]} : {order_price[1][i]} лв.")

        print(f"Общо: {order_price[0]} лв.")
