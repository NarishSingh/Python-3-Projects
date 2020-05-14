# Author: Narish Singh
# Date Created: 5/13/20
# Last Modified: 5/13/20
import math
import sys


def get_menu_choice():
    """
    Print menu and get user shape selection
    :return: {int} 1-4 corresponding with a shape type
    """
    print("1 | Right Triangle")
    print("2 | Square")
    print("3 | Rectangle")
    print("4 | Circle")

    menu_choice = 0

    while menu_choice < 1 or menu_choice > 4:
        menu_choice = int(input("Please select shape: "))

    return menu_choice


def right_tri_area(b, h):
    """
    area calculation of right triangle
    :param b: {float} base
    :param h: {float} height
    :return: area of right triangle
    """
    return .5 * (b * h)


def right_tri_hypotenuse(b, h):
    """
    calculate the hypotenuse of right triangle
    :param b: {float} base
    :param h: {float} height
    :return: {float} hypotenuse/the longest side of right triangle
    """
    return math.sqrt(b ** 2 + h ** 2)


def right_tri_perimeter(b, h):
    """
    find the hypotenuse then calculate perimeter
    :param b: {float} base
    :param h: {float} height
    :return: {float} perimeter of a right triangle
    """
    c = right_tri_hypotenuse(b, h)

    return b + h + c


def square_area(s):
    """
    area calculation of square
    :param s: {float} side
    :return: area of square
    """
    return s ** 2


def square_perimeter(s):
    """
    perimeter calculation of square
    :param s: {float} side
    :return: perimeter of square
    """
    return 4 * s


def rect_area(l, w):
    """
    area calculation of rectangle
    :param l: {float} length
    :param w: {float} width
    :return: {float} area of rectangle
    """
    return l * w


def rect_perimeter(l, w):
    """
    perimeter calculation of rectangle
    :param l: {float} length
    :param w: {float} width
    :return: {float} perimeter of rectangle
    """
    return (2 * l) + (2 * w)


def circle_area(r):
    """
    area calculation of circle
    :param r: {float} radius
    :return: {float} area of circle
    """
    return math.pi * (r ** 2)


def circle_perimeter(r):
    """
    perimeter calculation of circle
    :param r: {float} radius
    :return: {float} perimeter of circle
    """
    return 2 * math.pi * r


def shape_calculations(shape_choice):
    """
    Get user inputs for key sides in shape, then calculate and print area, perimeter, and another unique calculation for
     shape
    :param shape_choice: {int} 1-4 corresponding to shape
    :return: {void}
    """
    if shape_choice == 1:
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))

        print("Hypotenuse = ", right_tri_hypotenuse(b, h))
        print("Area = ", right_tri_area(b, h))
        print("Perimeter = ", right_tri_perimeter(b, h))
    elif shape_choice == 2:
        s = float(input("Enter side: "))

        print("Diagonal = ", right_tri_hypotenuse(s, s))
        print("Area = ", square_area(s))
        print("Perimeter = ", square_perimeter(s))
    elif shape_choice == 3:
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))

        print("Diagonal = ", right_tri_hypotenuse(l, w))
        print("Area = ", rect_area(l, w))
        print("Perimeter = ", rect_perimeter(l, w))
    elif shape_choice == 4:
        r = float(input("Enter radius: "))

        print("Diameter = ", (2 * r))
        print("Area = ", circle_area(r))
        print("Perimeter = ", circle_perimeter(r))
    else:
        print("Unknown command")
        sys.exit()


def main():
    """
    App controller
    :return: {void}
    """
    print("Welcome to the shape calculator, we will calculate areas and perimeters for you")
    shape = get_menu_choice()
    shape_calculations(shape)


main()
