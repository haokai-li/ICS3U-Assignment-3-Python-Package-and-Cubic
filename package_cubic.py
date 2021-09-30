#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program calculate weight and volume of package


def main():
    # This function calculate weight and volume of package

    # input
    string_weight = input("Please enter weight of the package(kg): ")
    string_length = input("Please enter length of the package(cm): ")
    string_width = input("Please enter width of the package(cm): ")
    string_height = input("Please enter height of the package(cm): ")
    print("")

    # process
    try:
        number_weight = int(string_weight)
        number_length = int(string_length)
        number_width = int(string_width)
        number_height = int(string_height)

        cubic_volume = number_length * number_width * number_height

        if number_weight <= 27 or cubic_volume <= 10000:
            if number_weight <= 27:
                if cubic_volume <= 10000:
                    # output
                    print("OK, we will accept the package.")
                else:
                    # output
                    print("Your package is too large.")
            else:
                # output
                print("Your package is too heavy.")
        else:
            # output
            print("Your package is too heavy and too large.")
    except Exception:
        # output
        print("Your input is not a valid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
