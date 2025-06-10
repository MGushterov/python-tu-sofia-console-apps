import unittest
import WareHouse as wh
class Tests(unittest.TestCase):

    #Testing WareHouse get_user_choice
    def test_return_choice(self):
        self.warehouse = wh.WareHouse()
        self.assertEqual(2, self.warehouse.get_user_choice())

    def test_return_none(self):
        self.warehouse = wh.WareHouse()
        self.assertEqual(None, self.warehouse.get_user_choice())

    # Testing WareHouse add_product
    def test_quantity_error(self):
        self.warehouse = wh.WareHouse()
        self.assertEqual("Please enter a quantity over 0: ", self.warehouse.add_product("tv", -4, 1000, "led display", "samsung"))
