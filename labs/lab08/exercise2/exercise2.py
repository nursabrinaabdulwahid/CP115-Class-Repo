employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()
overtime_pay = 35*overtime_hours
gross_salary = base_salary + overtime_pay

if (tax_status == Single):
    if(gross_salary >= 5000):
    tax_rate = 0.22

    else:
    tax_rate = 0.18

if (gross_salary >= 6000):
    tax_status = "Married"
    tax_rate = 0.20
else:
    tax_rate = 0.15

if (gross_salary >= 5500):
    tax_status = "Head"
    tax_rate = 0.25
else:
    tax_rate = 0.19

net_salary = gross_salary - (gross_salary * tax_rate) - (11/100 * gross_salary) - (0.5/100 * gross_salary)

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
