# importing libraries
from product import Product
from data import data_products
from prettytable import PrettyTable

# Class Inventory

class Inventory:
    def __init__(self,products):
        self.products = products

    # method to display all products
    def get_product_details(self):
        table = PrettyTable()
        table.field_names = ["Product ID","Product Name","Quantity","$ Cost Price", "$ Sale Price"]
        for value in self.products.values():
            table.add_row([value.product_id,value.name,value.quantity,value.cost_price,value.sale_price])
        print(table)

    # Looking for Product
    def search_product(self,product_id):
        if product_id in self.products:
            return self.products[product_id]
        else:
            return None
