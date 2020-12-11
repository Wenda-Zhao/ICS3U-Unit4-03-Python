#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Dec 2020
# This program is for for loop


def main():
    # this function is for loop
    basic_number = -1

    # input
    positive_number = input("Enter a non-negative number: ")
    print("")

    # process & output
    try:
        positive_number_int = int(positive_number)
        print("It is a integer")
        if positive_number_int >= 0:
            for loop_number in range(positive_number_int + 1):
                basic_number = basic_number + 1
                square_number = basic_number ** 2
                print("{0}² = {1}".format(loop_number, square_number))
        else:
            print("It is not a non-negative number")
    except Exception:
        print("It is not a integer")
    finally:
        print("Done!")


if __name__ == "__main__":
    main()
