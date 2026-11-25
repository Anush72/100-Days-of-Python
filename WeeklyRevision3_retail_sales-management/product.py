# product class



class Product:
    def __init__(self,product_id,name,quantity,cost_price,sale_price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.cost_price = cost_price
        self.sale_price = sale_price

    # method to display product
    def display_product(self):
        print(f"Product ID: {self.product_id}\nProduct Name: {self.name}\nAvailable stock: {self.quantity}"
              f"\nCost Price: ${self.cost_price:.2f}\nSelling Price: ${self.sale_price:.2f}")

    # method to restock thw product
    def restock_product(self,restock):
        if restock > 0:
            self.quantity += restock
        else:
            print('The restock should be positive not negative')

    # method to reduce stock
    def reduce_stock(self,sale_quantity):
        stock = False
        if sale_quantity > 0:
            if self.quantity >= sale_quantity:
                self.quantity -= sale_quantity
                stock = True
            else:
                print(f"You have {self.quantity} quantity")
        else:
            print('The quantity should be positive not negative')
        return stock

