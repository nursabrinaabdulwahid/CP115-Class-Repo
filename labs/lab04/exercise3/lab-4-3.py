hours = int(input())
if hours == 2:
    charges = 0
else:
    if hours <= 5:
        charges = 2
if charge <= 30:
    parkingFee = charge * hours
else:
    parkingFee = 30 * hours
print(parkingFee)
