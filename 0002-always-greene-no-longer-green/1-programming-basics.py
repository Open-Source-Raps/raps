#!/usr/bin/python3

# Anything after the # is a "comment".  It's just a note to ourselves and doesn't actually do anything.
# We'll use these to give notes along with the programs below...



# Variables?!  Oh, no!~

x = 5

y = 6

z = -1

x + y

a = x + y - z

print(a)

print('Oh, this is easy!')

print('Oh, wait, there\'s more?!')									# note the "escaped" character otherwise it's a bug!

string_variable = str('A string is just a list of characters.')						# A "string of characters"
int_variable = int(5)  											# Whole Numbers
other_int_variable = int(y)										# You can use variables here too!
float_variable = float(-1.234) 										# A "float" is a floating point number
bool_variable = True											# Boolean variables are special. We'll cover them soon.
char_variable = 'a'											# A single character.  

type(string_variable)
type(int_variable)
type(float_variable)
type(bool_variable)
type(char_variable)											# This is a string in Python, but can be a special type in other languages.


import math
math.sin(a)												# a is the input, the output is -0.5365729180004349

math.tan(z)												# Tangent.
math.sqrt(49)												# Square root.

def my_function(thing):
  return thing + 1

a = my_function(x)
b = my_function(y)
print(a)
print(b)
print("Any string can go here" + " and even 'added' (or concatenated) to another one.")  		# We've already been doing output so far...

print('Enter your favorite number:')
favorite_number = input()
print('You entered: ' + favorite_number)
favorite_number_incremented = int(favorite_number) + 1							# python is smart enough to see we're trying to add a number and a string and will error if we don't "cast" one to the other
print('This number is bigger: ' + str(favorite_number_incremented))					# and now we have to cast it back



x = 0
if x > 0:
  print('Greater than 0.')

if x == 0:
  print('Equal to 0.')

if x < 0:
  print('Less than 0.')

# we can combine these into one logical block

if x > 0:
  print('Greater than 0.')
elif x == 0:
  print('Equal to 0.')
else:
  print('Less than 0.')

y = 1
if x == 0 and y == 2:
  print('This will not work.')
elif x == 0 and y == 1:
  print('This will work.')

if x == 0 or y == 2:
  print('This will also work.')


# Both of these loops print the numbers from 0

for x in range(5):	# range() is a yielding function (one that keeps track of its responses and enumerates appropriately) that will return the values 0, 1, 2, 3, and 4 respectively.
  print(x)

x = 0
while x <= 4:
  print(x)
