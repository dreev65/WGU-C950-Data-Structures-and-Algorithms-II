from package_import import myHash

# Empty truck lists created
first_delivery = []
second_delivery = []

first_truck_distances = []
second_truck_distances = []

# Times the trucks leave the hub
first_leave_times = ['8:00:00']
third_leave_times = ['10:30:00']

first_delivery.append(myHash[0])
first_delivery.append(myHash[3])
first_delivery.append(myHash[7])

print("\nFirst Truck Deliveries:")
print(first_delivery)