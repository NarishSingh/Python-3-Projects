# Author: Narish Singh
# Date Created: 5/13/20
# Last Modified: 5/13/20

import sys


def display_unit_list():
    """
    Display unit list for the menu
    :return: {void}
    """
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


def get_user_menu_choice():
    """
    get user input for menu, constrains input using while loop
    :return: {int} 1-8 for the desired unit of measure throws ValueError exception if not number
    """
    menu_input = 0

    while menu_input < 1 or menu_input > 8:
        try:
            menu_input = int(input("Unit: "))
        except ValueError:
            print("Not a numerical input")
            sys.exit()

    return menu_input


def menu_choice_as_string(menu_input):
    """
    Convert numerical input for menu selection to String
    :param menu_input: {int} 1-8 corresponding to menu inputs, exits program otherwise
    :return:
    """
    if menu_input == 1:
        return "in"
    elif menu_input == 2:
        return "ft"
    elif menu_input == 3:
        return "yd"
    elif menu_input == 4:
        return "mi"
    elif menu_input == 5:
        return "mm"
    elif menu_input == 6:
        return "cm"
    elif menu_input == 7:
        return "m"
    elif menu_input == 8:
        return "km"
    else:
        print("Unknown command")
        sys.exit()


def process_distance(from_unit, distance):
    """
    Process starting measure into feet or meters based on whether it was originally customary or metric
    :param from_unit: {int} 1-8 corresponding to menu inputs, exits program otherwise
    :param distance: {float} distance to be processed
    :return:
    """
    if from_unit == 1:
        return distance / 12
    elif from_unit == 3:
        return distance * 3
    elif from_unit == 4:
        return distance * 5280
    elif from_unit == 5:
        return distance / 1000
    elif from_unit == 6:
        return distance / 100
    elif from_unit == 8:
        return distance * 1000
    else:
        print("Unknown command")
        sys.exit()


def convert_distance(to_unit, dist_in_ft, dist_in_m):
    """
    convert distance from feet or meters to another unit of measure
    :param to_unit: {int} 1-8 corresponding to menu inputs, exits program otherwise
    :param dist_in_ft: {float} user's distance in feet
    :param dist_in_m: {float} user's distance in meters
    :return: {float} distance converted from ft/m to intended unit of measure
    """
    if to_unit == 1:
        return dist_in_ft * 12
    elif to_unit == 2:
        return dist_in_ft
    elif to_unit == 3:
        return dist_in_ft / 3
    elif to_unit == 4:
        return dist_in_ft / 5280
    elif to_unit == 5:
        return dist_in_m * 1000
    elif to_unit == 6:
        return dist_in_m * 100
    elif to_unit == 7:
        return dist_in_m
    elif to_unit == 8:
        return dist_in_m / 1000
    else:
        print("Unknown command")
        sys.exit()


def conversion(from_unit, to_unit, distance):
    """
    controller for converting distance from one unit of measure to another
    :param from_unit: {int} 1-8 corresponding to menu inputs
    :param to_unit: {int} 1-8 corresponding to menu inputs
    :param distance: {float} distance to be processed
    :return: {float} distance converted to intended unit of measure
    """
    if from_unit == to_unit:
        print("No conversion to be done")
        sys.exit()
    elif from_unit == 1 or from_unit == 2 or from_unit == 3 or from_unit == 4:
        dist_in_ft = process_distance(from_unit, distance)
        dist_in_m = dist_in_ft / 3.28

        converted = convert_distance(to_unit, dist_in_ft, dist_in_m)
        return converted
    elif from_unit == 5 or from_unit == 6 or from_unit == 7 or from_unit == 8:
        dist_in_m = process_distance(from_unit, distance)
        dist_in_ft = dist_in_m * 3.28

        converted = convert_distance(to_unit, dist_in_ft, dist_in_m)
        return converted
    else:
        print("Unknown command")
        sys.exit()


def main():
    """
    app controller
    :return: {void}
    """
    print("Welcome to the distance converter")

    print("Please select the starting unit: ")
    display_unit_list()
    starting_unit = get_user_menu_choice()

    print("Select unit to convert to")
    ending_unit = get_user_menu_choice()

    try:
        dist = float(input("Please enter distance: "))
    except ValueError:
        print("Not a numerical input")
        sys.exit()

    start_unit_string = menu_choice_as_string(starting_unit)
    end_unit_string = menu_choice_as_string(ending_unit)
    converted_distance = conversion(starting_unit, ending_unit, dist)
    print(dist, start_unit_string, " = ", format(converted_distance, ',.4f'),
          end_unit_string)


main()
