# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.
Coffee_Price = 3.50
Coffee_Qty = int(input("Enter the quantity of the coffee:"))
Muffin_Price = 2.10
Muffin_Qty = int(input("Enter the quantity of the muffin:"))
Water_Price = 1.05
Water_Qty = int(input("Enter the quantity of the water:"))
Total = (Coffee_Price * Coffee_Qty) + (Muffin_Price * Muffin_Qty) + (Water_Price * Water_Qty)
Receipt = "========== RECEIPT ==========\nItem\tPrice\tQty\tTotal\nCoffee\t$3.50\t" + str(Coffee_Qty) + "\t$" + f"{Coffee_Price * Coffee_Qty:.2f}" + "\nMuffin\t$2.10\t" + str(Muffin_Qty) + "\t$" + f"{Muffin_Price * Muffin_Qty:.2f}" + "\nWater\t$"