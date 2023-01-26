import csv

from hash_table import ChainingHashTable


# Creates the Package Class
class Package:
    # Constructor for the Package Class
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, status, timestamp):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.timestamp = timestamp

    # overwrite print(Package) otherwise it will print object reference
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.ID, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.status,
            self.timestamp)


# loadPackageData(filename) reads the package_file.csv and creates package objects that get added to the
# hash table. The objects are added to the hash table in each iteration of the for loop
def loadPackageData(fileName):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)  # skip header
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pStatus = "AtHub"
            pTimestamp = "None"

            # package object
            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pStatus, pTimestamp)

            # insert it into the hash table
            myHash.insert(pID, p)


# Calls the ChainingHashTable function
myHash = ChainingHashTable()

# Calls the loadPackageData function and passes the package_file.csv to be read from
loadPackageData('package_file.csv')
