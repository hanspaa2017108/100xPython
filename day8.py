#Functions

def area():
    width = 6
    length = 12
    print(f"The Area of Rectangle is: {width*length}")
area()

# Define the functions print_passed and print_failed as specified above.
# Call the functions accordingly as per the score.

# define print_passed
def print_passed():
  print("You have passed")
# define print_failed
def print_failed():
  print("You have failed")
  
score = 65
if score >= 45:
  # call print_passed
  print_passed()
else:
  # call print failed
  print_failed()

#Positional Arguments
  
def area(width, length):
    width = 6
    length = 12
    print(f"The Area of Rectangle is: {width*length}")
area(3,5)

# Define a function print_result which accepts a score argument
# Evaluate the score and print the text accordingly
score = 43

# Call print_result with score as an argument
def print_result(score):
  if score >= 45:
    print(f"You have passed the test with a score of {score}")
  else:
    print(f"You have failed the test with a score of {score}")
print_result(score)

#Return Statement
'''
1) Using the return statement we can send the result of the operation back outside
the function, where it can be used for further operations.
2) 

'''

def area(width, length):
  return width * length

result = area(5,4)
print(f"The Area of Rectangle is: {result}")

# Define a function get_result which accepts a score argument
# Call print_result with score as an argument
# Evaluate the score and return the text accordingly

name = "Alice"
score = 55
subject = "English"
date = "15/05/2022"

def get_result(score):
  # Return Passed if score is or greater than 45
  # Return Failed otherwise
  if score >= 45:
    return "passed"
  else:
    return "failed"
    
print("-------------------------------------------------")
print(f"| Name: {name} \t\t| Date: {date} \t|")
print("-------------------------------------------------")
print(f"| Subject: {subject} \t| Score: {score} \t\t|")
print("-------------------------------------------------")
print(f"| Result: \t\t| {get_result(score)} \t\t|")
print("-------------------------------------------------")

#Function Arguments
#Default Arguments

def area(width, length, shape):
  if shape == "rectangle":
    return width * length
  elif shape == "rhombus":
    return width * length / 2
  
result = area(2,3,"rectangle")
print(f"AREA OF RECTANGLE: {result}")

result = area(3,2,"rhombus")
print(f"AREA OF RHOMBUS: {result}")

# Set 0 as the default value for the argument score in the get_result function

name = "Suraj"
subject = "English"
date = "15/05/2022"

def get_result(score=0):
  if score >= 45:
    return "Passed"
  else:
    return "Failed"


print("-------------------------------------------------")
print(f"| Name: {name} \t\t| Date: {date} \t|")
print("-------------------------------------------------")
print(f"| Subject: {subject} \t| Score: --- \t\t|")
print("-------------------------------------------------")
print(f"| Result: \t\t| {get_result()} \t\t|")
print("-------------------------------------------------")

#Keyword Arguments 
#(don't require to be in any order like positional arguments.)
def area(width, length):
  return width * length
result = area(1,8)
print(f"area of rectangle is: {result}")

def area(*, width, length):
  return width * length
result = area(width=1, length=8)
print(f"the area of rectangle is: {result}")

# Convert the argument of generate_report_card to keyword arguments

name = "Alice"
score = 55
subject = "English"
date = "15/05/2022"

def get_result(score=0):
  if score >= 45:
    return "Passed"
  else:
    return "Failed"

def generate_report_card(*,name, date, subject, score=0):
  print("-------------------------------------------------")
  print(f"| Name: {name} \t\t| Date: {date} \t|")
  print("-------------------------------------------------")
  print(f"| Subject: {subject} \t| Score: {score} \t\t|")
  print("-------------------------------------------------")
  print(f"| Result: \t\t| {get_result(score)} \t\t|")
  print("-------------------------------------------------")

generate_report_card(name=name, date=date, subject=subject, score=score)

#Variable Arguments (It will be a tuple containing all the positional arguments given to the function.)
def area(*var, width = 1, length= 2, shape="rectangle"):
  print(var)

area(6,5,shape="rectangle")

#Variable Keyword Arguments (prepended with **)
#Using Variable Arguments
def area(*args, shape="rectangle"):

  if shape == "rectangle":
    width = args[0]
    length = args[1]
    return width * length

  elif shape == "circle":
    radius = args[0]
    return 3.14 * radius ** 2

  elif shape == "cuboid":
    height = args[0]
    width = args[1]
    breadth = args[2]
    return height * width * breadth

# Get area of a Circle
print(f"The area of a circle with radius 5 is {area(5, shape='circle')}")

# Get area of a Rectangle
print(f"The area of a rectangle with width 6 and length 5 is {area(6, 5, shape='rectangle')}")

# Get area of a Cuboid
print(f"The area of a cuboid with height 6 and width 8 and breadth 4 is {area(6, 8, 4, shape='cuboid')}")

#using variable arguments
def area(*, shape="rectangle", **kwargs):

  if shape == "rectangle":
    width = kwargs['width']
    length = kwargs['length']
    return width * length

  elif shape == "circle":
    radius = kwargs['radius']
    return 3.14 * radius ** 2

  elif shape == "cuboid":
    height = kwargs['height']
    width = kwargs['width']
    breadth = kwargs['breadth']
    return height * width * breadth

# Get area of a Circle
print(f"The area of a circle with radius 5 is {area(radius=5, shape='circle')}")

# Get area of a Rectangle
print(f"The area of a rectangle with width 6 and length 5 is {area(width=6, length=5, shape='rectangle')}")

# Get area of a Cuboid
print(f"The area of a cuboid with height 6 and width 8 and breadth 4 is {area(height=6, width=8, breadth=4, shape='cuboid')}")

# Accept scores as variable keyword arguments and calculate the percentage

def calculate_percentage(**scores):
  return sum(scores.values()) / len(scores)

percentage = calculate_percentage(hindi=45, english=76, marathi=66, maths=87, science=78)
print(f"The percentage is {percentage}%")
