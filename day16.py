#Generators
'''
A function is paused after it yields a value and resumes when it is explicitly asked.
Generators are basically stateful functions. They can be paused and resumed at specific points

The yield keyword is similar to the return keyword wherein it returns a value from the function.
The difference between them is that the return keyword exits the function, while the yield, pauses the function.

A function with a yield statement can be called a Generator. 
Generators are paused when the yield keyword is used. 
To resume these functions we call them using next().

Generators are extremely useful when we would like to iterate through large or infinite data. 
The next item is not fetched/calculated until it is explicitly asked for.
'''

def hotel():
    yield "samosa"

    yield "pav bhaji"

    yield "idli"

waiter = hotel()

print(next(waiter))
print(next(waiter))
print(next(waiter))

#Generating the Fibonacci Sequence

def fibonacci():
  # yield 0 and 1 directly
  first = 0
  yield first
  second = 1
  yield second

  while True: # Loop infintely
    third = first + second # <-- Calculate the next number in the series
    yield third # <-- Yield the next number in the series
    first = second
    second = third

fib_gen = fibonacci()
for _ in range(10): # Loops for 10 iterations
  print(next(fib_gen), end="\t") # <-- Can generate the next number infintely

#Passing Arguments to generators
names = ["ferrari", "john", "barbie", "cottonwood", "shirley"]
labels = ["car", "boy", "toy", "tree", "girl"]

def combine(data_a, data_b):
  for a, b in zip(data_a, data_b):
    yield f"{a.capitalize()} is a {b}"
    
cogen = combine(names, labels) # pass arguments to combine

for value in cogen: # for loop will iterate until end of data
  print(value)

#More About Decorators

# Modify encrypt decorator to accept argument strength
# Add it to ord(c)

def encrypt(strength=0):
  def outer_wrapper(function):
    def wrapper(*args, **kwargs):
      message = function(*args, **kwargs)
      return [strength + ord(c) for c in message]
    return wrapper
  return outer_wrapper

@encrypt(strength=3)
def send_message(message):
  return message

message = send_message("Hello Officers. This is your captain speaking.")

print(message)

#Bitwise Operators

print(bin(67))

print(5, "\t = " , bin(5))
print(4, "\t = " , bin(4))
print(~4, "\t = " , bin(~4))
print(4 & 5, "\t = " , bin(4 & 5))
print(4 | 5, "\t = " , bin(4 | 5))
print(4 ^ 5, "\t = " , bin(4 ^ 5))
print(8, "\t =", bin(8))
print(8 << 1, "\t =", bin(8 << 1))
print(8, "\t =", bin(8))
print(8 >> 2, "\t =", bin(8 >> 2))

# Find if a number is even or odd using & operator
nums = [45, 21, 34, 64, 4, 97, 24]

for num in nums:
  if num & 1: # <-- add condition here
    print(f"{num} is odd")
  else:
    print(f"{num} is even")

# Modify an even number by adding 1 and making it odd
nums = [45, 21, 34, 64, 4, 97, 24]

for num in nums:
  result = num | 1
  print(f"{num} is now {result}")

# Find the unique number from the list

nums = [34, 3, 64, 33, 22, 574, 74, 6, 3, 2, 574, 43, 33, 789, 6, 64, 43, 22, 789, 34, 2]
result = 0
for num in nums:
  result ^= num
  # add solution here

print(result)

# Find the number of 1 bits in n

n = 355
result = 0
print(bin(n))

while n:
  result += (n & 1) # get the last bit and add it to result
  n >>= 1 # shift to the right

print(result)
