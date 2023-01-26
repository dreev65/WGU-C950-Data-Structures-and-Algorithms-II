# Daniel Reeve    Student ID: 001990892

from interface import userSearch
from truck_deliveries import runDelivery

runDelivery()

if __name__ == '__main__':
    print("")
    print("---------------------")
    print("WGUPS ROUTING PROGRAM")
    print("---------------------")

    # Creates the interface that the user sees when they run the program. Option one displays all the packages at
    # their delivered status and the total mileage traveled. Option 2 calls userSearch(2), allows the user to search
    # for one package at any time. Option 3 calls userSearch(2), allows the user to search
    # for all packages at any time. Option 4 ends the program.
    isExit = True
    while isExit:
        print("\nOptions:")
        print("1. Print All Package Status and Total Mileage")
        print("2. Get a Single Package Status with a Time")
        print("3. Get All Package Status with a Time")
        print("4. Exit the Program")
        option = input("\nChose an option (1,2,3 or 4): ")

        if option == "1":
            userSearch(1)
        elif option == "2":
            userSearch(2)
        elif option == "3":
            userSearch(3)
        elif option == "4":
            isExit = False
        else:
            print("Incorrect input, please try again!")
