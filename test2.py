Ednaco_Family= ['Emman', 'Elise', 'Erinn', 'Zeke']
for name in Ednaco_Family:
    print("Hi " + name + " Ednaco")


print("=================================")

languages = ['Swift', 'Python', 'Go']

for language in languages:
    print("Hello " + language)
print("Hi " + language)


print("=================================")

digits = [0, 5]
for i in digits:
    print(i)
else:
    print('no items left')

print("=================================")

nums = [1, 2, 3, 4, 5, 6]

n = 2

found = False
for num in nums:
    if n == num:
        found = True
        break

print(f'List contains {n}: {found}')

print("=================================")

def print_sum_even_nums(even_nums):
    total=0
    for x in even_nums:
        if x % 2 == 0:
            print("Sum of Even numbers" + str(total))
            total +=x
        else:
            print("There are odd numbers, cannot add odd number")
            break

print_sum_even_nums([2, 4, 6, 10])

print("====================================")

groceries = ["bananas","butter","cheese","toothpaste"]
for index, grocery in enumerate(groceries):
    print(f"Grocery: {grocery} is at index: {index}.")

print("====================================")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

print("====================================")

for x in range(2, 30, 3):
    print(x)

print("====================================")
for x in range(6):
    print(x)
else:
    print("Finally finished!")

print("====================================")

for x in range(6):
    if x == 5: break
    print(x)
else:
    print("Finally finished!")