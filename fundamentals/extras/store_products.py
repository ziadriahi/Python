from My_modules.Store import *
from My_modules.Product import *

Fashion=Store("Fashion_Store")
nike=Product(1,"Air Max",150,"Shoes")
ck=Product(2,"Calvin Klein",80,"Djeans")
adidas=Product(3,"Stan Smith",100,"Shoes")
Fashion.add_product(nike)
Fashion.add_product(ck)
Fashion.add_product(adidas)
print(Fashion.products[2].print_info())
print(Fashion.products[1].print_info())
print(Fashion.products[0].print_info())
ck.update_price(20,True)

Fashion.inflation(10)
Fashion.set_clearance("Shoes",10)
print(Fashion.products[0].print_info())
print(Fashion.products[1].print_info())
print(Fashion.products[2].print_info())
Fashion.sell_product(1)
print(Fashion.products[0].print_info())
print(Fashion.products[1].print_info())
