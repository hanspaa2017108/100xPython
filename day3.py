#print('it's my life')
print("it's my life")
print('it\'s my life')

list = [1,2,3,4,5,6,7,8,9]
print(list)
for i in list:
    print(i)

list.append(13)
for i in list:
    print(i)
print("")
print(list)

#list.add('Hello!') #can't do this

set={'I', 'AM', 'THE', 'HALF_BLOOD PRINCE', '?'}
print(set)
set.add('Harry Potter')
print(set)

s=0
for i in set:
    print("HP WHAT?: " + i)
    print("before adding:", s)
    s = s + 1
    print("after adding:", s)
print(s)

#def num_function(numbers):
#   return numbers % 2 == 1
#for i in range(15):
#    print(i, 'is', 'odd', if num_function(i) else 'even')

#tuples aur dictonaries karne hai

#print 1 to 100

def print_1_to_100():
    for i in range(1,101):
        print(i)
print_1_to_100()

#print msg n times

def print_msg_ntimes(n, message:str):
    for i in range(n):
        print(message)
print_msg_ntimes(2, 'hey')

print("-----DIVISION-----")

def division(num1:int, num2:int):
    #return 0
    value = 0
    for i in range(num2):
        value = num1-num2
        return value

print('should be true: ', division(150,15) == 10)

print("-----MULTIPLY-----")

def multiply(num1, num2):
    value = 0
    for i in range(num2):
        value += num1
    return value

print('should be true: ', multiply(12,6) == 1)

print("-----DIVISION_GPT-----")

def division(num1: int, num2: int) -> int:
    # Initialize the result to 0
    result = 0
    
    # Keep subtracting num2 from num1 until num1 becomes less than num2
    while num1 >= num2:
        num1 -= num2
        result += 1
    
    return result

# Test the function
print('should be true:', division(150, 15) == 9)

#STRING FORMATTING
# Use the data below to print "Hi, My name is `name`. I was built in the year `year`. To give me a command say `command`."
# Use str() to join numbers to the sentence

name = "Wall-E"
year = 2008
command = "Hello Wall-E"
print("Hi, My name is "+name+". I was built in the year "+str(year)+". To give me a command say "+command+".")

# Given the details below, use .format() to construct a the text mentioned above.

rover = "Mangal"
hour = 9
am_pm = "PM"
date = 24
month = "July"
print("ISRO is happy to announce the successful landing of {rover}, on the surface of Mars at {hour} {am_pm} on {date} {month}.".format(rover=rover, hour=hour, am_pm=am_pm, date=date, month=month))

# Add the details mentioned below to the print statements given below.
# i.e Name:   Bob
# Use F-strings

name = "Bob"
age = 24
gender = "Male"
issue = "Severe chest pain"

print("-------- ABC HOSPITTAL -----------")
print(f"Name:\t\t {name}")
print(f"Age:\t\t {age}")
print(f"Gender:\t\t {gender}")
print(f"Issue:\t\t {issue}")

# Calculate the next leap year within the F-string and print it to the screen
# Expected output: The next leap year is `year`

previous_leap_year = 2020
print(f"The next leap year is {previous_leap_year + 4}")

name = "tom"
age = 32
print(f"My name is {name.capitalize()}. I was born in {2022-age}")

# Pad the codes given below with 00 using String formatting syntax
# i.e Elena Williams    005

print("Operative \t\t Code")
print("-----------------------------")
print(f"Elena Williams \t\t {5:03d}")
print(f"Catherine Smith \t {6:03d}")
print(f"James Bond \t\t {7:03d}")