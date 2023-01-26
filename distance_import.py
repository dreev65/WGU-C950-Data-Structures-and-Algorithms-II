import csv

DistanceList = []


# Creates the Distance Class
class Distance:
    # Constructor for the Distance Class
    def __init__(self, distance):
        self.distance = distance


# loadDistanceData(filename) reads the distance_file.csv and creates distance objects that get added to the
# DistanceList. The objects are added to the list in each iteration of the for loop
def loadDistanceData(fileName):
    with open(fileName) as distances:
        distanceData = csv.reader(distances, delimiter=',')
        next(distanceData)  # skip header
        for distances in distanceData:
            DistanceList.append(distances)


# Allows for the searching of specific distances between two points by passing start and end parameters. Will look at
# the DistanceList and return the coordinate value at that position
def lookup_distance(start, end):
    distance = float(DistanceList[start][end])

    return distance


# Calls the loadDistanceData function and passes the distance_file.csv to be read from
loadDistanceData('distance_file.csv')
