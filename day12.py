#Working with the datetime module
from datetime import datetime
print(datetime.now())
today = datetime.now()

print(today.time)
print(today.hour)
print(today.year)
print(today.day)
print(today.month)
print(today.minute)
print(today.second)

#print(datetime.date())
#print(datetime.month())
#print(datetime.year())
#print(datetime.hour())
#print(datetime.minute())
#print(datetime.second())
#print(datetime.day())

# Get the current datetime and print it in the **The current date is dd-mm-yyyy**
#from datetime import datetime

print("---METHOD-1---")
today = datetime.now()
day = today.day
month = today.month
year = today.year
'''
error on taking above today.date > "The current date is <built-in method date of datetime.datetime object at 0x7ffff784b630>-4-2024"
'''
print(f"The current date is {day}-{month}-{year}.")

print("---METHOD-2---")

print(f"The current date is {today.day}-{today.month}-{today.year}.")

#Printing date and time ()

'''
characters preceded with a % are called format codes and translate to a value in Python:-
%A name of current weekend
%d current date of the month
%B month name
%b abv month name
%Y current year (in four digit)
%y current year (in two digit)

%w which day of the week
'''

print(f"It is day {today:%w} of the week")
print(f"It is {today:%a %d, %Y}")

print("---METHOD-1---")
print(f"The current date is {today:%d} {today:%B} {today:%Y} and the time is {today:%I}:{today:%M} {today:%p}.")
print("---METHOD-2---")
print(f"The current date is {today:%d %B %Y} and the time is {today:%I:%M %p}.")

christmas_day = datetime(year=2022, month=12, day=25)
print(f"This year Christmas day comes on a {christmas_day:%A}")

# Create datetime object using the following details
# Print the text given above with the datetime object

date = 15
month = 8
year = 1947

# Initialize the date on the next line
#destination = datetime(day=15, month=8, year=1947)
destination = datetime(year=year, month=month, day=date)
print(f"Setting the travel destination date to {destination:%d %B %Y}.")

#Calculate the difference between times 
'''
datetime objects can be subtracted from each other to find the difference between times. 
This operation returns a timedelta object which has only the attributes days, seconds, and microseconds.
'''
birthday_day = datetime(year=2002, month=4, day=5)
current_date = datetime.now()

# Calculate the difference
delta = current_date - birthday_day

# Update X with the number of days in the following print statement
print(f"Travelling {delta.days} days back in the past.")
print(f"Travelling {delta.seconds} seconds back in the past.")

#Replace a value in datetime [use the replace() method.]
christmas_day = datetime(year=2022, month=12, day=25)

# can use year, month, day, hour, minute, microsecond
last_christmas = christmas_day.replace(year=2021)

time_since = datetime.now() - last_christmas

print(f"It has been {time_since.days} days since the last Christmas")

independence_day = datetime(year=1947, month=8, day=15)
updated_year = 1997

# Update independence_day here
updated_date = independence_day.replace(year=updated_year)
print(f"Setting the travel destination date to {updated_date:%d %B %Y}.")

#Adding time using Timedelta (Sometimes we might want to add or subtract a number of days to/from our date. For this, we use the timedelta() function. The timedelta object adds or removes weeks, days, and time. For example, we could also add an hour to our time.)
from datetime import datetime, timedelta
work_update = datetime.now()
print(f"i will complete the work by...{work_update}")
deadline_work_update = datetime.now() + timedelta(hours=+11)
print(f"i will complete the work by...{deadline_work_update}")


destination_date = datetime(year=2022, month=12, day=25)
travel_days = +7

print("---method1---") #this works on basis of the current machine present time
# Uncomment and assign new date to the variable below
new_destination_date = datetime.now() + timedelta(travel_days)
print(f"Setting the travel destination date to {new_destination_date:%d %B %Y}.")

print("---method2---") #this work on basis of time and other data in input
travel_delta = timedelta(days=travel_days)
new_destination_date = destination_date + travel_delta
print(f"Setting the travel destination date to {new_destination_date:%d %B %Y}.")

print("-------------------------DECORATORS--------------------------")

#A world without decorators
'''
repitition can be avoided using decorators or to wrap the code in any function
'''
import time

def hello_world():
  print("Hello World")

start = time.time()
hello_world()
end = time.time()
print(f"Time taken for to execute hello_world is {end - start} seconds")

#What are decorators?
'''
help us run code before and after other functions.
Decorator functions take in a function as an input and run it between some other code.
'''
import time

def hello_world():
  print("Hello World")

def measure_time(pass_function):
  start = time.time()
  result=pass_function()
  end = time.time()
  print(f"Time taken for to execute hello_world is {end - start} seconds")
  return result

measure_time(hello_world)

def send_message():
  return "Tango, Mango"

def encrypt(function):
  message = function()
  return [ord(c) for c in message]

message = encrypt(send_message)
print(message)

def measure_time(another_function):
  start = time.time()
  result = another_function()
  end = time.time()
  print(f"Time taken for to execute hello_world is {end - start} seconds")
  return result

@measure_time # <-- wraps hello_world in measure_time decorator
def hello_world():
  print("Hello World")

#Nested Functions {A nested function is a function defined within another function.}

#Using Nested Functions in decorators

def measure_time(another_function):
  def wrapper():
    start = time.time()
    result = another_function() # Nested functions have access to variables from parent function
    end = time.time()
    print(f"Time taken for to execute hello_world is {end - start} seconds")
    return result
  return wrapper

@measure_time
def hello_world():
  print("Hello World")

hello_world() 

# Add a nested wrapper function to encrypt and call it with @ symbol

def encrypt(function):
  def wrapper():
   message = function()
   return [ord(c) for c in message]
  return wrapper

@encrypt
def send_message():
  return "Tango, Charlie, Alpha"

message = send_message()

print(message)

#Decorating functions with arguments

#Using multiple decorators on one function