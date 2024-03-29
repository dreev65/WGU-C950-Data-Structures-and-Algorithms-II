import datetime

from address_import import AddressDict
from distance_import import lookup_distance
from package_import import myHash


# Empty truck lists created
truck_one = []
truck_two = []

# Empty distance lists to store all the distances calculated from each start to the possible end addresses
first_truck_distances = {}
second_truck_distances = {}

# Empty distance lists that will hold the actual distances traveled for each truck
truck_one_min_dist = []
truck_two_min_dist = []

# Times the trucks leave the hub
first_truck_time = []
x = datetime.timedelta(hours=8)
first_truck_time.append(x)

second_truck_time = []
x = datetime.timedelta(hours=9.5)
second_truck_time.append(x)

# package lists
package_list_one = [1, 5, 7, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
package_list_two = [2, 3, 4, 6, 8, 10, 11, 12, 17, 18, 22, 24, 25, 36, 38]
package_list_three = [9, 21, 23, 26, 27, 28, 32, 33, 35, 39]


# Load trucks with packages and update status to 'en route'
def loadTrucks(run):
    if run == 1:
        for p in package_list_one:
            temp = myHash.lookup(p)
            temp.status = 'en route'
            truck_one.append(format(myHash.lookup(p)))

        for p in package_list_two:
            temp = myHash.lookup(p)
            temp.status = 'en route'
            truck_two.append(format(myHash.lookup(p)))

    elif run == 2:
        truck_one.clear()
        for p in package_list_three:
            temp = myHash.lookup(p)
            temp.status = 'en route'
            truck_one.append(format(myHash.lookup(p)))


# creates a list of all the distance between a start and end location
def getDistances(truck, start):

    if truck == 1:
        first_truck_distances[start] = {}
        for i in range(len(truck_one)):
            package = truck_one[i]
            # print(package)
            a = package.split(', ')
            address = a[1]
            # print(address)
            for key, value in AddressDict.items():
                if value == address:
                    end = key
                    distance = lookup_distance(start, end)
                    first_truck_distances[start][end] = distance

    elif truck == 2:
        second_truck_distances[start] = {}
        for i in range(len(truck_two)):
            package = truck_two[i]
            # print(package)
            a = package.split(', ')
            address = a[1]
            # print(address)
            for key, value in AddressDict.items():
                if value == address:
                    end = key
                    distance = lookup_distance(start, end)
                    second_truck_distances[start][end] = distance


# finds the minimum distance and the package associated with it
def getMinDistance(truck):
    new_start = -1
    new_end = -1
    min_dist = 10000
    package_id = -1
    if truck == 1:
        for a_id, a_info in first_truck_distances.items():
            start = a_id
            # print("\nStart Address:", start)
            for key in a_info:
                end = key
                distance = a_info[key]
                # print("End Address:", end, "->", distance)
                if distance < min_dist:
                    min_dist = distance
                    new_start = start
                    new_end = end

                    x = AddressDict[new_end]
                    for i in range(len(truck_one)):
                        package = truck_one[i]
                        a = package.split(', ')
                        id = a[0]
                        address = a[1]
                        if address == x:
                            package_id = id

    elif truck == 2:
        for a_id, a_info in second_truck_distances.items():
            start = a_id
            # print("\nStart Address:", start)
            for key in a_info:
                end = key
                distance = a_info[key]
                # print("End Address:", end, "->", distance)
                if distance < min_dist:
                    min_dist = distance
                    new_start = start
                    new_end = end

                    x = AddressDict[new_end]
                    for i in range(len(truck_two)):
                        package = truck_two[i]
                        a = package.split(', ')
                        id = a[0]
                        address = a[1]
                        if address == x:
                            package_id = id

    return new_start, new_end, min_dist, package_id


# returns the total distance traveled in miles
def getTotalDistance(truck):
    if truck == 1:
        total = 0
        for m in truck_one_min_dist:
            total += m
        return total
    elif truck == 2:
        total = 0
        for m in truck_two_min_dist:
            total += m
        return total


# get the current time of a truck
def getCurrentTime(truck):
    current_time = datetime.timedelta()
    if truck == 1:
        for i in first_truck_time:
            current_time += i
        print("Current Time:", str(current_time))
    elif truck == 2:
        for i in second_truck_time:
            current_time += i
        print("Current Time:", str(current_time))
    return current_time


# deliver the packages
def deliverTrucks(truck, start):  # nearest neighbor algorithm
    if truck == 1:
        count = len(truck_one)
        if count > 0:
            # get all the distances from the starting address
            new_start = int(start)
            # print('\nNew Start:', new_start)
            getDistances(1, new_start)

            # get the minimum distance address
            delivery = getMinDistance(1)
            start = delivery[0]
            end = delivery[1]
            distance = delivery[2]
            package_id = delivery[3]

            # Add the distance to the distance list for future total calculation
            truck_one_min_dist.append(distance)

            print("TRUCK DELIVERY:")
            print("Start:", start)
            print("End:", end)
            print("Distance:", distance)
            print("Package Id:", package_id)

            # get the current deliver time
            delivery_time = (distance / 18)
            time = datetime.timedelta(hours=delivery_time)
            # print('Time:', time)
            first_truck_time.append(time)  # adds delivery time to first_truck_time list
            current_time = getCurrentTime(1)  # total time

            # remove the package from the truck
            package_num = int(package_id)
            # print("Package_Number:", package_num)
            p = myHash.lookup(package_num)
            # print("Truck_one:", truck_one)
            # print("Removable Package:")
            # print(p)
            truck_one.remove(str(p))

            # update the package record with the delivery time
            temp = myHash.lookup(package_num)
            temp.timestamp = current_time
            temp.status = 'Delivered'
            # print("New package record in hash table:")
            # print(myHash.lookup(package_num))

            first_truck_distances.clear()
            deliverTrucks(1, end)
        else:  # gets the distance and time back to the hub
            distance_to_hub = lookup_distance(start, 0)
            truck_one_min_dist.append(distance_to_hub)
            delivery_time = (distance_to_hub / 18)
            time = datetime.timedelta(hours=delivery_time)
            first_truck_time.append(time)  # adds delivery time to first_truck_time list
            print('*************************************************')

    elif truck == 2:
        count = len(truck_two)
        if count > 0:
            # get the all the distances from the starting address
            new_start = int(start)
            # print('\nNew Start:', new_start)
            getDistances(2, new_start)

            # get the minimum distance address
            delivery = getMinDistance(2)
            start = delivery[0]
            end = delivery[1]
            distance = delivery[2]
            package_id = delivery[3]

            # Add the distance to the distance list for future total calculation
            truck_two_min_dist.append(distance)

            print("TRUCK DELIVERY:")
            print("Start:", start)
            print("End:", end)
            print("Distance:", distance)
            print("Package Id:", package_id)

            # get the current deliver time
            delivery_time = (distance / 18)
            time = datetime.timedelta(hours=delivery_time)
            # print('Time:', time)
            second_truck_time.append(time)  # adds delivery time to second_truck_time list
            current_time = getCurrentTime(2)  # total time

            # remove the package from the truck
            package_num = int(package_id)
            # print("Package_Number:", package_num)
            p = myHash.lookup(package_num)
            # print("Truck_two:", truck_two)
            # print("Removable Package:")
            # print(p)
            truck_two.remove(str(p))

            # update the package record with the delivery time
            temp = myHash.lookup(package_num)
            temp.timestamp = current_time
            temp.status = 'Delivered'
            # myHash.insert(end, temp)
            # print("New package record in hash table:")
            # print(myHash.lookup(package_num))

            second_truck_distances.clear()
            deliverTrucks(2, end)
        else:  # gets the distance and time back to the hub
            distance_to_hub = lookup_distance(start, 0)
            truck_two_min_dist.append(distance_to_hub)
            delivery_time = (distance_to_hub / 18)
            time = datetime.timedelta(hours=delivery_time)
            second_truck_time.append(time)  # adds delivery time to first_truck_time list
            print('*************************************************')


# function to be called in main.py to run the deliveries
def runDelivery():
    loadTrucks(1)

    deliverTrucks(1, 0)
    deliverTrucks(2, 0)

    loadTrucks(2)
    deliverTrucks(1, 0)

    # print('\nMin Distances:')
    # print(truck_one_min_dist)
    # print(truck_two_min_dist)
    # total = getTotalDistance(1) + getTotalDistance(2)
    # print("Total Distance Traveled:", round(total, 2), "miles")
