# Write a program to prompt the user for hours and rate per hour to compute gross pay.
# give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# use try and except so that your program handles non-numeric input gracefully.

workHrMax = 40
try:
    hr = float(input("Enter hours worked this week: "))
except ValueError:
    print("Please enter a numerical value.")

try:
    hrPay = round(float(input("Enter hourly pay rate: $")), 2)
except ValueError:
    print("Please enter a numerical value.")

if hr > 40:
    overtime = hr - 40
    otPay = round((1.5 * hrPay), 2)

    normalEarn = round((workHrMax * hrPay), 2)
    otEarn = round((overtime * otPay), 2)
    grossPay = normalEarn + otEarn
else:
    grossPay = round((hr * hrPay), 2)

print("Gross pay = $", grossPay)
