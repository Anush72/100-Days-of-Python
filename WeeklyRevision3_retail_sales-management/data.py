# storing the data
from product import Product

data_products = {
    "P001": Product("P001", "Laptop", 10, 700, 950),
    "P002": Product("P002", "Mouse", 30, 15, 25),
    "P003": Product("P003", "Keyboard", 20, 30, 50),
    "P004": Product("P004", "Monitor", 15, 150, 220),
    "P005": Product("P005", "Headphones", 25, 40, 65),
    "P006": Product("P006", "Webcam", 12, 35, 60),
    "P007": Product("P007", "USB Hub", 40, 10, 20),
    "P008": Product("P008", "External SSD", 18, 80, 120),
    "P009": Product("P009", "Microphone", 14, 45, 75),
    "P010": Product("P010", "Wireless Speaker", 22, 50, 85)
}

if 'P001' in data_products:
    print('Hello')