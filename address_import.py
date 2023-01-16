import csv

vertex_list = []
AddressList = []


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

            a = Address(aID, aAddress)
            AddressList.insert(aID, a)


def getVertex():
    for i in AddressList:
        vertex = AddressList.index(i)
        vertex_list.append(vertex)

    print('\nVertex List (nodes):')
    print(vertex_list)

    return vertex_list


def getAddressData():
    print("\nAddresses:")

    for i in AddressList:
        print(i)


# Load addresses to list
loadAddressData('address_file.csv')

# return addresses list
getAddressData()
