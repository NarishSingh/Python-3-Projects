# Random Number Generator File IO
# Date Created: 6/12/20
# Last Modified: 6/12/20
import math
import random
import sys

NUMBER_FILE = "nums.txt"
DELIMITER = " "


def write_nums(num_limit, rand_min, rand_max):
    """
    write random numbers within range to file in rows of 10 digits
    :param num_limit: number of randoms to write
    :param rand_min: min of range for randomization
    :param rand_max: max of range for randomization
    """
    try:
        nums = open(NUMBER_FILE, "w")
    except IOError:
        print("Could not open number file")
        sys.exit()

    for i in range(0, (num_limit + 1)):
        nums.write(str(random.randint(rand_min, rand_max)) + DELIMITER)

    nums.close()


def average_of_file(num_limit):
    """
    read in the randoms from file and calculate the average
    :param num_limit: amount of numbers in file
    :return: the average of all the randoms
    """
    try:
        rands = open(NUMBER_FILE, "r")
    except IOError:
        print("Could not open number file")
        sys.exit()

    num_total = 0

    num_list = rands.readline().rstrip(DELIMITER).split(DELIMITER)

    rands.close()

    # print(num_list)  # debug

    for n in num_list:
        num_total += int(n)

    return num_total / num_limit


def main():
    print("Welcome to the random number generator")

    rn_limit = int(input("Enter the number of randoms you would like printed to file: "))
    lower_bound = int(input("Enter the lower bound of range for randoms: "))
    upper_bound = int(input("Enter the upper bound of range for randoms: "))
    while math.isnan(rn_limit) or math.isnan(lower_bound) or math.isnan(upper_bound):
        print("Invalid input")
        rn_limit = int(input("Enter the number of randoms you would like printed to file: "))
        lower_bound = int(input("Enter the lower bound of range for randoms: "))
        upper_bound = int(input("Enter the upper bound of range for randoms: "))

    write_nums(rn_limit, lower_bound, upper_bound)

    avg = average_of_file(rn_limit)
    print("The average from file is " + format(avg, '.2f'))


main()
