from Restaurant import Restaurant

restaurant = Restaurant(name=input("Име на ресторанта: "), address=input("Адрес: "))


def generate_restaurant_and_menu():
    flag = False
    while not flag:
        try:
            dish_name = input("Име на ястие: ")
            dish_price = float(input("Цена на ястие: "))
        except ValueError as val_er:
            print(val_er, "Въведете число за цената на ястието!")
        else:
            restaurant.add_to_menu(dish_name, dish_price)
            choice = input("Искате ли да въведете още ястия? (Y/N): ")
            if choice == "N":
                flag = True


def end_program():
    restaurant.generate_receipt()