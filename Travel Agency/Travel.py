class Travel:
    def __init__(self, id, destination, price, status):
        self.id = self.set_id(id)
        self.destination = destination
        self.price = price
        self.status = self.set_status(status)

    def get_id(self):
        return self.id

    def set_id(self, value):
        if len(value) != 4:
            print("Invalid input. Id must be exactly 4 digits long")

        return value

    def get_destination(self):
        return self.destination

    def get_price(self):
        return self.price

    def get_status(self):
        return self.status

    def set_status(self, value):
        if value != "Taking off" or value != "Has taken off":
            print("Invalid status")

        return value

