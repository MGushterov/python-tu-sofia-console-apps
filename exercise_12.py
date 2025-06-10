class PhoneBook():
    def __init__(self):
        self.phonebook = {}

    def generate_phonebook(self, names, numbers):
        for i in range(len(names)):
            self.add_phone_number(names[i], numbers[i])
        self.print_phone_book()


    def add_phone_number(self, name, number):
        validated_number = self.validate_phone_number(number)
        validated_name = self.validate_name(name)
        if validated_number and validated_name:
            self.phonebook[name] = number
        else:
            print("Invalid phone number")


    def delete_phone_number(self, name):
        try:
            del self.phonebook[name]
        except:
            raise Exception(f"{name} does not exist in phonebook")


    def print_phone_book(self):
        for name, number in self.phonebook.items():
            print(f"Name: {name}, phone number: {number}")


    def validate_phone_number(self, number):
        if len(number) == 10:
            return True
        return False

    def validate_name(self, name):
        if len(name) >= 3:
            return True
        return False



phonebook = PhoneBook()
names = input("Enter names: ").split()
numbers = input("Enter phone numbers: ").split()
phonebook.generate_phonebook(names, numbers)
phonebook.add_phone_number(input("Enter name: "), input("Enter phone number: "))
phonebook.delete_phone_number(names[1])
phonebook.print_phone_book()