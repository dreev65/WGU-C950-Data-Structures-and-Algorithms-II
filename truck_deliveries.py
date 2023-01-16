import datetime
from package_import import myHash
from address_import import AddressDict
from distance_import import DistanceList, lookup_distance


# Empty truck lists created
truck_one = []
truck_two = []

# Empty distance lists
first_truck_distances = []
second_truck_distances = []

# Times the trucks leave the hub
first_leave_time = ['9:05:00']
second_leave_time = ['10:30:00']

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


def deliverTruckOne():
    print()
    address1 = list(AddressDict.keys())[0]
    min_dist = 1000000
    for a in range(len(truck_one)):  # iterates through the truck list

        # compare the string address from the package to the address in AddressDict
        # pull the address id from AddressDict
        for key, val in AddressDict.items():  # finds the key based on value search for delivery address
            p = truck_one[a].split(', ')
            package_address = p[1]

            if val == package_address:  # pulls the id
                print("Truck One Package Address:", package_address)
                print('Position:', key)

            # TODO: 3) use address id (pos) to get the distance between addresses to calculate shortest distance
            # TODO: check to see if correct min distance value is being calculated
            address2 = key
            distance = lookup_distance(address1, address2)
            if min_dist > distance:
                min_dist = distance

            address1 = address2


        # TODO: 4) deliver the package (with timestamp) and remove it from the truck
        # delivery_time = distance / 18
        # time_obj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    print('Min Distance:', min_dist)
    print('New Address:', address2)

def deliverTruckTwo():
    return


def printTrucks():
    print("\nFirst Truck Deliveries:")
    for i in truck_one:
        print(i)

    # print("\nSecond Truck Deliveries:")
    # for i in truck_two:
    #     print(i)


printTrucks()
deliverTruckOne()
