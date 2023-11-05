# Variable declaration
num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
# log statement
print(type(fruit)) # log statement with type check
print(pizza_toppings[1]) # log the second element of the list
pizza_toppings.append('Mushrooms') # Add element of the list
print(person['name']) # Acces value of the name of the dictionary
person['name'] = 'George'
person['eye_color'] = 'blue' # Key error : 'eye_color'
print(fruit[2])
# Condition
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: # length chek
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# for loop
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0 
while(x < 5): # while loop
    print(x)
    x += 1

pizza_toppings.pop() # delete list value
pizza_toppings.pop(1) # delete second list value

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
# function definition
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
# function execution
print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)