from hash_table import ChainingHashTable
import csv

# Package Class
class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.ID, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.status)


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

            # package object
            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pStatus)
            # print(p)

            # insert it into the hash table
            myHash.insert(pID, p)


# Hash table instance 
myHash = ChainingHashTable()

# Load packages to Hash Table
loadPackageData('package_file.csv')


def getPackageData():
    # Fetch data from Hash Table
    for i in range(len(myHash.table) + 1):
        print("Package: {}".format(myHash.search(i + 1)))  # 1 to 41 is sent to myHash.search()


# Return the package data
getPackageData()
