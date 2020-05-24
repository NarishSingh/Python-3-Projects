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


def prime_list(num):
    """
    Test for primes up to the argument and print them
    :param num: int - positive integer above 1
    """
    for i in range(2, num + 1):
        if is_prime(i):
            print(i, end=', ')

    print()


def main():
    print("===Prime Number Test===")
    print("1 | Calculate for a Prime")
    print("2 | Print all Primes")
    menu = int(input("Action: "))

    if menu == 1:
        calculating = True
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
    elif menu == 2:
        listing = True

        while listing:
            test_to = int(input("Enter a integer (0 or 1 to exit): "))

            if test_to == 0 or test_to == 1 or test_to < 0:
                print("No primes in range")
                listing = False
            else:
                print(prime_list(test_to))
    else:
        print("Unknown command...")


main()
