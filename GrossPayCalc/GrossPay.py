# Author: Narish Singh
# Date Created: 4/19
# Last Modified: 5/13
import sys

WORK_HR_MAX = 40
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

    normalEarn = round((WORK_HR_MAX * hrPay), 2)
    otEarn = round((overtime * otPay), 2)
    grossPay = normalEarn + otEarn
else:
    grossPay = round((hr * hrPay), 2)

print("Gross pay = $", grossPay)
