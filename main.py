from main.service.InventoryService import InventoryService
from main.service.ProductService import ProductService

product_service = ProductService()
inventory_service = InventoryService()


def create_stack_of_products():
    global new_product_five
    new_product_one = product_service.create_product()
    inventory_service.add_to_inventory(new_product_one)
    new_product_two = product_service.create_product()
    inventory_service.add_to_inventory(new_product_two)
    new_product_three = product_service.create_product()
    inventory_service.add_to_inventory(new_product_three)
    new_product_four = product_service.create_product()
    inventory_service.add_to_inventory(new_product_four)
    new_product_five = product_service.create_product()
    inventory_service.add_to_inventory(new_product_five)


if __name__ == "__main__":
    create_stack_of_products()

    inventory_service.print_product_from_inventory()

    new_product_five.name = "Neutron star"
    new_product_five.description = "What can be better then neutron star???"

    inventory_service.update_product_in_inventory(new_product_five)

    inventory_service.print_product_from_inventory()

    inventory_service.remove_from_inventory(new_product_five.id)

    inventory_service.print_product_from_inventory()
