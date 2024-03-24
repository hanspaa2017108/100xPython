# datatypes in Python- [Day 1/100]
print("Hello World!")
print(25*6)
print(24-32)
print(23+9)
print(5/10)
print(type(0) is None)# Check if 0 is the same as `None`
print("NAME\t AGE\nAMAN\t 22\nKAIF\t 22\nGAURAV\t 22")
print('aman\nhanspal\n22 years\ndypu')

# operators in Python- [Day 1/100] 

#arithmetic operators
print(11**3) #Exponent operator
print(22 // 10) #floor division operator

#comparision operators
print('apple' == 'banana')
print("Hello World" != "hello world") #inequality operator
print((16/2) <= 8) #greater/less than operator
print(10000<= 24 ** 3 <=15000) #Chaining Operators

#operator precedence 
#(prioritize the multiplicative and divisive operators over the additive and subtractive operators)
# Change to order of operation to calculate the result of 3+5 * result of 23-4.
print((3 + 5) * (23 - 4))
print("Operators\t Priority\n()\t         1\n**\t         2\n*, /, //, %\t 3\n+, -\t         4\n")

#variables in Python- [Day 1/100]

number_of_shoes = 3
print(number_of_shoes)

# Assign "Hello " to a variable named `greeting`, Concatenate it to "World" and print 
greeting = "Hello"
print(greeting + " World")

# print type of `favorite_food`, `over_speed_limit` and `age`.
favorite_food = "cheeseburger"
over_speed_limit = True
age = 24

print(type(favorite_food))
print(type(over_speed_limit))
print(type(age))

#Variable Naming Tip
#characters from a to z, numbers and _ are supported in variable names
#Variables names cannot start with a number
#Variable names are case sensitive

#Python variables are generally declared in snake case
#no_of_animals = 13 # recommended
#noOfAnimals = 13 # not recommended