# Time conversion program for min or sec
# Author: Narish Singh
# Date Created: 4/21/20
# Last Modified: 5/13/20

import sys

SEC_PER_MIN = 60
SEC_PER_HR = 60 * SEC_PER_MIN
MIN_PER_HR = 60

print("We will convert your raw input into hours, minutes, and seconds.")
print("Enter the number corresponding to the unit of time you would like converted: ")
print("1 - Seconds")
print("2 - Minutes")
userChoice = int(input())

if userChoice == 1:  # sec
    try:
        sec = int(input("Enter number of seconds: "))
    except ValueError:
        print("Not a numerical value.")
        sys.exit()

    hr = sec // SEC_PER_HR
    sec = sec % SEC_PER_HR
    mins = sec // SEC_PER_MIN
    sec = sec % SEC_PER_MIN

    print(hr, end='')
    if hr == 1:
        print(" hour ", end='')
    else:
        print(" hours ", end='')

    print(mins, end='')
    if mins == 1:
        print(" minute ", end='')
    else:
        print(" minutes ", end='')

    print(sec, end='')
    if sec == 1:
        print(" second")
    else:
        print(" seconds")
else:  # min
    try:
        mins = int(input("Enter number of minutes: "))
    except ValueError:
        print("Not a numerical value.")
        sys.exit()

    sec = mins * 60
    hr = mins // MIN_PER_HR
    mins = mins % MIN_PER_HR

    print(hr, end='')
    if hr == 1:
        print(" hour ", end='')
    else:
        print(" hours ", end='')

    print(mins, end='')
    if mins == 1:
        print(" minute ")
    else:
        print(" minutes ")

    print(sec, "total seconds")
