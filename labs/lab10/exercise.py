# programmer's name : Nur Sabrina Rabiatul Adawiyah Binti Abdul Wahid
# problem description : a Python program that asks the user to enter the
# monthly usage and then calculates and displays the amount of the bill to be paid
# after receiving the discount.

monthly_usage = float (input("Enter your monthly usage: "))

if monthly_usage <= 50:
    amount = monthly_usage - (monthly_usage * 0.0)
    print (amount)
elif monthly_usage <= 100:
    amount = monthly_usage - (monthly_usage * 0.05)
    print (amount)
else:
    amount = monthly_usage - (monthly_usage * 0.2)
    print (amount)

