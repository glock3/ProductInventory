from main.entity import Product
import random


class ProductService:

    incremented_index = 0

    def __init__(self):
        self.predefined_product_names = ["Sport car", "Whiskey", "Hammer", "Screwdriver", "UAV"]
        self.predefined_product_descriptions = ["You can move fast", "It can make you happy",
                                                "It's really man's thing", "What can be better then this?",
                                                "Cool thing!"]

    def create_product(self):
        product_id = self.incremented_index
        self.incremented_index += 1
        product_name = self.predefined_product_names[random.randint(0, 4)]
        product_description = self.predefined_product_descriptions[random.randint(0, 4)]
        product = Product(product_id, product_name, product_description)
        return product
