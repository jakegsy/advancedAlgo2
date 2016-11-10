import numpy as np
import random as rand
import sys as sys


tryInput = [("Philly","Steak",10),
            ("Philly","Macs",3),
            ("Philly","KFC",4),
            ("Philly","BK",7),
            ("Steak","Philly",10),
            ("Steak","Macs",2),
            ("Steak","KFC",1),
            ("Steak","BK",8),
            ("Macs","Philly",3),
            ("Macs","Steak",2),
            ("Macs","KFC",5),
            ("Macs","BK",9),
            ("KFC","Philly",4),
            ("KFC","Steak",1),
            ("KFC","Macs",5),
            ("KFC","BK",3),
            ("BK","Philly",7),
            ("BK","Steak",8),
            ("BK","Macs",9),
            ("BK","KFC",3)]
#print len(tryInput)

def sanitizeInput(input):
    #Assuming format of (cityA,cityB), distance
    returnDict = {}
    for (cityA,cityB,distance) in input:
        if(not returnDict.has_key(cityA)):
            returnDict[cityA] = {}
        if(not returnDict.has_key(cityB)):
            returnDict[cityB] = {}
        returnDict[cityA][cityB] = distance
        returnDict[cityB][cityA] = distance
    return returnDict

#cleanedPut = (sanitizeInput(tryInput))
#print cleanedPut


def minCity(fromCity,dict, visited):
    cityDict = dict[fromCity]
    minCity = ""
    min = sys.maxint
    for city in cityDict.keys():
        if (city in visited):
            continue
        value = cityDict[city]
        if (value < min):
            minCity = city
            min = value
    if (min == sys.maxint):
        min = 0
    return (minCity,min)

#print minCity("KFC",cleanedPut,["Steak"])

def greedySalesman(input):
    dict = sanitizeInput(input)
    print dict
    visitedCity = []
    totalDist = 0
    #Assume starting from first city
    atCity = dict.keys()[4]
    while(len(visitedCity) < len(dict.keys())):
        nextCity,dist = minCity(atCity,dict,visitedCity)
        visitedCity.append(atCity)
        totalDist += dist
        atCity = nextCity

    return (visitedCity,totalDist)

print(greedySalesman(tryInput))