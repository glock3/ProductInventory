import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from main.entity.Product import Product
from main.service.InventoryService import InventoryService
from main.service.ProductService import ProductService

from main import read_input


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

    # function
    # class object
    # class


    # mock on  function
    def test_when_create_and_add_new_product_product_service_is_triggered(self):
        product_service_mock = ProductService()
        product_service_mock.create_product = MagicMock()
        self.inventory_service.productService = product_service_mock

        self.inventory_service.create_and_add_new_product()

        product_service_mock.create_product.assert_called_once()

    # mock on  function
    def test_when_create_and_add_new_product_product_service_return_product(self):
        mocked_return_product = Product(1, 'N', 'D')
        product_service_mock = ProductService()
        product_service_mock.create_product = MagicMock()
        product_service_mock.create_product.return_value = mocked_return_product

        self.inventory_service.productService = product_service_mock

        self.inventory_service.create_and_add_new_product()

        actual_product_one = self.inventory_service.inventory.inventory_list[0]
        self.assertEqual(mocked_return_product, actual_product_one)

    def test_when_create_and_add_new_product_product_service_is_triggered_and_product_saved(self):
        product_to_return_by_mock = Product(1, 'name', 'description')
        self.inventory_service.productService.create_product = MagicMock()
        self.inventory_service.productService.create_product.return_value = product_to_return_by_mock
        self.inventory_service.add_to_inventory = MagicMock()

        self.inventory_service.create_and_add_new_product()

        self.inventory_service.add_to_inventory.assert_called()
        self.inventory_service.add_to_inventory.assert_called_once_with(product_to_return_by_mock)


    # function patching
    def test_when_create_and_add_new_product_product_service_is_triggered_with_patch(self):
        product_to_return_by_mock = Product(1, 'name', 'description')
        with patch('main.service.InventoryService.ProductService.create_product') as mock_product_service:
            mock_product_service.return_value = product_to_return_by_mock

            self.inventory_service.create_and_add_new_product()

            mock_product_service.assert_called_once()

    #function patching
    def test_when_create_and_add_new_product_product_service_is_triggered_with_patch_and_product_added_to_inventory(self):
        product_to_return_by_mock = Product(1, 'name', 'description')
        with patch('main.service.InventoryService.ProductService.create_product') as mock_product_service:
            mock_product_service.return_value = product_to_return_by_mock

            self.inventory_service.create_and_add_new_product()

            mock_product_service.assert_called_once()

            actual_product_one = self.inventory_service.inventory.inventory_list[0]
            self.assertEqual(product_to_return_by_mock, actual_product_one)

    def test_when_create_and_add_new_product_product_service_is_triggered_with_patch_on_class(self):
        product_to_return_by_mock = Product(1, 'name', 'description')
        with patch('main.service.ProductService') as mock_product_service_class:
            mocked_instance = mock_product_service_class.return_value
            mocked_instance.create_product.return_value = product_to_return_by_mock
            #mock_product_service_class.side_effect

            self.inventory_service.productService = mocked_instance
            self.inventory_service.create_and_add_new_product()

            mocked_instance.create_product.assert_called_once()
            actual_product_one = self.inventory_service.inventory.inventory_list[0]
            self.assertEqual(product_to_return_by_mock, actual_product_one)

    def side_effect_custom(self):
        return [1, 2, 3, 4, 5]

    def my_side_effect(*args, **kwargs):
        if args[1] == 1:
            return Product(1, "Name 1", "Description 1")
        elif args[1] == 2:
            return Product(2, "Name 2", "Description 2")
        elif args[1] == 3:
            return Product(3, "Name 3", "Description 3")

    def test_side_effects(self):
        self.inventory_service.productService.create_product_custom_for_test = MagicMock()
        self.inventory_service.productService.create_product_custom_for_test.side_effect = self.my_side_effect

        self.inventory_service.create_and_add_new_product_by_prepared_product_id(1)

        actual_product = self.inventory_service.inventory.inventory_list[0]
        self.assertEqual(Product(1, "Name 1", "Description 1"), actual_product)

        self.inventory_service.create_and_add_new_product_by_prepared_product_id(3)

        actual_product = self.inventory_service.inventory.inventory_list[1]
        self.assertEqual(Product(3, "Name 3", "Description 3"), actual_product)

        self.inventory_service.create_and_add_new_product_by_prepared_product_id(2)

        actual_product = self.inventory_service.inventory.inventory_list[2]
        self.assertEqual(Product(2, "Name 2", "Description 2"), actual_product)


    def test_side_effects_with_exception(self):
        self.inventory_service.productService.create_product_custom_for_test = MagicMock()
        self.inventory_service.productService.create_product_custom_for_test.side_effect = ValueError('Custom text')

        with self.assertRaises(ValueError) as context:
            self.inventory_service.create_and_add_new_product_by_prepared_product_id(1)
        self.assertEqual('Custom text', str(context.exception))

    ##############################

    @patch('main.service.InventoryService.ProductService')
    def test_when_create_and_add_new_product_product_service_is_triggered_with_decorator(self, product_service_mock):
        self.inventory_service.productService = product_service_mock

        self.inventory_service.create_and_add_new_product()

        product_service_mock.create_product.assert_called_once()

    @patch.object(ProductService, 'create_product')
    def test_when_create_and_add_new_product_product_service_is_triggered_with_decorator_for_object(self, product_service_mock):
        self.inventory_service.productService = product_service_mock

        self.inventory_service.create_and_add_new_product()

        product_service_mock.create_product.assert_called_once()

    def my_side_effect_for_decorator(*args, **kwargs):
        if args[0] == 1:
            return Product(1, "Name 1", "Description 1")
        elif args[0] == 2:
            return Product(2, "Name 2", "Description 2")
        elif args[0] == 3:
            return Product(3, "Name 3", "Description 3")

    @patch.object(ProductService, 'create_product_custom_for_test', side_effect=my_side_effect_for_decorator)
    def test_when_create_and_add_new_product_product_service_is_triggered_with_decorator_and_side_effect(self, product_service_mock):
        self.inventory_service.create_and_add_new_product_by_prepared_product_id(1)

        actual_product = self.inventory_service.inventory.inventory_list[0]
        self.assertEqual(Product(1, "Name 1", "Description 1"), actual_product)

    #
    # def test_for_object(self):
    #     product_service_mock = ProductService()
    #     product_service_mock.create_product = MagicMock()
    #
    #     self.inventory_service.create_and_add_new_product(product_service_mock)
    #
    #     product_service_mock.create_product.assert_called_once()
