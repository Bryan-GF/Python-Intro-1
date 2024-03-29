"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime as dt
import datetime

def calendarSystem():
  tcalendar = calendar.TextCalendar(firstweekday=0)
  today = datetime.date.today()
  if len(sys.argv) == 1:
    tcalendar.prmonth(today.year, today.month)
    ##print the calendar for the current month  (NO INPUT)
  elif len(sys.argv) == 2:
    month = sys.argv[1]
    print(today.year)
    tcalendar.prmonth(int(today.year), int(month))
    ##assume argument is month, render calendar for that month of the current year (1 INPUT)
  elif len(sys.argv) == 3:
    month = sys.argv[1]
    year = sys.argv[2]
    tcalendar.prmonth(int(year), int(month))
    ##Render calendar for that month and year (2 INPUT)
  else:
    print('In order to render calendar please execute through the following format: "cal.py month [year]"')

calendarSystem();