#The collections Module
import collections
from collections import Counter
print(collections)

string = "AirPods"
c = Counter(string)
print(c)

string2 = "Apple, Aman, Akash, Anuj, Akash"
string3 = ["Apple", "Aman", "Akash", "Anuj", "Akash"]
c1 = Counter(string2) 
c2 = Counter(string3)  
print(c1.most_common())
#print(c1.most_common(3))
print(c2.most_common())
#print(c2.most_common(3))

# Use counter to counter the number of fours and sixes scored.

runs_scored = [1, 2, 1, 1, 4, 2, 6, 6, 2, 4, 6, 2, 2, 6, 6, 4, 2, 1, 1, 1, 6]

# Use Counter here.
c = Counter(runs_scored)
print(f"Dhoni scored {c[4]} fours and {c[6]} sixes in this match.")

#Default Dictionary

# Group songs by Artist name.
# Use .split() to split the song and artist names
# Use defaultdict to store the result

from collections import defaultdict

favorite_songs = ["Not Afraid-Eminem", "Hotel California-Eagles", "I have a dream-ABBA",
                  "Desperado-Eagles", "Dancing Queen-ABBA", "Space Bound-Eminem", "Chiquitita-ABBA"]

artist_songs = defaultdict(list)

for song in favorite_songs:
  song, artist = song.split('-')
  artist_songs[artist].append(song)

print(artist_songs)

#Storing items with Ordered Dictionary [OrderedDict()]
# Create an ordered dictionary of {item: quantity} given items
from collections import OrderedDict

items = ["cheese", "yoghurt", "tomatoes", "yoghurt", "onions", "milk", "milk", "cheese"]

cart = OrderedDict()
for item in items:
  cart[item] = cart.get(item, 0) + 1

print(cart)

#Tuples with names [namedtuple]
from collections import namedtuple

Person = namedtuple('Person', ['name', 'place', 'age'])
person = Person('Aman', 'Mumbai, India', 22)

print(f"{person.name} is from {person.place} and is {person.age} years old")


from collections import namedtuple

csv_data = "Jupiter, 69911\nSaturn, 58232 km\nUranus, 25362 km\nNeptune, 24622 km\nEarth, 6371 km\nVenus, 6052 km\nMars, 3390 km\nMercury, 2440 km"

Planet = namedtuple('Planet', ['name', 'radius'])
planet_list = []

for line in csv_data.split('\n'):
  name, radius = line.split(', ')
  planet_tuple = Planet(name, radius)
  planet_list.append(planet_tuple)
  
for planet in planet_list:
  print(f"The radius of {planet.name} is {planet.radius}")

#Deque
