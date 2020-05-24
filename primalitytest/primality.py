# Primality Test
# Date Created: 5/22/20
# Last Modified: 5/23/20

import math


def is_prime(num):
    """
    check for primality between 2 and square root of number
    :param num: int - a positive integer above 1
    :return: boolean - True if number is prime, False otherwise
    """
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def main():
    calculating = True

    print("===Prime Number Test===")

    while calculating:
        num = int(input("Enter a integer (0 or 1 to exit): "))

        if num == 0 or num == 1:
            calculating = False
        elif num < 0:
            print("Cannot solve for a negative number")
        elif is_prime(num):
            print(num, "is a prime number!")
        else:
            print(num, "is not a prime number...")


main()
