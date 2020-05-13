# Author: Narish Singh
# Date Created: 5/13/20
# Last Modified: 5/13/20

import sys


def displayUnitList():
    print("===Customary===")
    print("1 | Inch")
    print("2 | Foot")
    print("3 | Yard")
    print("4 | Mile")
    print("5 | Nautical Mi")
    print("===Metric===")
    print("6 | Millimeter")
    print("7 | Centimeter")
    print("8 | Meter")
    print("9 | Kilometer")


def getUserMenuChoice():
    menuInput = 0

    while menuInput < 1 or menuInput > 9:
        try:
            menuInput = int(input("Convert from: "))
        except ValueError:
            print("Not a numerical input")
            sys.exit()

    return menuInput


# convert all to ft or m
# def inToFt(in):
#     return in/12
#
# def

def convert(fromUnit, toUnit):


# fill in conversions


def main():
    print("Welcome to the distance converter")

    print("Please select the starting unit: ")
    displayUnitList()
    startingUnit = getUserMenuChoice()

    print("Select unit to convert to")
    displayUnitList()
    endingUnit = getUserMenuChoice()

    print(convert(startingUnit, endingUnit))
