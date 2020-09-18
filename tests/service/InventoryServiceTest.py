import unittest

from main.entity.Product import Product
from main.service.InventoryService import InventoryService


class InventoryServiceTest(unittest.TestCase):

    def setUp(self):
        self.inventory_service = InventoryService()

    def test_when_product_added_to_inventory_should_appear_in_inventory(self):
        expected_product = Product(1, "Name 1", "Description 1")

        self.inventory_service.add_to_inventory(expected_product)

        actual_product = self.inventory_service.inventory.inventory_list[0]
        self.assertEqual(expected_product, actual_product)

    def test_when_two_products_added_to_inventory_should_not_remove_old_from_inventory(self):
        expected_product_one = Product(1, "Name 1", "Description 1")
        expected_product_two = Product(2, "Name 2", "Description 2")

        self.inventory_service.add_to_inventory(expected_product_one)
        self.inventory_service.add_to_inventory(expected_product_two)

        actual_product_one = self.inventory_service.inventory.inventory_list[0]
        self.assertEqual(expected_product_one, actual_product_one)
        actual_product_two = self.inventory_service.inventory.inventory_list[1]
        self.assertEqual(expected_product_two, actual_product_two)

    def test_when_null_added_to_inventory_should_error_appear(self):
        expected_product = None

        with self.assertRaises(Exception) as context:
            self.inventory_service.add_to_inventory(expected_product)

        self.assertEqual('None passed to inventory', str(context.exception))