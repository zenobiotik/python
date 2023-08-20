def my_function():
    print("Hello from a function")

my_function()

print("============================")

def my_function(fname):
    print(fname + " Ednaco")

my_function("Emman")
my_function("Elise")
my_function("Erinn")
my_function("Ezekiel")

print("==================================")

def my_function(*kids):
    print("The youngest child is " + kids[1])

my_function("Erinn", "Zeke")

print("===================================")
def my_function(child1, child2):
    print("The youngest child is " + child2)

my_function(child1 = "Erinn", child2 = "Zeke")

print("=======================================")
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly

def my_function(**kid):
    print("His last name is " + kid["lname"])
    print("His first name is " + kid["fname"])

my_function(fname='Ezekiel', lname='Ednaco')

print("=======================================")

def test_foods(food):
    for x in food:
        print(x)

fruits= ["apple", "banana", "cherry"]

test_foods(fruits)


