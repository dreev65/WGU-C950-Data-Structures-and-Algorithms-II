import csv


# Distance Class
class Distance:
    def __init__(self, distance):
        self.distance = distance

    """
    def loadDistanceData(fileName):
        with open(fileName) as distances:
            distanceData = csv.reader(distances, delimiter=',')
            next(distanceData)  # skip header
            for distances in distanceData:
    """


def getDistanceData():
    print("\nDistances:")


# Load addresses to list
# loadDistanceData('distance_file.csv')

# return addresses list
getDistanceData()
