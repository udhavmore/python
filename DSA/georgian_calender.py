"""
Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.


Test Data
Sample input: 2000

Expected output: Leap year

Sample input: 2015

Expected output: Common year

Sample input: 1999

Expected output: Common year

Sample input: 1996

Expected output: Leap year

Sample input: 1580

Expected output: Not within the Gregorian calendar period
"""


year = int(input("Enter a year: "))

#
# Write your code here.
#	
if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else:
    print("Leap year")