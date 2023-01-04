# Daniel Reeve    Student ID: 001990892

from address_import import getAddressData
from package_import import getPackageData

if __name__ == '__main__':

    print("---------------------")
    print("WGUPS ROUTING PROGRAM")
    print("---------------------")

    # loop until user is satisfied
    isExit = True
    while isExit:
        print("\nOptions:")
        print("1. Print All Package Status and Total Mileage")
        print("2. Get a Single Package Status with a Time")
        print("3. Get All Package Status with a Time")
        print("4. Exit the Program")
        option = input("Chose an option (1,2,3 or 4): ")

        # TODO: fill in the remaining options
        if option == "1":
            getPackageData()
        elif option == "2":
            # search_input = int(input('Enter the package number: '))
            # ChainingHashTable.search(search_input)

            getAddressData()

        # elif option == "3":
            # getDistanceData()

        elif option == "4":
            isExit = False
        else:
            print("Wrong option, please try again!")
