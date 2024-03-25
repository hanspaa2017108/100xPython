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