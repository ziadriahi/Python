class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self,first_name, last_name, pet, treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food    	
    
# implement the following methods:

# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self, obj):
       self.pet.play() 
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        if len(self.pet_food)>0 :
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food} !")
            self.pet.eat()
        else :
            print("Oh !! No !! You need more pet food !")
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()

class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self, name, type,tricks,noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 100
        self.energy = 50
# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
# noise() - prints out the pet's sound
    def noise(self):
        self.noise

pet_treats=["Biscuits","Chews","Snacks"]
pet_foods =["Crockets","Steak","Fish","Bacon"]

sam = Pet("SAM","DOG",["Funny","Good player"],"HAB HAB!")
Zied = Ninja("ZIED","RIAHI",sam,pet_treats,pet_foods)

Zied.feed()
Zied.feed()
Zied.feed()
Zied.feed()
Zied.feed()