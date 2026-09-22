#!/usr/bin/env python4\
# Created By:Kamche
# Date: September 22, 2026
# This program ask the user for the length and width of
# a rectangle and calculates and displays the area and perimeter.
# back to the user with proper units.
def main():
    # get the length from the user and convert to an interger
    length = int(input("Enter the length of the rectangle (cm): "))

    # get the width from the user and convert to an integer
    width = int(input("Enter the width of the rectangle (cm): "))

    # calculate the area and perimeter of the rectangle
    area = length * width
    perimeter = 2 * (length + width)

    # display the area and perimeter to the user with proper units
    print("The area of the rectangle is: {} cm².".format(area))
    print("The perimeter of the rectangle is: {} cm.".format(perimeter))


if __name__ == "__main__":
    main()
