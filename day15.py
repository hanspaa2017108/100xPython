#Overloading the + operator for objects
#Overloading other mathematical operators

class Basket:
  def __init__(self, items):
    self.items = items

  def __lshift__(self, basket): # <-- Overload << operator
    self.items += basket.items # <-- Add items from other basket to current basket
    basket.items = [] # <-- Empty other basket

  def __repr__(self):
    items_str = ', '.join(self.items)
    return f"Basket[items: [{items_str}]]"

non_empty_basket = Basket(["apples", "eggs", "milk"])
empty_basket = Basket([])

print(f"Non Empty Basket: {non_empty_basket}")
print(f"Empty Basket: {empty_basket}")

print("\nMoving items from non empty basket to empty basket\n")

empty_basket << non_empty_basket # <-- Move items

print(f"Non Empty Basket: {non_empty_basket}")
print(f"Empty Basket: {empty_basket}")


class Egg:
  pass

class EggCrate:
  def __init__(self):
    self.no_of_eggs = 0

  def __add__(self, item):
    self.no_of_eggs += 1

  def __sub__(self, item):
    self.no_of_eggs -= 1

  def __repr__(self):
    """Do not touch this code"""
    no_of_rows = self.no_of_eggs // 5
    last_row_no = self.no_of_eggs % 5
    full_row = "|".join(["⚪"] * 5)
    empty_row = "|".join(["⏺"] * 5)

    rows = "\n".join([full_row] * no_of_rows)

    if last_row_no > 0:
      last_row = "|".join(["⏺" if i > last_row_no else "⚪" for i in range(1, 6)])
      rows = "\n".join((rows, last_row))
      no_of_rows += 1

    empty_rows_no = 6 - no_of_rows
    emp_row_str = "\n".join(([empty_row] * empty_rows_no))
    return "\n".join((rows, emp_row_str))

crate = EggCrate()

for _ in range(16):
  crate + Egg()

crate - Egg()
crate - Egg()

print(crate)

#Overloading unary operators
class LightBulb:
  def __init__(self):
    self.switch = 'OFF'

  def __invert__(self): # <-- This operator takes no arguments
    if self.switch == 'ON':
      self.switch = 'OFF'
    elif self.switch == 'OFF':
      self.switch = 'ON'

  def __repr__(self):
    return f"LightBulb: {self.switch}"

bulb = LightBulb()
print(bulb)

print("\n Switching on Bulb \n")

~bulb # <-- Invert bulb
print(bulb)

print("\n Switching off Bulb \n")

~bulb # <-- Invert bulb
print(bulb)


class Egg:
  pass

class EggCrate:
  def __init__(self, no_of_eggs):
    self.no_of_eggs = no_of_eggs

  def __repr__(self):
    """Do not touch this code"""
    no_of_rows = self.no_of_eggs // 5
    last_row_no = self.no_of_eggs % 5
    full_row = "|".join(["⚪"] * 5)
    empty_row = "|".join(["⏺"] * 5)

    rows = "\n".join([full_row] * no_of_rows)

    if last_row_no > 0:
      last_row = "|".join(["⏺" if i > last_row_no else "⚪" for i in range(1, 6)])
      rows = "\n".join((rows, last_row))
      no_of_rows += 1

    empty_rows_no = 6 - no_of_rows
    emp_row_str = "\n".join(([empty_row] * empty_rows_no))
    return "\n".join((rows, emp_row_str))

  def __invert__(self):
    self.no_of_eggs = 0

crate = EggCrate(10)
~crate
print(crate)

#Overloading comparison operators
class Cart:
  def __init__(self, items):
    self.items = items
    self.total = sum(items.values())

  # Overload operators
  def __eq__(self, cart):
    return self.total == cart.total

  def __gt__(self, cart):
    return self.total > cart.total

  def __lt__(self, cart):
    return self.total < cart.total


cart_1 = Cart({"milk": 19, "carrots": 50, "eggs": 100})
cart_2 = Cart({"potatoes": 40, "turnips": 13, "banana": 98})

print(cart_1 == cart_2)


class File:
  def __init__(self, filename, filesize):
    self.filename = filename
    self.filesize = filesize

  def __eq__(self, file):
    return self.filesize == file.filesize

  def __gt__(self, file):
    return self.filesize > file.filesize

  def __lt__(self, file):
    return self.filesize < file.filesize

file_one = File("file1.txt", 243432)
file_two = File("file2.txt", 6755352)

if file_two < file_one:
  print(f"{file_one.filename} is larger in size")
elif file_one < file_two:
  print(f"{file_two.filename} is larger in size")
elif  file_one == file_two:
  print(f"{file_two.filename} and {file_two.filename} are the same size")


#Handling multiple types in Overloaded Operators
class Bedroom: # <-- Bedroom class
  def __init__(self, room_owner):
    self.owner = room_owner

  def __repr__(self):
    return f"{self.owner}'s bedroom"


class Bathroom: # <-- Bathroom class
  def __init__(self, room_owner):
    self.owner = room_owner

  def __repr__(self):
    return f"{self.owner}'s bathroom"


class House:

  def __init__(self):
    self.bedrooms = []
    self.bathrooms = []

  def __add__(self, room): # <-- operator overloading done here
    if isinstance(room, Bathroom): # <-- if room is a Bathroom
      self.bathrooms.append(room)
    elif isinstance(room, Bedroom): # <-- if room is a Bedroom
      self.bedrooms.append(room)
    return house

  def __repr__(self):
    bedroom_names = [str(room) for room in self.bedrooms]
    bedroom_str = ', '.join(bedroom_names)

    bathroom_names = [str(room) for room in self.bathrooms]
    bathroom_str = ', '.join(bathroom_names)
    return f"House[bedrooms: [{bedroom_str}], bathrooms: [{bathroom_str}]]"



house = House()
judys_bedroom = Bedroom("Judy")
house = house + judys_bedroom
print(house)


arthurs_bathroom = Bathroom("Arthur")
house = house + arthurs_bathroom
print(house)


# Overload the + operator to accept string or file as data arg
# If data is str, append to content
# if data is File, append content of file to content of current file

class File:
  def __init__(self, filename, content):
    self.filename = filename
    self.content = content

  def __repr__(self):
    return f"File(contents={self.content})"

  def __add__(self, data):
    if isinstance(data, File):
      self.content += data.content
    elif isinstance(data, str):
      self.content += data

file_one = File("file1.txt", "Hello World. ")
file_two = File("file2.txt", "How are you doing? ")

file_one + "This is Jamie. "
file_one + file_two
print(file_one)
