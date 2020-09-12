from main.entity.Inventory import Inventory


class InventoryService:

    def __init__(self):
        self.inventory = Inventory()

    def add_to_inventory(self, product):
        self.inventory.inventory_list.append(product)

    def remove_from_inventory(self, id):
        index = 0
        for product_in_inventory in self.inventory.inventory_list:
            if product_in_inventory.id == id:
                del self.inventory.inventory_list[index]
                break
            index += 1

    def update_product_in_inventory (self, product):
        index = 0
        for product_in_inventory in self.inventory.inventory_list:
            if product_in_inventory.id == product.id:
                self.inventory.inventory_list[index] = product
                break
            index += 1

    def print_product_from_inventory (self):
        print("Products in the inventory")
        for product_in_inventory in self.inventory.inventory_list:
            print(product_in_inventory)
            print("\n")
        print("End of the product list")
