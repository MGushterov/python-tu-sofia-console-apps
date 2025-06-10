class WareHouse():
    def __init__(self):
        self.ware_house = dict()


    def get_user_choice(self):
        try:
            choice = int(input("Enter 1, 2, 3, 4 or 5: \n"))
        except:
            return None
        else:
            return choice


    def add_product(self, name, quantity, price, category, brand):
        if quantity < 0:
            new_quantity = int(input("Please enter a quantity over 0: "))
            self.add_product(name, new_quantity, price, category, brand)

        if name in self.ware_house.keys():
            self.edit_product(name, quantity)
        else:
            print("Item added to warehouse")
            self.ware_house[name] = {
                "quantity": quantity,
                "price": price,
                "category": category,
                "brand": brand
            }

    def edit_product(self, name, quantity):
        client_choice = input("Choose if you want to CHANGE quality or DELETE quality/reenter product: ").upper()
        if client_choice == "CHANGE":
            print("Item updated")
            self.ware_house[name]["quantity"] = quantity
        elif client_choice == "DELETE":
            self.delete_product(name, quantity)
        else:
            print("Wrong input. Try again by typing in CHANGE/DELETE")
            self.edit_product(name, quantity)



    def delete_product(self, name, quantity=0):
        client_choice = input("Choose if you want to delete part of QUANTITY or the ENTIRE product: ").upper()
        if self.ware_house[name]["quantity"] < quantity or client_choice == "ENTIRE":
            del self.ware_house[name]
        elif client_choice == "QUANTITY":
            self.ware_house[name]["quantity"] -= quantity
        else:
            print("Wrong input. Try again by typing in QUANTITY/ENTIRE")
            self.delete_product(name, quantity)


    def print_products(self):
        print("---------------------------------------------------------------------------------------")
        for name in self.ware_house.keys():
            print(f"Product: {name}")
            for key, val in self.ware_house[name].items():
                print(f"{key}: {val}")

            print('\n')
        print("---------------------------------------------------------------------------------------")



