weight = float(input())
ticketPrice = float(input())
if weight == 0:
    finalPrice = ticketPrice - 10
else:
    if weight <= 15:
        pass
    else:
        exWeight = weight - 15 * 4
        finalPrice = ticketPrice + exWeight
print(finalPrice)
