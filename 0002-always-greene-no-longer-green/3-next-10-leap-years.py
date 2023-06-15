#!/usr/bin/python3

from datetime import date

# Get current year
current_year = date.today().year

# Initialize count and year variables
count = 0
year = current_year

# Loop until we find 10 leap years
while count < 10:
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    # If the year is a leap year, print it and increment the count
    print(year)
    count += 1

  # Increment the year
  year += 1
