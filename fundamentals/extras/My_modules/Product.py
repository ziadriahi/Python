class Product:
    def __init__(self,id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category= category
    def print_info(self):
        print(f'The name of product is {self.name},its id is {self.id}, its category is {self.category} and its price is {self.price}$')
    
    def update_price(self, percent_change, is_increased) :
        if is_increased :
            self.price += (percent_change*self.price/100)
        else :
            self.price -= (percent_change*self.price/100)