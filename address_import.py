import csv


# Address Class
class Address:
    AddressList = []

    def __init__(self, address):
        self.address = address

    def __str__(self):  # overwrite print(Address) otherwise it will print object reference
        return "%s" % self.address


def loadAddressData(fileName):
    with open(fileName) as addresses:
        addressData = csv.reader(addresses, delimiter=',')
        next(addressData)  # skip header
        for address in addressData:
            aAddress = address[0]

            Address.AddressList.append(aAddress)


def getAddressData():
    print("\nAddresses:")

    for i in Address.AddressList:
        print(i)


# Load addresses to list
loadAddressData('address_file.csv')

# return addresses list
getAddressData()
