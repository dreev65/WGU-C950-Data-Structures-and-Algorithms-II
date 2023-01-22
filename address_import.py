import csv

AddressDict = {}


# Address Class
class Address:

    def __init__(self, ID, address):
        self.ID = ID
        self.address = address

    def __str__(self):  # overwrite print(Address) otherwise it will print object reference
        return "%s, %s" % (self.ID, self.address)


def loadAddressData(fileName):
    with open(fileName) as addresses:
        addressData = csv.reader(addresses, delimiter=',')
        next(addressData)  # skip header
        for address in addressData:
            aID = int(address[0])
            aAddress = address[1]

            AddressDict[aID] = aAddress


# Load addresses to list
loadAddressData('address_file.csv')


