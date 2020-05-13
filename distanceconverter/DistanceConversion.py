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
    print("===Metric===")
    print("5 | Millimeter")
    print("6 | Centimeter")
    print("7 | Meter")
    print("8 | Kilometer")


def getUserMenuChoice():
    menuInput = 0

    while menuInput < 1 or menuInput > 8:
        try:
            menuInput = int(input("Convert from: "))
        except ValueError:
            print("Not a numerical input")
            sys.exit()

    return menuInput


# convert all to ft or m
def inToFt(inches):
    return inches / 12


def ydToFt(yd):
    return yd * 3


def miToFt(mi):
    return mi * 5280


def mmToM(mm):
    return mm / 1000


def cmToM(cm):
    return cm / 100


def kmToM(km):
    return km * 1000


def processDistance(fromUnit, distance):
    # process customary and metric measures
    if fromUnit == 1:
        return inToFt(distance)
    elif fromUnit == 3:
        return ydToFt(distance)
    elif fromUnit == 4:
        return miToFt(distance)
    elif fromUnit == 5:
        return mmToM(distance)
    elif fromUnit == 6:
        return cmToM(distance)
    elif fromUnit == 8:
        return kmToM(distance)


def convert(fromUnit, toUnit, distance):  # fill in conversions
    if fromUnit == toUnit
        print("No conversion to be done")
        sys.exit()
    elif fromUnit == 1 or fromUnit == 2 or fromUnit == 3 or fromUnit == 4:
        distInFt = processDistance(fromUnit, distance)
        distInM = distInFt / 3.28

        if toUnit == 1:
            return distInFt * 12
        elif toUnit == 2:
            return distInFt
        elif toUnit == 3:
            return distInFt / 3
        elif toUnit == 4:
            return distInFt / 5280
        elif toUnit == 5:
            return distInM * 1000
        elif toUnit == 6:
            return distInM * 100
        elif toUnit == 7:
            return distInM
        elif toUnit == 8:
            return distInM / 1000
    else:
        distInM = processDistance(fromUnit, distance)
        distInFt = distInM * 3.28

        # TODO finish conversions
        if toUnit == 1:
        elif toUnit == 2:
        elif toUnit == 3:
        elif toUnit == 4:
        elif toUnit == 5:
        elif toUnit == 6:
        elif toUnit == 7:
        elif toUnit == 8:


def main():
    print("Welcome to the distance converter")

    print("Please select the starting unit: ")
    displayUnitList()
    startingUnit = getUserMenuChoice()

    print("Select unit to convert to")
    displayUnitList()
    endingUnit = getUserMenuChoice()

    try:
        dist = int(input("Please enter distance: "))
    except ValueError:
        print("Not a numerical input")
        sys.exit()

    print(convert(startingUnit, endingUnit, dist))
