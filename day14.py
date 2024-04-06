#Inheriting from other classes
'''
Python supports inheriting data and methods from other classes. This can help us to avoid rewriting common functionalities across multiple classes.
'''

# Inherit Car in Batmobile

class Car:
  def open_door(self):
    print("Opening door.")

  def start_car(self):
    print("Starting Car.")

class Batmobile(Car):
  pass

batmobile = Batmobile()
batmobile.open_door()
batmobile.start_car()

class Maths:
  def addition(self):
    print(1+5)

  def subtraction(self):
    print(1-5)

class Solution(Maths):
  pass

solution = Solution()
solution.addition()
solution.subtraction()

class Phone: # <-- Parent class
  """
  Contains all functionalities and data of a Phone
  """

  def call(self, number):
    print(f"Calling {number}")


class IPhone(Phone): # <-- Inherits Phone class
  """
  Contains all functionalities and data of a Phone and IPhone
  """
  def __init__(self):
    self.ios_version = "12.5.6"

  def get_ios_version(self):
    print(f"iOS Version {self.ios_version}")


class AndroidPhone(Phone): # <-- Inherits Phone class
  """
  Contains all functionalities and data of a Phone and Android Phone
  """
  def open_playstore(self):
    print("Opening Play Store")


print("Calling iPhone methods")
iphone = IPhone()
iphone.call("999999999") # <-- Called from parent (Phone) class
iphone.get_ios_version() # <-- Called from child (IPhone) class

print()

print("Calling Android methods")
android_phone = AndroidPhone()
android_phone.call("999999999") # <-- Called from parent (Phone) class
android_phone.open_playstore()  # <-- Called from child (AndroidPhone) class

# Add shoot_missile method in the Batmobile class

class Car:
  def open_door(self):
    print("Opening door.")

  def start_car(self):
    print("Starting Car.")


class Batmobile(Car):
  # Add shoot_missile() method here
  def shoot_missile(self):
    print("Sssswossshhhhhh . . . Boom!")

  pass

batmobile = Batmobile()
batmobile.start_car()
batmobile.shoot_missile()

#Overriding methods

class Phone:
  """
  Parent Class
  """
  def send_email(self, email_id):
    print(f"Sending an email to {email_id} via Email")

class IPhone(Phone):
  """
  Child Class
  """
  def send_email(self, email_id): # <-- Child class with same method name and args as parent class
    print(f"Sending an email to {email_id} via Apple Mail")

print("Calling Phone methods")
phone = Phone()
phone.send_email("abc@gmail.com") # <-- Called from Parent class

print()

print("Calling iPhone methods")
iphone = IPhone()
iphone.send_email("abc@gmail.com") # <-- Overwritten method called from Child class

# Overwrite the refuel method in Batmobile class

class Car:
  def refuel(self):
    print("Filling Gas...")


class Batmobile(Car):
  # Overwrite refuel method here
  def refuel(self):
    print("Connecting to Charging port")
  #pass

batmobile = Batmobile()
batmobile.refuel()

#The super function
'''
super() refers to a temporary instance of the parent class.
There are times when we might wish to call the overwritten method 
from the parent class before executing the method from the child class. 
'''

class Phone:
  """
  Parent Class
  """
  def power_up(self):
    print("Powering up Phone.")


class IPhone(Phone):
  """
  Child Class
  """
  def power_up(self):
    super().power_up() # <-- Calls Phone.power_up()
    print("Showing apple logo")


print("Calling iPhone methods")
iphone = IPhone()
iphone.power_up()

# use super() to add additional functionality to the do_action method

class Car:
  def do_action(self, key):
    if key == "W":
      print("Switching on Lights")
    elif key == "H":
      print("Blowing horn")


class Batmobile(Car):
  def do_action(self, key):
    # make changes here
    super().do_action(key)
    if key == "E":
      print("Spinning Batmobile")

batmobile = Batmobile()
batmobile.do_action("W")
batmobile.do_action("E")

#Inheriting from multiple classes

class Phone:
  """
  Contains all functionalities and data of a Phone
  """
  def call(self, number):
    print(f"Calling {number}")


class Camera:
  """
  Contains all functionalities and data of a Camera
  """

  def open_camera(self):
    print(f"Opening Back camera")

class IPhone(Phone, Camera):
  def __init__(self):
    print("Switching on iPhone")

iphone = IPhone()
iphone.call("123456789") # <-- Calls from Phone class
iphone.open_camera() # <-- Calls from Camera class

class Phone:
  """
  Contains all functionalities and data of a Phone
  """
  def start(self):
    print(f"Opening Caller")


class Camera:
  """
  Contains all functionalities and data of a Camera
  """

  def start(self):
    print(f"Opening Camera")

class IPhone(Phone, Camera):
  def __init__(self):
    print("Switching on iPhone")

iphone = IPhone()
iphone.start() # <-- Calls from Phone class

# Inherit Car and Weapon in Batmobile

class Car:
  def open_door(self):
    print("Opening door.")

  def start_car(self):
    print("Starting Car.")

class Weapon:
  def inflict_damage(self):
    print("Health was reduced by 40")

class Batmobile(Car, Weapon):
  pass


batmobile = Batmobile()
batmobile.open_door()
batmobile.start_car()
batmobile.inflict_damage()