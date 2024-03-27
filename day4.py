#lists and tuples

#print lists
furniture_needed = ["chair", "table", "bed", "couch"]
print(furniture_needed)

#append lists
# Append the string `tomato` to the `ingredients`
ingredients = ["spaghetti", "onions", "spinach", "carrot"]
#print(ingredients)
ingredients.append("tomato")
print(ingredients)

#remove lists
list_of_animals = ['cat', 'dog', 'sheep', 'horse']
print(list_of_animals)

list_of_animals.remove('sheep')
print(list_of_animals)

ingredients = ["spaghetti", "onions", "spinach", "carrot"]
ingredients.remove('carrot')
print(ingredients)

#Accessing values from a List
# Fetch the 4th value from the `countries` list and print it to the screen.
countries = ["Italy", "Germany", "Australia", "India", "Turkey"]
print(countries[3])

#Length of a List (Python provides a utility function called len() to check the length of the list.)
#find the size of `cart` and print it to the screen.
cart = ["Sugar", "Apple", "Wine", "Eggs", "Chips", "Chewing Gum"]
print(f"You have {len(cart)} items in your cart")

#Search a List
list_of_animals = ['cat', 'dog', 'sheep', 'horse']
print('dog' in list_of_animals)
print('rabbit' in list_of_animals)

# Check if `spinach` is present in the `pasta_ingredients` list. Print Enjoy your meal if spinach is not present. Print Choose a different dish if spinach is present.
pasta_ingredients = ["spaghetti", "onions", "spinach", "carrot"]
if 'spaghetti' in pasta_ingredients:
  print("Choose a different dish")
else:
  print("Enjoy your meal")

#Nested Lists (list within a list)
# Create a nested list with the Movie names given above and print it to the screen
collections = [
  ['The Avengers', 'Iron Man', 'Thor'],
  ['Justice League', 'Man of Steel', 'The Dark Knight'],
  ['Titanic', 'Avatar', 'Spiderman']
]
print(collections)

#Lists vs Tuples (Tuples are read-only and can only be accessed or searched for elements.)
# Declare a tuple `emotions` with values `laugh`, `shout`, `cry` and print it
emotions = ('laugh', 'shout', 'cry')
print(emotions)

#Attempting to add an element to the planets tuple will result in an error.
planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus","Neptune")
planets.append("Neptune")
print(planets)