import datetime
from package_import import myHash


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


print("\nFirst Truck Deliveries:")
for i in truck_one:
    print(i)

print("\nSecond Truck Deliveries:")
for i in truck_two:
    print(i)

