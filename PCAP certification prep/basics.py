# name = input("Enter Your Name:\n")
# print(len(name))


# def bmi():
#     weight = float(input("Enter your Weight(KG): "))
#     height = float(input("Enter your Height(M): "))
#     user_bmi = weight / height ** 2
#     if int(user_bmi) < int(18.5):
#         return str(user_bmi) + "\nUnder Weight"
#     elif int(user_bmi) in range(int(18.5), 25):
#         return str(user_bmi) + "\nNormal Weight"
#     elif int(user_bmi) in range(25, 30):
#         return str(user_bmi) + "\nOverweight"
#     else:
#         return str(user_bmi) + "\nObese"
#
#
# while True:
#     print(bmi())

#
# till_age = 90
# curr_age = 22
#
# left_years = till_age-curr_age
#
# days_left = left_years * 365
# print(f"days left to 90: {days_left}")
#
# months_till_last = left_years * 12
# print(f"Months left to 90: {months_till_last}")
#
# weeks_till_last = months_till_last * 7
# print(f"weeks left to 90: {left_years}")

# bill = float(input("Total Bill:"))
# tip = int(input("Tip Percent(10,15,20):"))/100
# split = int(input("Number of People:"))
# tip = bill * tip
# bill_with_tip = bill + tip
# each_share = bill_with_tip/split
# print(f"Total Share: {each_share}")


# num = int(input("enter number: "))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# leap year or not
# """
# 1. if year is cleanly (no remainder) divisble by 4 go to next
# 2. if year is NOT cleanly divisble by 100 -> Leap Year || if YES go to next
# 3. if year is cleanly (no remainder) divisible by 400 -> Leap Year
# """
# while True:
#     year = int(input("Enter Year: "))
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print("Leap Year 400")
#             else:
#                 print("Not Leap Year 400")
#         else:
#             print("Leap Year 100")
#     else:
#         print("Not Leap Year")

import random

n = random.random()