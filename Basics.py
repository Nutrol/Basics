print("Hello world")
# drawing a triangle
# order of instructions matters alot
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
# Variables and data types
# Strings
phrase = "My name is Brian\n Am 22 yrs old"# \n is used to skip a line
print(phrase)
print(phrase.lower())# prints phrase in lower case
print(phrase.upper())# prints phrase in upper case
print(phrase.upper().isupper()) # tells if upper case or not
print(len(phrase))
print(phrase[0]) # extracting first character in phrase
print(phrase[1])
print(phrase.index("M",))
print(phrase.replace("22","23"))
print("name" in phrase)
print(phrase.title())

first = "John"
last = "smith"
message = f'{first}[{last}] is a coder' #formating strings
print(message)

# setting length limits in strings



# Integers
print(2)
print(4/2)
print(10%3) # gives the remainder
x = 5
print(str(x))
y = -6
print(abs(y))
print(pow(3,2)) # 3^2
print(round(3.7))

from math import * # imports a bunch of math functions
print(ceil(3.7))
print(sqrt(36))


# lists
fruits = ["mangoes","bananas"]
print(fruits[0])
fruits.sort()
print(fruits)
numbers = [3,10,7,8]
numbers.sort()
print(numbers)
numbers.reverse()

# tuples
# they can't be modified
coordinates = (4, 5)
print(coordinates[1])

# functions
def say_hi(name, age):
    print("Hello " + name + ", you are" + age)
say_hi("mike","20")

# return statement
def cube(num):
    return num*num*num
print(cube(3))


# arithmetic opperators
print(10/3)
print(10**2) # power
print(10//3)
print(10%3)


# logical and comparison operators
temperature = 20
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")


name = "hghfjfj"
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Nice name")

# while loops
i = 1
while i <= 5:
    print(i)
    i += 1
print("Done")

x = (1)
while x>2:
    print("x is greater than 2")
else:
    print("x is less than 2")


def calculator(num1,num2,operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

print(calculator(10,2,"+"))
print(calculator(10,2,"/"))
print(calculator(10,2,0))

# for loop
for item in ['Mosh','John','Serah']:
    print(item)
    for item in range(10):
        print(item)

prices = [10,20,30]
total = 10
for price in prices:
    total += price
    print(f"Total:{total}")


for x in range(4):
    for y in range(3):
        print(f"({x} , {y})")