# Function to check leap year
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Days in each month
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Take user input
date_input = input("Enter date (DD/MM/YYYY): ")
day, month, year = map(int, date_input.split("/"))

# Validate the date
if month < 1 or month > 12 or day < 1 or day> 31:
  print("Invalid")
  exit()

# Adjust February days if leap year
if is_leap(year):
    month_days[1] = 29

if day > month_days[month - 1]:  # Check valid day for the given month
    print("Invalid")
    exit()

# 1st Jan 1900 was Monday (Reference Date)
base_year = 1900
days_count = 0

# Count days from 1900 to the given year
for y in range(base_year, year):
    days_count += 366 if is_leap(y) else 365

# Count days from Jan 1 of given year to given date
for m in range(month - 1):
    days_count += month_days[m]

days_count += day - 1  # Add days of the current month

# Find the weekday (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(weekdays[days_count % 7])
