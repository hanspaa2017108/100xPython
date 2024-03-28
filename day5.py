#iterating over lists
 #Repeating Statements

animals = ["dog", "cat", "wolf", "cow"]
print(f"This is a {animals[0]}")
print(f"This is a {animals[1]}")
print(f"This is a {animals[2]}")
print(f"This is a {animals[3]}")

print("---NEW METHOD---")
#for loop method
for i in animals:
    print(f"This is a {i}")

# Use the for loop to print the name of every student on the students list.
students = ["Alia", "Sidharth", "Varun", "Vishal", "Farah"]

print("The nominations for the Student of the Year Award are: ")
for SOTY in students:
  print(SOTY)

#If condition within Loops Method

names = ["Will Granda", "Thomas Cooper", "Charlie Mitchell", "Pepper Cooper", "Samantha Cooper"]
for name in names:
  if name.endswith("Cooper"):
    print(name)

# Use if condition to print all the city names ending with England
cities = ["Dublin, Ireland", "London, England", "Glasgow, Scotland" ,"Liverpool, England", "Bristol, England", "Amsterdam, Netherlands"]
for i in cities:
  if i.endswith("England"):
    print(i)

#Skip statements using continue
fruits=['Banana', 'Pineapple', 'Apple', 'GreenApple', 'MuskMelon']
for i in fruits:
  if "apple" in i:
    continue
  if "Apple" in i:
    continue
  print(f"I AM {i}")

items = ["Brocolli - Food", "Pen - Stationary", "Pasta - Food", "Book - Stationery", "Soap - Cleaning", "Football - Sport", "Salad - Food"]
final_list = []

# Add all items to final_list except sport items
for i in items:
  if "Sport" in i:
    continue
  #i.append(final_list)
  final_list.append(i)
print(final_list)

#Stopping the loop using break
weight_of_apples  = [200, 230, 190, 160, 140, 198, 218]

for apple_weight in weight_of_apples:
  if apple_weight < 150:
    print("Apple below 150gm found. Shipment Cancelled.")
    break
  print("Apple is above 150gm ✓")

# break the loop after house_number 105
#house_numbers = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
#for i in house_numbers && i <= 105:
#  print(f"Delivered to house number {i}")
#  if i > 105:
#    break
#  print("All newspapers delivered.")
  
# break the loop after house_number 105
house_numbers = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

for house_number in house_numbers:
  if house_number > 105:
    print("All newspapers delivered.")
    break

  print(f"Delivered to {house_number}")

#Generating numbers using Range
  
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
for index in range(len(planets)):
  print(planets[index])

# print all the ingredients along with their index using a loop and range()
ingredients = ["cabbage", "carrot", "cauliflower", "mayonnaise", "salt", "peas"]
for i in range(len(ingredients)):
  print(f"Position {i} contains {ingredients[i]}")
  # my error code part: print(f"Position {ingredients(i)} contains {i}")

#Iterating two lists
  
countries = ["India", "China", "Japan", "England", "France"]
capitals = ["New Delhi", "Beijing", "Tokyo", "London", "Paris"]

for country, capital in zip(countries, capitals):
  print(f"The capital of {country} is {capital}")


# Print a line for each pair as `The opposite of *word* is *opposite_word*.`
# Use the zip function

words = ["love", "beautiful", "borrow", "laugh"]
opposite_words = ["hate", "ugly", "lend", "cry"]

for i, j in zip(words, opposite_words):
  print(f"The opposite of {i} is {j}")
  #print(f"The opposite of  {i} is {opposite_words(j)}.") {MY WRONG CODE PART}

#Iterating Nested Lists
teams = [
  ["Shahrukh", "Aamir", "Salman"],
  ["Akshay", "Ajay", "Sunil"],
  ["Katrina", "Bobby", "Amitabh"]
]

i = 1

for team in teams: # outer loop
  print(f"Team {i} consists of: ", end="")

  for member in team: # inner loop
    print(member, end=", ")

  i += 1
  print() # new line


# Print each movie collection along with the price in the format given above.
# Use zip and nested loops

collections = [
  ["The Avengers", "Iron Man", "Thor"],
  ["Justice League", "Man of Steel", "The Dark Knight"],
  ["Titanic", "Avatar", "Spiderman"],
]

prices = [2490, 3120, 1999]

for i,j in zip(collections, prices):
  print(f"Collection |  ₹{j}")
  for i1 in i:
    print(i1)
    
  print()