# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


# def greet():
#   print("Hello Coder")
#   print("How are you?")
#   print("How is the weather today?")
# greet()
#########################################################
# function that allows for input
# Name = input("What's your name?")
# def greetName(name):
#   print("Hello " + name, end = ".\n")
#   print("How are you?")
#   print("How is the weather today?")

# greetName(Name)



#########################################################
# Function with more than one input
Name = input("Hi, What's your name?")
Age = input("How old are you?")
def greetNameAge(name, age):
  print(f"Hello {name}, you are {age} years old.")

greetNameAge(Name, Age)
greetNameAge(name = "Obada", age = "26")


##########################################################
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# Write your code below this line 👇
import math
def paint_calc(height, width, cover):
  print(f"You'll need " + str(math.ceil((height * width)/cover)) + " cans of paint.")

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


###########################################################
# Prime number checker
# Write your code below this line 👇

def prime_checker(number):
  prime = True
  for x in range(2, number):
    if number % x == 0:
      prime = False
  if prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")        


# Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)