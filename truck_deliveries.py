import datetime

from address_import import AddressDict
from distance_import import lookup_distance
from package_import import myHash

# create truck numbers
truck1 = 1
truck2 = 2

# Empty truck lists created
truck_one = []
truck_two = []

# Empty distance lists
first_truck_distances = {}
second_truck_distances = {}

# Times the trucks leave the hub
first_truck_time = ['08:00:00']
second_truck_time = ['10:30:00']

# package lists
package_list_one = [1, 6, 13, 14, 15, 16, 19, 20, 25, 29, 30, 31, 34, 37, 40]
package_list_two = [2, 3, 4, 5, 7, 8, 10, 11, 12, 17, 18, 22, 24, 36, 38]
package_list_three = [9, 21, 23, 26, 27, 28, 32, 33, 35, 39]


# Load trucks with packages and update status to 'en route'
def loadTrucks(run):
    if run == 1:
        for p in package_list_one:
            temp = myHash.lookup(p)
            temp.status = 'en route'
            myHash.insert(p, temp)
            truck_one.append(format(myHash.lookup(p)))

        for p in package_list_two:
            temp = myHash.lookup(p)
            temp.status = 'en route'
            myHash.insert(p, temp)
            truck_two.append(format(myHash.lookup(p)))

    elif run == 2:
        for p in package_list_three:
            temp = myHash.lookup(p)
            temp.status = 'en route'
            myHash.insert(p, temp)
            truck_one.append(format(myHash.lookup(p)))


# creates a list of all the distance between a start and end location
def getDistances(start):
    # print("\ngetDistances Packages:")
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
    print("\nFirst Truck Distances:", first_truck_distances)


# finds the minimum distance and the package associated with it
def getMinDistance():
    new_start = -1
    new_end = -1
    min_dist = 10000
    package_id = -1
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

    # print("\nMin_Dist:", min_dist)
    # print("Start:", new_start)
    # print("End:", new_end)
    # print("Package Id:", package_id)
    return new_start, new_end, min_dist, package_id


# returns the total distance traveled in miles
def getTotalDistance():
    for d in first_truck_distances:
        total = 0
        total = d + total
        return total


# get the current time of a truck
def getCurrentTime(truck):
    current_time = datetime.timedelta()
    if truck == 1:
        for i in first_truck_time:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            current_time += d
        print(str(current_time))
    elif truck == 2:
        for i in second_truck_time:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            current_time += d
        print(str(current_time))
    return current_time


# deliver the packages
def deliverTrucks(truck, start):  # nearest neighbor algorithm
    if truck == 1:
        # get the all the distances from the starting address
        new_start = int(start)
        print('\nNew Start:', new_start)
        getDistances(new_start)

        # get the minimum distance address
        delivery = getMinDistance()
        start = delivery[0]
        end = delivery[1]
        distance = delivery[2]
        package_id = delivery[3]
        print("TRUCK DELIVERY:")
        print("Start:", start)
        print("End:", end)
        print("Distance:", distance)
        print("Package Id:", package_id)

        # get the current deliver time
        delivery_time = (distance / 18) * 60 * 60
        time = str(datetime.timedelta(seconds=delivery_time))
        first_truck_time.append(time)  # adds delivery time to first_truck_time list
        print("Delivery Times:", first_truck_time)  # list of truck_one delivery times
        current_time = getCurrentTime(1)  # total time

        # remove the package from the truck
        package_num = int(package_id)
        print("Package_Number:", package_num)
        p = str(myHash.lookup(package_num))
        print("Truck_one:", truck_one)
        print("Removable Package:")
        print(p)
        truck_one.remove(p)

        # update the package record with the delivery time
        temp = myHash.lookup(package_num)
        temp.timestamp = current_time
        temp.status = 'Delivered'
        myHash.insert(end, temp)
        print("New package record in hash table:")
        print(myHash.lookup(end))

        first_truck_distances.clear()
        deliverTrucks(1, end)


loadTrucks(1)
print("\n-------------------------------------------------------------------------------------")
deliverTrucks(1, 0)
print("Total Distance Traveled for Truck One:", getTotalDistance())

# 20, 3595 Main St, Salt Lake City, UT, 84115, 10:30 AM, 37, en route, None
# temp = myHash.lookup(20)
# temp.status = 'en route'
# myHash.insert(20, temp)
# p = str(myHash.lookup(20))
# print("\nRemovable Package:")
# print(p)

#
# temp = myHash.lookup(20)
# temp.timestamp = '9:00:00'
# temp.status = 'Delivered'
# myHash.insert(20, temp)
# print("New package record in has table:")
# print(myHash.lookup(20))