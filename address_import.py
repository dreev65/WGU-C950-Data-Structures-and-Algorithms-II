import csv

AddressDict = {}


# Creates the Address Class
class Address:
    # Constructor for the Address Class
    def __init__(self, ID, address):
        self.ID = ID
        self.address = address

    # overwrite print(Address) otherwise it will print object reference
    def __str__(self):
        return "%s, %s" % (self.ID, self.address)


# loadAddressData(filename) reads the address_file.csv and creates address objects that get added to the AddressDict.
# The objects are added to the dictionary list as ID: Address values
def loadAddressData(fileName):
    with open(fileName) as addresses:
        addressData = csv.reader(addresses, delimiter=',')
        next(addressData)  # skip header
        for address in addressData:
            aID = int(address[0])
            aAddress = address[1]

            AddressDict[aID] = aAddress


# Calls the loadAddressData function and passes the address_file.csv to be read from
loadAddressData('address_file.csv')


