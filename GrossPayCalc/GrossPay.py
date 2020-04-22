# Author: Narish Singh
# Date Created: 4/19
# Last Modified: 4/19
import sys

workHrMax = 40
try:
    hr = float(input("Enter hours worked this week: "))
except ValueError:
    print("Not a numerical value.")
    sys.exit()

try:
    hrPay = round(float(input("Enter hourly pay rate: $")), 2)
except ValueError:
    print("Not a numerical value.")
    sys.exit()

if hr > 40:
    overtime = hr - 40
    otPay = round((1.5 * hrPay), 2)

    normalEarn = round((workHrMax * hrPay), 2)
    otEarn = round((overtime * otPay), 2)
    grossPay = normalEarn + otEarn
else:
    grossPay = round((hr * hrPay), 2)

print("Gross pay = $", grossPay)
