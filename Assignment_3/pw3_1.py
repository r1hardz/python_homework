import os
import re

os.chdir(os.path.dirname(__file__))

lowestCold = float('inf')
highestCold = float('-inf')
lowestColdName = ''
highestColdName = ''
coldRatingTotal = 0
coldRatingCount = 0

lowestHot = float('inf')
highestHot = float('-inf')
lowestHotName = ''
highestHotName = ''
hotRatingTotal = 0
hotRatingCount = 0

def getAverage(type):
    if (type == "C"):
        return coldRatingTotal / coldRatingCount
    elif (type == "H"):
        return hotRatingTotal / hotRatingCount

def printResults():
    print("Cereal type: Cold")
    print("The lowest cereals rating value: ", lowestCold, "Cereals name: ", lowestColdName)
    print("The highest cereals rating value: ", highestCold, "Cereals name: ", highestColdName)
    print("Average cereals rating value: ", getAverage("C"), '\n')
    print("Cereal type: Hot")
    print("The lowest cereals rating value", lowestHot, "Cereals name:", lowestHotName)
    print("The highest cereals rating value: ", highestHot, "Cereals name: ", highestHotName)
    print("Average cereals rating value: ", getAverage("H"))


filename = input("Enter file name: ")
with open(filename, 'r') as f:
    firstLine = f.readline()
    for line in f:
        
        nameIndex = line.index(',')+ 1
        while line[nameIndex] == "_":
            temp = line[nameIndex:-1]
            nameIndex = temp.index(',') + 1 + nameIndex
        temperature = line[nameIndex + 2]
        name = line[0:nameIndex - 1].replace('_', " ")
        rating = float(line[line.rindex('.') -2: -1])

        """temperature = re.findall(',([CH]), ', line)[0]
        brandName = re.findall('(.+?), [A-Z], ', line)[0].replace('_' ' ')  ### <==== REGEX
        rating = float(re.findall(', ([0-9.]+)$', line)[0])"""

        if (temperature == 'C'):
            coldRatingTotal += rating
            coldRatingCount += 1
            if (rating > highestCold):
                highestCold = rating
                highestColdName = name
            elif (rating < lowestCold):
                lowestCold = rating
                lowestColdName = name
            else:
                hotRatingTotal += rating
                hotRatingCount += 1
                if (rating > highestHot):
                    highestHot = rating
                    highestHotName = name
                elif (rating < lowestHot):
                    lowestHot = rating
                    lowestHotName = name
    printResults()
    f.close()

