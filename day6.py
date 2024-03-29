#Set 
#Creating a Set

create_sets = ['Set1', 'Set2', 'Set3', 'Set4', 'Set5', 'Set2', 'Set1', 'Set2']
print(create_sets)

main_sets = set(create_sets)
print(main_sets)

# create a set by enclosing values within the {}.
number_sets = {'1', '2', '1', '3', '4', '5', '1'}
print(f"Here's the SET {number_sets}")

# Merge emilys_list into mikas_list and convert the combined list into a set
# Print the sorted list from the set (print the sorted list from the resulting set using sorted method)
mikas_list = [
  "Sim Park",
  "Golden Amusement Mall",
  "Red Garden"
]

emilys_list = [
  "Sim Park",
  "Wildlife Safari Zoo",
  "Red Garden"
]

#Method-1
#for i in mikas_list:
#    emilys_list.append(i)

#print(set(emilys_list))

#Method-2
combined_list = mikas_list + emilys_list
final_list = sorted(set(combined_list))
print(final_list)

#Adding values to a Set
animals = {"cat", "dog", "pig", "cow"}
print(animals)

animals.add("horse") # add a new element
print(animals)

animals.add("cow") # add an existing element
print(animals)

animals.add("tiger")
print(animals)

# Add Joshua's suggestion to the final set and print the sorted list from the set.
final_set = {'Sim Park', 'Nature Park', 'Wildlife Safari Zoo', 'Golden Amusement Mall', 'Red Garden'}
joshuas_suggestion = "Willow's Water Park"
final_set.add(joshuas_suggestion)
final_op = sorted(final_set)
print(final_op)

# Add Joshua's suggestion to the final set and print the sorted list from the set.
final_set = {'Sim Park', 'Nature Park', 'Wildlife Safari Zoo', 'Golden Amusement Mall', 'Red Garden'}
joshuas_suggestion = "Willow's Water Park"

final_set.add(joshuas_suggestion)
print(sorted(final_set))

#Removing values from a Set
animals = {"cat", "dog", "pig", "cow"}
print(animals)

animals.remove("dog")
print(animals)
animals.remove("cat")
#animals.remove("cat", "pig") #{TypeError: set.remove() takes exactly one argument (2 given)}
print(animals)

# Remove Sim Park from the final_set and print the sorted list from the final_set
final_set = {'Sim Park', 'Nature Park', 'Wildlife Safari Zoo', 'Golden Amusement Mall', 'Red Garden'}
final_set.remove("Sim Park")
print(sorted(final_set))

#INTERSECTION B/W SETS
#Common elements among set
animals = {"cat", "dog", "pig", "cow"}
more_animals = {"elephant", "dog", "pig", "chicken"}

common_animals = animals.intersection(more_animals)
print(common_animals)

# Get the common candidates from raghavs_selection and rajivs_selection
raghavs_selection = {"Bob", "Tom", "Elliot", "Stacy"}
rajivs_selection = {"Stacy", "Philip", "Bob", "Tom", "Vishal"}

#Intersection of Raghav's selection from Rajiv's selection
common_selection = raghavs_selection.intersection(rajivs_selection)
print(sorted((common_selection)))

#Difference between Sets
animals = {"cat", "dog", "pig", "cow"}
more_animals = {"elephant", "dog", "pig", "chicken"}

uncommon_animals = animals.difference(more_animals)
print(uncommon_animals)

# Find the difference between all_players and mikes_team and print the sorted list from the result
all_players = {"Joey", "Chandler", "Ross", "Sheldon", "Leonard", "Howard", "Raj", "Ted", "Marshall", "Barney"}

mikes_team = {"Joey", "Ross", "Leonard", "Barney"}
#left_team_players = mikes_team.difference(all_players)
left_team_players = all_players.difference(mikes_team)
print(sorted(left_team_players))

#Combining Sets [.update() and .union()]
    # .union() returns a combined set
    # .update() will update the first set with the values of the second
set_one = {'iMac', 'Mac Mini', 'MBP', 'MBA'}
set_two = {'iPhone', 'iPad', 'iPod', 'Vision Pro'}
print(sorted(set_one.union(set_two)))

# Merge emilys_list into mikas_list and convert the combined list into a set
# Print the sorted list from the set
mikas_set = {
  "Sim Park",
  "Golden Amusement Mall",
  "Red Garden"
}

emilys_set = {
  "Nature Park",
  "Wildlife Safari Zoo"
}
print("#Method-1")
print(sorted(mikas_set.union(emilys_set)))

print("#Method-2")
updated_set = sorted(mikas_set.union(emilys_set))
print(updated_set)

#Subsets (issubset() checks if all the elements from he first set exist in the second set. It returns a boolean of either True or False.)
one = {1,2,3,4,5}
two = {2,3,4,5,6,7}
#print(one.is_subset(two))
print(one.issubset(two))

# Check if all attendees are present in invitees set
invitees = {"Neha", "Pia", "Sushma","Nitin", "Abhilash", "Sonu"}
attendees = {"Neha", "Pia", "Sushma","Rancho", "Farhan", "Raju"}

# i did this...# if invitees.issubset(attendees):
if attendees.issubset(invitees):
  print("All attendees are verified") #{if all attendees are present in the invitees, if yes print this}
  
else:
    print("Some attendees were not invited") #{if no print this(for our output this will be printed)}


#DICTIONARIES (in-built way of storing key-value pairs)... [declared using dict() or {}]

#Creating Dictionaries   
# Create a dicitionary called `registry` with the data given above and print it
registry = {
  "Luis Castelino": "21-July-1951", "Michael Thompson": "24-August-1990",
  "Bob Elliot": "05-January-1993", "Sheryl Mendes": "13-April-2009",
}
print(registry)

#Accessing Dictionaries

fruits_and_colors = {
  "grapes": "green",
  "apple": "red",
  "banana": "yellow",
  "orange": "orange"
}

print(fruits_and_colors)
print(fruits_and_colors['apple'])
print(fruits_and_colors['grapes'])
print(fruits_and_colors['grapes'])
#print(fruits_and_colors['strawberry'])
print(fruits_and_colors.get('strawberry'))
print(fruits_and_colors.get('strawberry', 'NAHI HAI'))

# Fetch the DOB of the person via `name` and print it to the screen

registry = {
  "Luis Castelino": "21-July-1951",
  "Michael Thompson": "24-August-1990",
  "Bob Elliot": "05-January-1993",
  "Sheryl Mendes": "13-April-2009",
}


name = 'Bob Elliot'

#Method-1
dob = registry.get('Bob Elliot')
#for name in registry:
print(f"{name} was born on {dob}")

#Method-2
print(f"{name} was born on {registry[name]}")

# Use a for loop and fetch each customers order from preferences using .get()
# set the default preference to veg for customers whose name is missing
food_preferences = {
  "Raj": "veg",
  "Tom": "non-veg",
  "Susan": "non-veg",
  "James": "veg"
}

customers = ["Raj", "Tom", "Marcus", "Shekhar", "Susan", "James"]
for customer in customers:
  print(f"{customer} has been served {food_preferences.get(customer,'veg')}")

#Inserting into Dictionaries
food_preferences['Aman'] = "Apple"
print(food_preferences)

#food_preferences = {
# "Raj": "veg",
#  "Tom": "non-veg",
#  "Susan": "non-veg",
#  "James": "veg"
#}

# Add Marcus preference as veg
food_preferences["Marcus"] = "veg"
# Add Shekhar preference as non-veg
food_preferences["Shekar"] = "non-veg"
# Print the dictionary
print(food_preferences)

#Deleting from Dictionaries(use "del" keyword)
del food_preferences['Raj']
print(food_preferences)

#Deleting from Dictionaries(use "pop" keyword), .pop() returns the value of deleted data
del_item = food_preferences.pop('James')

# Remove eggs from cart using `.pop()` and print the text using the return value
cart = {
  "eggs": 2,
  "wine bottle": 3,
  "soft drinks": 5
}

item_to_remove = "eggs"
qty = cart.pop(item_to_remove)
print(f"{qty} quantities of {item_to_remove} have been removed from the cart.")

#Looping through Dictionaries
#using .items() to loop through key-value pair in dictionary

for i, j in cart.items():
   print(f"{i} is the name, {j} is availability")

# Print movie timings in the format given using a for loop.

movie_timings = {
  'Cars 2': '10:30 AM',
  'Titantic': '01:00 PM',
  'Mission Impossible 5': '09:30 PM',
}

for movieName, movieTiming in movie_timings.items():
  print(f"Movie: {movieName} | Screening Time: {movieTiming}")

#Checking for keys in Dictionaries

# Add new item to cart. Increase quantity if already exists
cart = {
  "soap": 1,
  "candle": 2
}

new_item = "soap"
if new_item in cart:
  cart[new_item] += 1
else:
  cart[new_item] = 1
  
print(cart)

#Merging Dictionaries(using .update())
# Merge emilys_list into mikas_list and print mikas_list
mikas_list = {
  "Bob": "Sim Park",
  "Neha": "Golden Amusement Mall",
  "Charlie": "Red Garden"
}

emilys_list = {
  "Frank": "Nature Park",
  "Susy": "Wildlife Safari Zoo"
}

mikas_list.update(emilys_list)
print(mikas_list)