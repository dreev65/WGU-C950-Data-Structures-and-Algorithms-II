import datetime

from address_import import AddressDict
from distance_import import lookup_distance
from package_import import myHash

# Empty truck lists created
truck_one = []
truck_two = []

# Empty distance lists
first_truck_distances = []
second_truck_distances = []

# Times the trucks leave the hub
first_truck_time = ['09:05:00']
second_truck_time = ['10:30:00']

# Load truck one
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

# Load truck two
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


def deliverTruckOne():  # nearest neighbor algorithm
    print()
    address1 = list(AddressDict.keys())[0]
    min_dist = 1000000
    lowest_dist = 0
    for a in range(len(truck_one)):  # iterates through the truck list
        # compare the string address from the package to the address in AddressDict
        # pull the address id from AddressDict
        # use address id (pos) to get the distance between addresses to calculate shortest distance
        # check to see if correct min distance value is being calculated (Expecting 20 : 1.9)
        for key, val in AddressDict.items():  # finds the key based on value search for delivery address
            p = truck_one[a].split(', ')
            package_address = p[1]

            if val == package_address:  # pulls the id
                # print("Truck One Package Address:", package_address)
                # print('Position:', key)
                address2 = key
                distance_between = lookup_distance(address1, address2)

                # TODO: fix the loop for finding the minimum distance
                if min_dist > distance_between:
                    min_dist = distance_between
                    if distance_between > min_dist:
                        min_address = address2
                        print('\nAddress1:', address1, 'Address2:', address2)
                        print('Min Address:', min_address)
                        print("Min Distance:", min_dist)

                #     # TODO: 4) deliver the package (with timestamp) and remove it from the truck
                #     delivery_time = (min_dist / 18) * 60 * 60
                #     time = str(datetime.timedelta(seconds=delivery_time))
                #     first_truck_time.append(time)
                #     print("Delivery Times:", first_truck_time)


def deliverTruckTwo():  # nearest neighbor algorithm
    return


def getTotalTime():
    total_time = datetime.timedelta()
    for i in first_truck_time:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        total_time += d
    print(str(total_time))


def printTrucks():
    print("\nFirst Truck Deliveries:")
    for i in truck_one:
        print(i)

    # print("\nSecond Truck Deliveries:")
    # for i in truck_two:
    #     print(i)


printTrucks()
deliverTruckOne()
