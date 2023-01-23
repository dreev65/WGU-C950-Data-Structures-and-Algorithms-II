# Daniel Reeve    Student ID: 001990892

import datetime
from package_import import myHash
from truck_deliveries import runDelivery, getTotalDistance

runDelivery()

if __name__ == '__main__':

    print("\n")
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

        # TODO: fill in the remaining interface items (remaining need to search by time for each status)
        elif option == "2":
            search_input = int(input('\nEnter the package number: '))
            time_input = input('Enter a time in the format of HH:MM:SS: ')
            (hrs, mins, secs) = time_input.split(":")
            time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

            package = myHash.lookup(search_input)
            timestamp = package.timestamp

            if time < timestamp:
                print('')
                print('Package:', package.ID)
                print('Address:', package.address)
                print('City:', package.city)
                print('State:', package.state)
                print('Zipcode:', package.zipcode)
                print('Deadline:', package.deadline)
                print('Weight:', package.weight)
                print('Status:', 'en route')
                print('Timestamp:', 'None')
            else:
                print('')
                print('Package:', package.ID)
                print('Address:', package.address)
                print('City:', package.city)
                print('State:', package.state)
                print('Zipcode:', package.zipcode)
                print('Deadline:', package.deadline)
                print('Weight:', package.weight)
                print('Status:', package.status)
                print('Timestamp:', package.timestamp)

        elif option == "3":
            continue
        elif option == "4":
            isExit = False
        else:
            print("Incorrect input, please try again!")



