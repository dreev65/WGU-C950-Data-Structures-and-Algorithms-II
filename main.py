# Daniel Reeve    Student ID: 001990892

from interface import userSearch
from package_import import myHash
from truck_deliveries import runDelivery, getTotalDistance

runDelivery()

if __name__ == '__main__':
    print("")
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
        option = input("\nChose an option (1,2,3 or 4): ")

        if option == "1":
            for i in range(1, 41):
                package = myHash.lookup(i)
                print("Package ID:", package.ID, "|", "Address:", package.address, "|", "City:", package.city, "|",
                      "State:", package.state, "|", "Zip:", package.zipcode, "|", "Deadline:", package.deadline, "|",
                      "Weight:", package.weight, "|", "Status:", package.status, "|", "Timestamp:", package.timestamp)
            total = getTotalDistance(1) + getTotalDistance(2)
            print("\nTotal Distance Traveled:", round(total, 2), "miles")

        elif option == "2":
            userSearch(2)
        elif option == "3":
            userSearch(3)
        elif option == "4":
            isExit = False
        else:
            print("Incorrect input, please try again!")
