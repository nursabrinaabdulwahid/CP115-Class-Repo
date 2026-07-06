kwh = int(input())
if kwh == 100:
    charge = 0.3
else:
    if kwh > 100:
        charge = 0.5
    else:
        if kwh > 200:
            charge = 0.75
totalBill = kwh * charge
print(totalBill)
