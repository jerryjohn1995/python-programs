# Program to display calendar

# importing calendar module
import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

# display the calendar
print(calendar.month(year, month))
