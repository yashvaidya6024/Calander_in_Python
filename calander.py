#Creating and working with calendar in python
"""Python has a built-in module called 'calendar' that allows you to work with calendars and perform various operations related to dates and times. Here's how you can use the calendar module in Python:"""

import calendar

# Displaying a calendar for a specific month and year
Month = calendar.month(2026, 4)
print(Month)
print(calendar.month(2026, 4, w = 3, l = 1))

# Displaying a calendar for an entire year
print(calendar.calendar(2026))

# Leap year check
print(calendar.isleap(2024))  # True, because 2024 is a leap year
print(calendar.isleap(2023))  # False, because 2023 is not a leap year
print(calendar.isleap(2020))  # True, because 2020 is a leap year
print(calendar.isleap(1900))  # False, because 1900 is not a leap year
print(calendar.isleap(2000))  # True, because 2000 is a leap year

# Other useful functions

day_num = calendar.weekday(2026, 1, 4)  # Get the weekday of April 1, 2026
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"January 4, 2026 is a {days[day_num]}")

# Text calendar and HTML calendar
cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatmonth(2026, 12))

html_cal = calendar.HTMLCalendar(calendar.MONDAY)
print(html_cal.formatmonth(2026, 1))