#Lambda Function
'''
this code defines a Lambda function that takes in an input x and returns its square
'''
square = lambda x : x*x
print(square(3))

# Write a lambda function to check if a student has passed or failed
score = 56

# Assign the function to check_result
check_result = lambda x: "Passed" if x>=45 else "Failed"

print(check_result(score))

#Lambda functions in map
circle_radii = [1,2,3,4,5]
circle_area = list(map(lambda x : 3.14 * x * x, circle_radii))
print(circle_area)

# Convert student marks to percent.
# There are 6 subjects of 100 marks each
# To get the percent we divide the marks scored by 6

marks_scored = [502, 482, 398, 403, 356]
#passed_failed = list(map(lambda x : (x/6) "Passed" if x>=45 else "Failed")
passed_failed = list(map(lambda x: "Passed" if x / 6 >=45 else "Failed", marks_scored))
print(passed_failed)

#String
#Separating Strings by character

characters = "Aman  Kaif Menon Dixit Chauhan"
#characters = "Aman, Kaif, Menon, Dixit, Chauhan"
print(characters.split(", "))
print(characters.split())

headers = ["Name" ,"Age","Phone","City"]
data = "Tom,25,9838572948,Bengaluru\nBob,29,8273885932,Jaipur\nSuresh,45,9273285631,Goa"

# Split data on every new line and assign to customers
customers = data.split("\n")

for customer in customers:

#   Split every customer data value into data_split
  data_split = customer.split(",")

  for column, value in zip(headers, data_split):
    print(f"{column.capitalize()}: {value}")

  print("---------------------------------")

#Joining Strings by character
  
characters = ["Aman", "Kaif", "Gaurav", "Vaibhav", "Aditya"]
print(f"The Students from MMO group were: {', ' .join(characters)}")

headers = ["Name" ,"Age","Phone","City"]
data = [
  ['Tom', '25', '9838572948', 'Kochi'],
  ['Bob', '29', '8273885932', 'Delhi'],
  ['Rob', '45', '9273285631', 'Miami'],
]

print("-------------------------------------------------------------")
# join headers using '\t|\t' here and print it
print('\t|\t'.join(headers))


print("-------------------------------------------------------------")
for record in data:
  # join record using '\t|\t' here and print it
  print('\t|\t'.join(record))

#Convert lowercase to uppercase
# Change the name to capital letters and the address to small letters.
customer = {
  'name': 'Vivek Maurya',
  'address': 'Gandhi Nagar, Shimla'
}

# change here
customer['name'] = customer['name'].upper()
customer['address'] = customer['address'].lower()

print(customer)

#Capitalize the first letter [.capitalize()]
# Correct the sentence by converting the text to lowercase and capitalizing the first letter of every sentence
'''
text = "i like travelling to Different Places. it is My Hobby. My other Hobbies include Reading, Dancing and Singing."
one = text.lower()
print(one)
two = one.split(".")
print(two)
three = one.capitalize()
print(three)
'''
text = "i like travelling to Different Places. it is My Hobby. My other Hobbies include Reading, Dancing and Singing."

lower_text = text.lower()
split_text = text.split(". ")
capitalized_text = []

for text in split_text:
  capitalized_text.append(text.capitalize())

result = ". ".join(capitalized_text)
print(result)

#Remove extra spaces from text [.strip()]
# Remove the extra whitespace from the name and address using strip()
customer = {
  'name': '    Alice Allens  ',
  'address': '   New Jersey, USA\n'
}
customer['name'] = customer['name'].strip()
customer['address'] = customer['address'].strip()
print(customer)

#Find the index of a word
text = "Aman before being promoted as CEO headed the Vision Products Group. At the Vision Products Group he was responsible for iteration, development and launch of Vision Ultra."
find_text = text.find("Vision")
print(f"THE TEXT WAS FOUND AT {find_text}")
find_text_again = text.find("Vision", find_text+1)
print(f"THE TEXT WAS FOUND AT {find_text_again}")
find_text_again_1 = text.find("Vision", find_text_again+1)
print(f"THE TEXT WAS FOUND AT {find_text_again_1}")

# Check if the number exists in text using find
# Print "The number is present at index `INDEX`" if it is present
# Print "The number is not present" if the number is missing
text = "Joseph +91-755-502-2339 Tom +91-915-551-9087 Bob +91-855-526-6867 Alice +91-755-585-7865 Carol +91-755-507-6331 Meenal +91-855-571-9817 Rose +91-855-596-4437 Alan +91-755-500-8969"

number = "+91-755-585-7865"
number_find = text.find(number)
if number in text:
  print(f"The number is present at index {number_find}")
else:
  print("The number is not present")

'''
# Check if the number exists in text using find
# Print "The number is present at index `INDEX`" if it is present
# Print "The number is not present" if the number is missing
text = "Joseph +91-755-502-2339 Tom +91-915-551-9087 Bob +91-855-526-6867 Alice +91-755-585-7865 Carol +91-755-507-6331 Meenal +91-855-571-9817 Rose +91-855-596-4437 Alan +91-755-500-8969"

number = "+91-755-585-7865"

index = text.find(number)

if index != -1:
  print(f"The number is present at index {index}")
else:
  print("The number is not present.") 

#
'''

#Replace a word [.replace()]
# Replace Alice's old number with her new number

text = "Joseph +91-755-502-2339 Tom +91-915-551-9087 Bob +91-855-526-6867 Alice +91-755-585-7865 Carol +91-755-507-6331 Meenal +91-855-571-9817 Rose +91-855-596-4437 Alan +91-755-500-8969"

number = "+91-755-585-7865"
new_number = "+91-855-590-7672"
new_text = text.replace(number, new_number)
#new_text = text.replace("number", "new_number")
print(new_text)

#Find whether a string is a digit [.isdigit() method in Python tells us if the particular string is a valid integer or not.]
age_list = [23, 45, "53", "45", 67, 22, 34, "23.45", "ab"]
verified_age = []

for age in age_list:
  if type(age) == int:
    verified_age.append(age)
  elif type(age) == str:
    if age.isdigit():
      verified_age.append(int(age))  
print(verified_age)

#Selecting a subset of a string
movie = "Spiderman: No Way Home"

print(f"The first character is {movie[0]}")
print(f"Midway this character is: {movie[5]}")
print(f"The last character is {movie[-1]}") # gets the last character
print(f"The length of the string is {len(movie)}")
#string slicing.
print(f"STRING SLICING... {movie[:0]}")

#Selecting a subset of a string (EXERCISE)
text = "Leonidus nodded to his wife and turned towards the messenger and said \"Madness? This is SPARTAAA!\""

start = text.find("\"") + 1
end = text.find("\"", start)

print(text[start:end])