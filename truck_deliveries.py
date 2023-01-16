import datetime
from package_import import myHash
# from distance_import import DistanceList, lookup_distance
from address_import import AddressList

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
    address1 = myHash.lookup(0)
    for a1 in range(len(truck_one)):  # iterates through the truck list
        p = truck_one[a1].split(',')
        package_address = p[1]

        # TODO: 1) find a way to compare the string address from the package to the address in AddressList
        # TODO: 2) find a way to pull the address id from AddressList
        # TODO: 3) use address id to get the distance between addresses to calculate shortest distance
        # TODO: 4) deliver the package (with timestamp) and remove it from the truck

        # pos = package_address in AddressList


        # print statements
        print("Truck One Package Address:", package_address)
        # print(pos)


    # delivery_time = distance / 18
    # time_obj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))


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
