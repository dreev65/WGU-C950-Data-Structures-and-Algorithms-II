import datetime
from package_import import myHash
from truck_deliveries import run_two_start, first_truck_time, second_truck_time, getTotalDistance


# creates the interface options for the user
# Space-Time Complexity -> O(n)
def userSearch(user_option):
    # Option 1 in the main.py interface.
    if user_option == 1:
        # Iterates through every package in the hash table and prints it
        for i in range(1, 41):
            package = myHash.lookup(i)
            print("Package ID:", package.ID, "|", "Address:", package.address, "|", "City:", package.city, "|",
                  "State:", package.state, "|", "Zip:", package.zipcode, "|", "Deadline:", package.deadline, "|",
                  "Weight:", package.weight, "|", "Status:", package.status, "|", "Timestamp:", package.timestamp)
        total = getTotalDistance(1) + getTotalDistance(2)  # gets the total distance traveled
        print("\nTotal Distance Traveled:", round(total, 2), "miles")  # prints the total distance

    # Option 2 in the main.py interface. Gets the time and package number input from user and searches the package
    # status at that time.
    # Space-Time Complexity -> O(1)
    elif user_option == 2:
        search_input = int(input('\nEnter the package number: '))  # get user package entry
        time_input = input('Enter a time in the format of HH:MM:SS: ')  # get user time entry

        # convert user time to datetime
        (hrs, mins, secs) = time_input.split(":")
        user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

        # package lists in the same order they were loaded
        truck_one = [1, 5, 7, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
        truck_two = [2, 3, 4, 6, 8, 10, 11, 12, 17, 18, 22, 24, 25, 36, 38]
        truck_one_rt = [9, 21, 23, 26, 27, 28, 32, 33, 35, 39]

        # looks up the package the user is searching for
        package = myHash.lookup(search_input)
        ID = package.ID
        timestamp = package.timestamp

        # determines the load time of the truck the package is on
        load_time = datetime.timedelta()
        if ID in truck_one:
            load_time = first_truck_time[0]
        elif ID in truck_two:
            load_time = second_truck_time[0]
        elif ID in truck_one_rt:
            load_time = run_two_start[0]

        # checks if the user time is before the load time of the package
        if user_time < load_time:
            print('')
            print('Package:', package.ID)
            print('Address:', package.address)
            print('City:', package.city)
            print('State:', package.state)
            print('Zipcode:', package.zipcode)
            print('Deadline:', package.deadline)
            print('Weight:', package.weight)
            print('Status:', 'at hub')
            print('Loading Time:', 'None')
        # checks if the user time is after or equal to the load time and before the delivery timestamp
        elif load_time <= user_time < timestamp:
            print('')
            print('Package:', package.ID)
            print('Address:', package.address)
            print('City:', package.city)
            print('State:', package.state)
            print('Zipcode:', package.zipcode)
            print('Deadline:', package.deadline)
            print('Weight:', package.weight)
            print('Status:', 'en route')
            print('Loading Time:', load_time)
        # checks if the user time is after or equal to the delivery timestamp
        elif user_time >= timestamp:
            print('')
            print('Package:', package.ID)
            print('Address:', package.address)
            print('City:', package.city)
            print('State:', package.state)
            print('Zipcode:', package.zipcode)
            print('Deadline:', package.deadline)
            print('Weight:', package.weight)
            print('Status:', package.status)
            print('Delivery Timestamp:', package.timestamp)

    # Option 3 in the main.py interface. Gets the time input from user and searches for each package status at that
    # time.
    elif user_option == 3:
        time_input = input('\nEnter a time in the format of HH:MM:SS: ')  # get user time entry

        # convert user time to datetime
        (hrs, mins, secs) = time_input.split(":")
        user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

        # package lists in the same order they were loaded
        truck_one = [1, 5, 7, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
        truck_two = [2, 3, 4, 6, 8, 10, 11, 12, 17, 18, 22, 24, 25, 36, 38]
        truck_one_rt = [9, 21, 23, 26, 27, 28, 32, 33, 35, 39]

        # iterates through for each package in the hash table. Gets the package delivery timestamp and compares the
        # user time to both the load time and delivery timestamp to determine the status of the package
        # Space-Time Complexity -> O(n)
        for i in range(1, 41):
            index = i
            package = myHash.lookup(index)
            ID = package.ID
            timestamp = package.timestamp

            # determines the load time of the truck the package is on
            load_time = datetime.timedelta()
            if ID in truck_one:
                load_time = first_truck_time[0]
            elif ID in truck_two:
                load_time = second_truck_time[0]
            elif ID in truck_one_rt:
                load_time = run_two_start[0]

            # checks if the user time is before the load time of the package
            if user_time < load_time:
                print("Package ID:", package.ID, "|", "Address:", package.address, "|", "City:", package.city, "|",
                      "State:", package.state, "|", "Zip:", package.zipcode, "|", "Deadline:", package.deadline, "|",
                      "Weight:", package.weight, "|", "Status:", "at hub", "|", "Timestamp:", "None")
            # checks if the user time is after or equal to the load time and before the delivery timestamp
            elif load_time <= user_time < timestamp:
                print("Package ID:", package.ID, "|", "Address:", package.address, "|", "City:", package.city, "|",
                      "State:", package.state, "|", "Zip:", package.zipcode, "|", "Deadline:", package.deadline, "|",
                      "Weight:", package.weight, "|", "Status:", "en route", "|", "Timestamp:", load_time)
            # checks if the user time is after or equal to the delivery timestamp
            elif user_time >= timestamp:
                print("Package ID:", package.ID, "|", "Address:", package.address, "|", "City:", package.city, "|",
                      "State:", package.state, "|", "Zip:", package.zipcode, "|", "Deadline:", package.deadline, "|",
                      "Weight:", package.weight, "|", "Status:", package.status, "|", "Timestamp:", package.timestamp)
