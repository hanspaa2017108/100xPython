# if-else statements- [Day 2/100]

#if condition
fruit_1 = "apple"
fruit_2 = "apple"
if fruit_1 == fruit_2: # Check if `fruit_1` is equal to `fruit_2`
  print("It's the same fruit") # print "It's the same fruit" is they are same

#if not condition
weather = "sunny"
if not weather == "raining":# Check if the variable weather is not equal to **raining**.
  print("It's movie time")# Print "It's movie time" if it is not.

#if else condition
# Check if `weather` is "cloudy" and print accordingly
weather = "cloudy"
if weather == "cloudy":
  print("Carry an Umbrella")
else:
    print("Do not carry an Umbrella")

#elif condition
# Check the `weather` using if/elif/else conditions.
# Print the statements as per the conditions above
weather  = "cold"
if weather == "raining":
  print("Wear a Raincoat")
elif weather == "sunny":
  print("Wear a Hat")
elif weather == "cold":
  print("Wear a Sweater")
else:
  print("You do not need any additional wear")

#Multiple Conditions
  # and condition: both conditions must be true for print st to execute
  # or condition: any 1 condition must be true for print st to executex

# Check if Johnny has been eating sugar and telling lies about it to his father
# print *Open your mouth* if he has.

eating_sugar = True
telling_lies = True

if eating_sugar == True and telling_lies == True:
  print("Open your mouth")

# Use conditions with or to find if the weather is rainy or cloudy
# Print *Carry an Umbrella* if it is
weather = "cloudy"
#weather1 = "rainy"
#if weather == cloudy or weather1 == rainy
  #print(Carry an Umbrella)
if weather == "cloudy" or weather == "rainy":
  print("Carry an Umbrella")

#inline if/else statement 
#Joseph would like to go on a trip within his budget. Use inline if/else statement to check if his budget is greater than 600. Return Paris if it is else return Goa.
#Store the return value in destination variable and print it.
  
budget = 400
destination = "Paris" if budget > 600 else "Goa"
print(destination)

# Display report card remarks using if else
score = 28
if score == 100:
  print("Outstanding")
elif 80 < score < 100:
  print("Excellent")
elif 60 < score < 81:
  print("Good")
elif score <=60:
  print("Can do better!")

# Calculate electricity bill using if else
  
units = 241
if 0 < units < 100:
  print((units*1.5))
elif 101 < units < 200:
  print((units*2.5))
elif 201 < units < 300:
   print((units*4.0))
elif 301 < units < 350:
  print((units*5.0))
#else units > 300: #invalid syntax
else:
  print(1500)

#Build a currency converter
usd_value = 5000
target_currency = "INR"

if target_currency == "INR":
  target_value = usd_value * 76
elif target_currency == "JPY":
  target_value = usd_value * 126
elif target_currency == "EUR":
  target_value = usd_value * 0.9

print(target_value)

#Build a currency notes calculator
#Monica has to pay her monthly rent to the landlord. She currently only has 10 rupee notes, 50 rupee notes and 100 rupee notes. Given the amount, help her calculate the number of 10 rupee notes, 50 rupee notes and 100 rupee notes she will need to pay to her landlord.

rent = 9330
no_100_notes = 0
no_50_notes = 0
no_10_notes = 0

# Calculate the number of notes required to meet the given rent amount
no_100_notes = rent // 100
rent = rent % 100

no_50_notes = rent // 50
rent = rent % 50

no_10_notes = rent // 10
rent = rent % 10

# Print the result
print("Monica will require:")
print(str(no_100_notes) + " x ₹100 notes")
print(str(no_50_notes) + " x ₹50 notes")
print(str(no_10_notes) + " x ₹10 notes")
