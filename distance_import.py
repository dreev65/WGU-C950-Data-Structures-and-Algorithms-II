import csv

# Distance Class

DistanceList = []
distance_array = []


class Distance:
    def __init__(self, distance):
        self.distance = distance


def loadDistanceData(fileName):
    with open(fileName) as distances:
        distanceData = csv.reader(distances, delimiter=',')
        next(distanceData)  # skip header
        for distances in distanceData:
            DistanceList.append(distances)


def getDistanceData():
    print("\nDistances:")

    for i in DistanceList:
        print(i)


# Load distances to list
loadDistanceData('distance_file.csv')

# return addresses list
getDistanceData()


print("\nSpecific rows:")
print(DistanceList[5][1])
