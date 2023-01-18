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


# Load trucks with packages
def loadTrucks(run):
    if run == 1:
        truck_one.append(format(myHash.lookup(1)))
        truck_one.append(format(myHash.lookup(6)))
        truck_one.append(format(myHash.lookup(13)))
        truck_one.append(format(myHash.lookup(14)))
        truck_one.append(format(myHash.lookup(15)))
        truck_one.append(format(myHash.lookup(16)))
        truck_one.append(format(myHash.lookup(19)))
        truck_one.append(format(myHash.lookup(20)))
        truck_one.append(format(myHash.lookup(25)))
        truck_one.append(format(myHash.lookup(29)))
        truck_one.append(format(myHash.lookup(30)))
        truck_one.append(format(myHash.lookup(31)))
        truck_one.append(format(myHash.lookup(34)))
        truck_one.append(format(myHash.lookup(37)))
        truck_one.append(format(myHash.lookup(40)))

        truck_two.append(format(myHash.lookup(2)))
        truck_two.append(format(myHash.lookup(3)))
        truck_two.append(format(myHash.lookup(4)))
        truck_two.append(format(myHash.lookup(5)))
        truck_two.append(format(myHash.lookup(7)))
        truck_two.append(format(myHash.lookup(8)))
        truck_two.append(format(myHash.lookup(10)))
        truck_two.append(format(myHash.lookup(11)))
        truck_two.append(format(myHash.lookup(12)))
        truck_two.append(format(myHash.lookup(17)))
        truck_two.append(format(myHash.lookup(18)))
        truck_two.append(format(myHash.lookup(22)))
        truck_two.append(format(myHash.lookup(24)))
        truck_two.append(format(myHash.lookup(36)))
        truck_two.append(format(myHash.lookup(38)))

    elif run == 2:
        truck_one.append(format(myHash.lookup(9)))
        truck_one.append(format(myHash.lookup(21)))
        truck_one.append(format(myHash.lookup(23)))
        truck_one.append(format(myHash.lookup(26)))
        truck_one.append(format(myHash.lookup(27)))
        truck_one.append(format(myHash.lookup(28)))
        truck_one.append(format(myHash.lookup(32)))
        truck_one.append(format(myHash.lookup(33)))
        truck_one.append(format(myHash.lookup(35)))
        truck_one.append(format(myHash.lookup(39)))

    findDistance(1)
    findDistance(2)


# adds all the distances between each package into a list
def findDistance(truck):
    address1 = list(AddressDict.keys())[0]
    address2 = -1

    if truck == 1:
        for i in range(len(truck_one)):  # iterates through the truck list
            first_truck_distances[address1] = {}
            for key, val in AddressDict.items():  # finds the key based on value search for delivery address
                p = truck_one[i].split(', ')
                package_address = p[1]

                if val == package_address:  # pulls the id
                    print("Truck One Package Address:", package_address)
                    print('Position:', key)
                    address2 = key

                    # finds the distance between address1 and address2 and adds it to the dict
                    distance_between = lookup_distance(address1, address2)
                    first_truck_distances[][address2] = distance_between




    # elif truck == 2:
    #     for a in range(len(truck_two)):  # iterates through the truck list
    #
    #         for key, val in AddressDict.items():  # finds the key based on value search for delivery address
    #             p = truck_two[a].split(', ')
    #             package_address = p[1]
    #
    #             if val == package_address:  # pulls the id
    #                 # print("Truck Two Package Address:", package_address)
    #                 # print('Position:', key)
    #                 address2 = key
    #                 distance_between = lookup_distance(address1, address2)  # finds the distance between address1 and
    #                 # address2
    #                 second_truck_distances[address2] = distance_between


# get the current time of a truck
def getCurrentTime(truck):
    current_time = datetime.timedelta()
    if truck == 1:
        for i in first_truck_time:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            current_time += d
        print(str(current_time))
    elif truck ==2:
        for i in second_truck_time:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            current_time += d
        print(str(current_time))


# deliver the packages
def deliverTrucks():  # nearest neighbor algorithm

    loadTrucks(1)

    # if min_dist >= distance_between:
    #     min_dist = distance_between
    #     min_address = address2
    # print('Address1:', address1, 'Address2:', address2)
    # print('Min Address:', min_address)
    # print("Min Distance:", min_dist)

# TODO: 4) deliver the package (with timestamp) and remove it from the truck

    # delivery_time = (min_dist / 18) * 60 * 60
    # time = str(datetime.timedelta(seconds=delivery_time))
    # first_truck_time.append(time)
    # print("Delivery Times:", first_truck_time)


deliverTrucks()

# print(AddressDict)
#
# print("\nFirst Truck Packages:", truck_one)
# print("Second Truck Packages:", truck_two)

print("\nFirst Truck Distances:")
print(first_truck_distances)
# print("Second Truck Distances:", second_truck_distances)
