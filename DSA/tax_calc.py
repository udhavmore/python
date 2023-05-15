"""
Once upon a time there was a land - a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course - their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.

Note: this happy country never returns money to its citizens. If the calculated tax is less than zero, it only means no tax at all (the tax is equal to zero). Take this into consideration during your calculations.



Sample input: 10000

Expected output: The tax is: 1244.0 thalers

Sample input: 100000

Expected output: The tax is: 19470.0 thalers

Sample input: 1000

Expected output: The tax is: 0.0 thalers

"""


income = float(input("Enter the annual income: "))

#
# Write your code here.
#
amt = 85528

if income < 0:
    tax = 0.0
elif income < amt:
    tax = (income * (18/100)) - 556.2
    print(tax)
else: 
    surplus = income - amt
    tax = 14839.2 + ((32/100)*surplus)
    print(tax)


tax = round(tax, 0)
print("The tax is:", tax, "thalers")
