#COMPREHENSIVE EXERCISE- II
#Check attendees
day_1 = ["3422", "4522", "7743", "2947", "2846", "1038", "8354", "2593", "7324", "7353"]
day_2 = ["9352", "3422", "7353", "1038", "7245", "8354", "9204", "2355", "2353", "7743"]

#both_days = set(day_1) & set(day_2) # both days
both_days = sorted(set(day_1).intersection(day_2))
day_1_attendees = set(day_1) - set(day_2) # only day 1
day_2_attendees = set(day_2) - set(day_1) # only day 2

print(f"Attendees on both days: {both_days}")
print(f"Attendees only on first day: {day_1_attendees}")
print(f"Attendees only on second day: {day_2_attendees}")

#Find popular people from the place
people = {
  "Conor McGregor": "Ireland",
  "Obama": "United States",
  "Adbul Kalam": "India",
  "AR Rahman": "India",
  "Tom Cruise": "United States",
  "Sharukh Khan": "India"
}

country_mapping = {}

for name, country in people.items():
  if country in country_mapping:
    country_mapping[country].append(name)
  else:
    country_mapping[country] = [name]

for country, people in country_mapping.items():
  print(f"The popular people from {country} are {people}")

#While Loop
i = 10
while i > 0:
  print(f"value of i is {i}")
  i-=1

# Use a while loop to assign seats until seat_number is 100
# Print **All seats have been assigned** once done
available_seats = 100
seat_number = 1
while available_seats >= seat_number:
 print(f"You have been assigned seat number {seat_number}")
 seat_number += 1
print("All seats are occupied")

#While loop for Lists
list = ["MANGO", "BANANA", "ORANGE", "APPLE", "JACK FRUIT"]
while list:
  remove_list = list.pop()
  print(f"Removing {remove_list} from the list")

print("The Bag is now empty")

'''
list = ["MANGO", "BANANA", "ORANGE", "APPLE", "JACK FRUIT"]
while list:
  list.pop()
  print(f"Removing {list} from the list")

print("The Bag is now empty")
'''
# pop tickets out of screen_four_tickets until its empty
# print Ticket X: Checked In for every ticket popped
screen_four_tickets = ['TCKT23', 'TCKT45', 'TCKT06', 'TCKT18', 'TCKT32', 'TCKT11', 'TCKT24']
while screen_four_tickets:
  checked_in = screen_four_tickets.pop()
  print(f"Ticket {checked_in}: Checked In")

#Nested While loops
  
numbers_list_1 = [15, 16, 17]
numbers_list_2 = [1, 2, 3, 4, 5]

i = 0

while i < len(numbers_list_1): # outer loop
  j = 0

  while j < len(numbers_list_2): # inner nested loop
    num_1, num_2 = numbers_list_1[i], numbers_list_2[j]
    print(f"The product of {num_1} * {num_2} is {num_1 * num_2}")
    j += 1

  print("-------------------------------")

  i += 1


# Use nested while loops to iterate through the Nested List `fish_tank`
# Print Found Nemo at `i,j` when `*` is found.
fish_tank = [
  ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
  ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
  ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
  ['w', 'w', 'w', 'w', 'w', '*', 'w', 'w', 'w', 'w'],
  ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
]

i = 0
while i < len(fish_tank):
  j = 0
  while j < len(fish_tank[i]):
    if fish_tank[i][j] == "*":
      print(f"Found Nemo at {i},{j}")
    j+=1
  i+=1
