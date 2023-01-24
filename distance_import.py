import csv

# Distance Class

DistanceList = []


class Distance:
    def __init__(self, distance):
        self.distance = distance


def loadDistanceData(fileName):
    with open(fileName) as distances:
        distanceData = csv.reader(distances, delimiter=',')
        next(distanceData)  # skip header
        for distances in distanceData:
            DistanceList.append(distances)


def lookup_distance(start, end):
    distance = float(DistanceList[start][end])

    return distance


# Load distances to list
loadDistanceData('distance_file.csv')
