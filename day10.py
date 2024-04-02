#List destructuring(variables on the left side, values on the right side)
hello, hi, hey = "hey", "hello", "hi"
print(hello, hi, hey)

greetings = ("hey", "hello", "hi")
hello, hi, hey = greetings
print(hello, hi, hey)

creatures = ("Elephant", "Snake", "Dog")
animal_1, animal_2, *others = creatures
print(animal_1, animal_2)
print(f"EXTRA ANIMAL IS: {others}")

# Split the csv_data using .split(", ") and use destructuring
# to store the result in item, quantity and price

csv_data = "Papaya, 3, 50"
split_csv = csv_data.split(", ")
item, quantity, price = split_csv

'''
csv_data = "Papaya, 3, 50"
item, quantity, price = csv_data.split(", ")
print(f"{quantity} quantities of {item} were purchased at ₹{price}")
'''
print(f"{quantity} quantities of {item} were purchased at ₹{price}")

#Destructuring within For Loops (enumerate() function)

names = ["Ricky", "Justin", "Bob"]

for index, name in enumerate(names):
  print(f"The value at index {index} is {name}")

# Iterate through cart using a for loop and get the name, quantity and price through destructuring.
# Calculate the final price for each product using quantity * price
# Print "The total price for ITEM is X" for every item

cart = [
    ("Papaya", 3, 50),
    ("Apple", 5, 20),
    ("Mango", 2, 30),
    ("Banana", 20, 5)
]

for name, quantity, price in cart:
  print(f"The total price for {name} is {quantity * price}")

#Fetching values using negative numbers
list = ["1", "2", "3", "4"]
print(f"NUMBERS ARE: {list[-1]}")
print(f"NUMBERS ARE: {list[-2]}")
print(f"NUMBERS ARE: {list[-4]}")
#print(f"NUMBERS ARE: {list[-5]}")

'''
Given the orders list, which contains the orders (order_id, order_date) sorted by recency ( older ones first ),
help Samwise fetch the most recent order_id using negative indices and print it to the screen.
'''
orders = [
  ('ORDER-170', '14 April 2022'),
  ('ORDER-180', '17 April 2022'),
  ('ORDER-190', '28 April 2022'),
  ('ORDER-200', '29 April 2022'),
  ('ORDER-210', '1 May 2022'),
  ('ORDER-220', '9 May 2022')
]
print(orders[-1][0])

#List Slicing

colors = ["red", "pink", "white", "yellow", "grey", "blue"]
print(colors[0:4])
print(colors[3: 6])
print(colors[4:])
print(colors[:4])
print(colors[-3:])
print(colors[2:-2])

# Fetch the last 3 recent orders and store them in recent orders

orders = [
  ('ORDER-170', '14 April 2022'),
  ('ORDER-180', '17 April 2022'),
  ('ORDER-190', '28 April 2022'),
  ('ORDER-200', '29 April 2022'),
  ('ORDER-210', '1 May 2022'),
  ('ORDER-220', '9 May 2022')
]

# Uncomment the next line and make changes
recent_orders = orders[-3:]
print("The last 3 order were made on: ")
for order in recent_orders:
  print(order[1])

#Filter filter(CRITERIA FOR FILTERING, WHAT NEEDS TO BE FILTERED)

# Filter the orders by date. Fetch only orders made on 10 May 2022
# Print the filtered list

orders = [
  ('ORDER-170', '10 May 2022'),
  ('ORDER-180', '17 April 2022'),
  ('ORDER-190', '10 May 2022'),
  ('ORDER-200', '29 April 2022'),
  ('ORDER-210', '10 May 2022'),
  ('ORDER-220', '10 May 2022')
]

#filtered = list(filter(lambda order: order[1] == '10 May 2022', orders))
#print(filtered)

#Map

# Use map to add a status field to each order. If the order was made on 10 May 2022, add the status as "In Process". For orders on other dates, add the status as "Completed".

orders = [
  ('ORDER-170', '10 May 2022'),
  ('ORDER-180', '17 April 2022'),
  ('ORDER-190', '10 May 2022'),
  ('ORDER-200', '29 April 2022'),
  ('ORDER-210', '10 May 2022'),
  ('ORDER-220', '10 May 2022')
]

def update_status(order):
#   return (order_id, order_date, order status) based on condition
  if order[1] == '10 May 2022':
    return order + ('In Process',)
  else:
    return order + ('Completed',)
 
# use map to add order status and print the new list
#updated_orders = list(map(update_status, orders))
#print(updated_orders)

#List comprehension (inline for loop) {[(return value) for value in list if (condition)]}

# Fetch the order id's of orders delivered by Pippin

orders = [
  ('#4415-170', '14 April 2022', 'Pippin'),
  ('#4416-180', '17 April 2022', 'Merry'),
  ('#4417-190', '20 April 2022', 'Pippin'),
  ('#4418-200', '29 April 2022', 'Hamfast'),
  ('#4419-210', '04 May 2022', 'Pippin'),
  ('#4420-220', '10 May 2022', 'Pippin')
]

pippins_orders = [order_id for order_id, date, agent in orders if agent == "Pippin"]

print(f"Orders delivered by Pippin are {', '.join(pippins_orders)}.")

#Handling Exceptions
#Try and except

countries_and_capitals = {
  "India" : "Delhi",
  "England" : "London",
  "Russia" : "Moscow",
  "USA" : "Washington DC"
}

countries_list = ["India", "England", "Russia", "China", "USA"]
for country in countries_list:
  try:
    print(f"The capital of {country} is {countries_and_capitals[country]}")
  except:
    print(f"--- Key {country} does not exist ---")

# Add a try-except block to handle invalid keys

spells = {
  "X": "Expelliarmus",
  "Y": "Wingardium Leviosa",
  "O": "Avada Kedavra",
  "A": "Lumos",
}

keys_pressed = ["X", "Y", "O", "A", "Ctrl", "Alt", "X"]

for key in keys_pressed:
  # Add try-except block here
  try:
    print(f"Casting Spell: {spells[key]}")
  except:
    print("This key is invalid")

#Capturing Types of Exceptions [KeyError, IndexError]
    
# Add a try-catch block and handle the KeyError and IndexError exceptions

spells = {
  "X": "Expelliarmus",
  "Y": "Wingardium Leviosa",
  "O": "Avada Kedavra",
  "A": "Lumos",
}

wands = ["Elm Wand", "Unicorn Hair Wand", "Elder Wand"]

keys_pressed = ["X", "Y", "3", "O", "A", "K", "H", "1", "6", "2"]

for key in keys_pressed:
  try:
    if key.isdigit():
      print(f"Changing wand to: {wands[int(key)]}")
    else:
      print(f"Casting Spell: {spells[key]}")
  except KeyError:
    print("Spell does not exist")
  except IndexError:
    print("Wand does not exist")

#Fetching the error message

# Capture the exception detail object and pass it to log_error

def log_error(e):
  print("LOGGER: ", e.__class__.__name__, ": ", e)

spells = {
  "X": "Expelliarmus",
  "Y": "Wingardium Leviosa",
  "O": "Avada Kedavra",
  "A": "Lumos",
}

wands = ["Elm Wand", "Unicorn Hair Wand", "Elder Wand"]

keys_pressed = ["X", "Y", "3", "O", "A", "K", "H", "1", "6", "2"]

for key in keys_pressed:
  try:
    if key.isdigit():
      print(f"Changing wand to: {wands[int(key)]}")
    else:
      print(f"Casting Spell: {spells[key]}")
  except Exception as e:
    log_error(e)

#Else Block, Finally block in Try-Except