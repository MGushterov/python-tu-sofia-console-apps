from WareHouse import WareHouse

warehouse = WareHouse()
while True:
    print("Choose how you would like to use the warehouse")
    print("1. Add product")
    print("2. Delete product/quantity")
    print("3. Redact product")
    print("4. Print all products")
    print("5. Exit")

    choice = warehouse.get_user_choice()
    if choice < 4:
        product_info = input("Enter product information: ").split()
        name, quantity = product_info[0], int(product_info[1])

    if choice == 1:
        warehouse.add_product(name, quantity, *product_info[2:])
    elif choice == 2:
        warehouse.delete_product(name)
    elif choice == 3:
        warehouse.edit_product(name, quantity)
    elif choice == 4:
        warehouse.print_products()
    elif choice == 5:
        warehouse.print_products()
        break
    else:
        print("Invalid input. Try again")
