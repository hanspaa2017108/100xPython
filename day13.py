#Defining Classes
class Dog: # <-- Define Dog class
  def __init__(self, name, breed):
    self.name = name # <-- Dog has a name
    self.breed = breed # <-- Dog belongs to a breed

  def bark(self): # <-- Dog can bark
    print("Woof")

  def wag_tail(self): # <-- Dog can wag tail
    print("Wagging tail..")

#Creating Objects
dexter = Dog(name="kaif", breed="paaji")
print(f"name of dog is: {dexter.name}")
print(f"breed of dog is: {dexter.breed}")
dexter.bark()
dexter.wag_tail()

# Create Employee class and add the checkin and checkout method
class Employee:
  def checkin(self):
    print("The Employee has entered the building.")
# Create Employee class
  def checkout(self):
    print("The Employee has left the building.")
  # Create checkin method

  # Create checkout method
employee = Employee()
employee.checkin()
employee.checkout()

#The init method, What is self?
'''
The __init__ method is automatically called by Python internally when we create an instance/object of the class. 
We can use it to set attributes within the object when it is created.
Functions within a class are called the methods of that class. 
----

'''

class Dog:
  def __init__(self, name): # <-- __init__ accepts name
    self.name = name # <-- name is assigned to self.name

  def print_name(self):
    print(f"Doggo name is {self.name}") # <-- self.name is printed

  def change_name(self, new_name):
    self.name = new_name


chester = Dog("Chester") # <-- new dog object is created with name
chester.print_name()


chester.change_name("Tio") # <-- another new dog object is created with name
chester.print_name()

# Add a instance attribute "name" and assign it the value "Annie" in the constructor
# Edit the print statements as given above.

class Employee:
    def __init__(self, name):
      self.name = name 
  # define __init__ here
    def checkin(self):
    # update this statement
    #print("The Employee has entered the building.")
     print(f"{self.name} has entered the building.")

    def checkout(self):
    # update this statement
    #print("The Employee has left the building.")
     print(f"{self.name} has left the building.")

employee = Employee("Annie")
employee.checkin()
employee.checkout()

#Class attributes

class Dog:
  NO_OF_OBJECTS = 0 # <-- This is a class attribute

  def __init__(self, name):
    self.name = name
    Dog.NO_OF_OBJECTS += 1

dog1 = Dog("Ringo")
dog2 = Dog("Tyson")
dog3 = Dog("Popsy")

print(Dog.NO_OF_OBJECTS) # Prints the number of objects created

# Add an id field to the Employee class.
# An incremented ID shlould be assigned when a new object is created.

class Employee:
  CURRENT_MEMBERS = 0
  # Create class attribute count

  def __init__(self, name):
    self.name = name
    Employee.CURRENT_MEMBERS += 1
    self.id = Employee.CURRENT_MEMBERS
    # Create id attribute and assign class attribute count

    # Increment class attribute count

  def checkin(self):
    print(f"{self.name} has entered the building.")

  def checkout(self):
    print(f"{self.name} has left the building.")

employee = Employee("Annie")
print(f"{employee.name}'s Employee ID: ", employee.id)
employee = Employee("Jonas")
print(f"{employee.name}'s Employee ID: ", employee.id)
employee = Employee("Peter")
print(f"{employee.name}'s Employee ID: ", employee.id)


#Find the class of an object
class Dog:
  def __init__(self, name):
    self.name = name

chester = Dog("Chester")
print(chester.__class__.__name__)

#Popular examples of classes and objects
from collections import Counter # import class

counter = Counter("hello world") # Count frequency
print(counter.most_common()) # print most common using .most_common() method