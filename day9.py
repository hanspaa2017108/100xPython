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