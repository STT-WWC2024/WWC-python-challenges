# Create a program that checks if a year is a leap year.
import calendar

year = int(input("Enter a year\n"))
print(f"{year} was a leap year: {calendar.isleap(year)}")

# OR

year = int(input("Enter a year\n"))
leap = True if year %4 == 0 else False
print(f"{year} was a leap year: {leap}")