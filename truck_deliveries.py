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

# Adds the delivery start time to the truck time list
first_truck_time = []
x = datetime.timedelta(hours=8)
first_truck_time.append(x)

second_truck_time = []
x = datetime.timedelta(hours=9.5)
second_truck_time.append(x)

# Creates an empty list for second run start time of truck one
run_two_start = []

# Manually loads package lists
package_list_one = [1, 5, 7, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]  # truck one
package_list_two = [2, 3, 4, 6, 8, 10, 11, 12, 17, 18, 22, 24, 25, 36, 38]  # truck two
package_list_three = [9, 21, 23, 26, 27, 28, 32, 33, 35, 39]  # truck one run two


# Updates the status and timestamp of the package object for each package as it gets loaded to the trucks
# Space-Time Complexity -> O(n^2)
def loadTrucks(run):
    if run == 1:
        for p in package_list_one:
            temp = myHash.lookup(p)
            temp.status = 'en route'
            temp.timestamp = '8:00:00'
            truck_one.append(format(myHash.lookup(p)))

        for p in package_list_two:
            temp = myHash.lookup(p)
            temp.status = 'en route'
            temp.timestamp = '9:30:00'
            truck_two.append(format(myHash.lookup(p)))

    elif run == 2:
        truck_one.clear()
        for p in package_list_three:
            temp = myHash.lookup(p)
            temp.status = 'en route'
            temp.timestamp = ''

            # changes the address of package 9, so it can be treated as a delayed package
            if p == package_list_three[0]:
                temp.address = '410 S State St'
                temp.zipcode = '84111'

            truck_one.append(format(myHash.lookup(p)))


# creates a list of all the distance between a start and end location
# Space-Time Complexity -> O(n^2)
def getDistances(truck, start):

    if truck == 1:
        first_truck_distances[start] = {}  # creates empty truck distances list
        # iterates through the truck packages and determines the street address of each package
        for i in range(len(truck_one)):
            package = truck_one[i]
            a = package.split(', ')
            address = a[1]
            # finds the end address and the distance from the start to end address
            for key, value in AddressDict.items():
                if value == address:
                    end = key
                    distance = lookup_distance(start, end)
                    first_truck_distances[start][end] = distance

    elif truck == 2:
        second_truck_distances[start] = {}  # creates empty truck distances list
        # iterates through the truck packages and determines the street address of each package
        for i in range(len(truck_two)):
            package = truck_two[i]
            a = package.split(', ')
            address = a[1]
            # finds the end address and the distance from the start to end address
            for key, value in AddressDict.items():
                if value == address:
                    end = key
                    distance = lookup_distance(start, end)
                    second_truck_distances[start][end] = distance


# finds the minimum distance and the package associated with it
# Space-Time Complexity -> O(n^2)
def getMinDistance(truck):
    new_start = -1
    new_end = -1
    min_dist = 10000
    package_id = -1
    if truck == 1:
        # sets the start address
        for a_id, a_info in first_truck_distances.items():
            start = a_id

            # sets the end address and distance
            for key in a_info:
                end = key
                distance = a_info[key]

                # determines if the new distance is less than the min_dist and sets it as the new min_dist
                if distance < min_dist:
                    min_dist = distance
                    new_start = start
                    new_end = end

                    # sets the package id of the min_address
                    x = AddressDict[new_end]
                    for i in range(len(truck_one)):
                        package = truck_one[i]
                        a = package.split(', ')
                        id = a[0]
                        address = a[1]
                        if address == x:
                            package_id = id

    elif truck == 2:
        # sets the start address
        for a_id, a_info in second_truck_distances.items():
            start = a_id

            # sets the end address and distance
            for key in a_info:
                end = key
                distance = a_info[key]

                # determines if the new distance is less than the min_dist and sets it as the new min_dist
                if distance < min_dist:
                    min_dist = distance
                    new_start = start
                    new_end = end

                    # sets the package id of the min_address
                    x = AddressDict[new_end]
                    for i in range(len(truck_two)):
                        package = truck_two[i]
                        a = package.split(', ')
                        id = a[0]
                        address = a[1]
                        if address == x:
                            package_id = id

    return new_start, new_end, min_dist, package_id


# returns the total distance traveled in miles for each truck
# Space-Time Complexity -> O(n)
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
# Space-Time Complexity -> O(n)
def getCurrentTime(truck):
    current_time = datetime.timedelta()
    if truck == 1:
        for i in first_truck_time:
            current_time += i
    elif truck == 2:
        for i in second_truck_time:
            current_time += i
    return current_time


# deliver the packages using a nearest neighbor algorithm
# Space-Time Complexity -> O(n^2)
def deliverTrucks(truck, start):
    if truck == 1:
        count = len(truck_one)  # sets the count to the number of list items in truck_one
        if count > 0:
            # get all the distances from the starting address
            new_start = int(start)
            getDistances(1, new_start)

            # get the minimum distance address
            delivery = getMinDistance(1)
            start = delivery[0]
            end = delivery[1]
            distance = delivery[2]
            package_id = delivery[3]

            # Add the distance to the distance list for future total calculation
            truck_one_min_dist.append(distance)

            # get the current deliver time
            delivery_time = (distance / 18)
            time = datetime.timedelta(hours=delivery_time)
            first_truck_time.append(time)  # adds delivery time to first_truck_time list
            current_time = getCurrentTime(1)  # total time

            # remove the package from the truck
            package_num = int(package_id)
            p = myHash.lookup(package_num)
            truck_one.remove(str(p))

            # update the package record with the delivery time
            temp = myHash.lookup(package_num)
            temp.timestamp = current_time
            temp.status = 'Delivered'

            # clear the truck distance list and recursively call deliverTrucks()
            first_truck_distances.clear()
            deliverTrucks(1, end)

        else:  # gets the distance and time back to the hub
            distance_to_hub = lookup_distance(start, 0)
            truck_one_min_dist.append(distance_to_hub)
            delivery_time = (distance_to_hub / 18)
            time = datetime.timedelta(hours=delivery_time)
            first_truck_time.append(time)  # adds delivery time to first_truck_time list

            # Add the final time for the first delivery (hub to hub) to the run_two_start list
            # Used by main.py to find the status of the package based on the users input time
            run_two_start.append(getCurrentTime(1))

    elif truck == 2:
        count = len(truck_two)  # sets the count to the number of list items in truck_two
        if count > 0:
            # get the all the distances from the starting address
            new_start = int(start)
            getDistances(2, new_start)

            # get the minimum distance address
            delivery = getMinDistance(2)
            start = delivery[0]
            end = delivery[1]
            distance = delivery[2]
            package_id = delivery[3]

            # Add the distance to the distance list for future total calculation
            truck_two_min_dist.append(distance)

            # get the current deliver time
            delivery_time = (distance / 18)
            time = datetime.timedelta(hours=delivery_time)
            second_truck_time.append(time)  # adds delivery time to second_truck_time list
            current_time = getCurrentTime(2)  # total time

            # remove the package from the truck
            package_num = int(package_id)
            p = myHash.lookup(package_num)
            truck_two.remove(str(p))

            # update the package record with the delivery time
            temp = myHash.lookup(package_num)
            temp.timestamp = current_time
            temp.status = 'Delivered'

            # clear the truck distance list and recursively call deliverTrucks()
            second_truck_distances.clear()
            deliverTrucks(2, end)

        else:  # gets the distance and time back to the hub
            distance_to_hub = lookup_distance(start, 0)
            truck_two_min_dist.append(distance_to_hub)
            delivery_time = (distance_to_hub / 18)
            time = datetime.timedelta(hours=delivery_time)
            second_truck_time.append(time)  # adds delivery time to first_truck_time list


# Function to be called in main.py to run the deliveries
def runDelivery():
    loadTrucks(1)  # loads the first run on truck one and two
    deliverTrucks(1, 0)  # delivers truck one
    deliverTrucks(2, 0)  # delivers truck two
    loadTrucks(2)  # loads the second run of truck one
    deliverTrucks(1, 0)  # delivers the second run of truck one
