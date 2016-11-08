import numpy as np
import random as rand
import sys as sys

A = [0,29,82,46,68,52,72,42,51,55,29,74,23,72,46]
B = [29,0,55,46,42,43,43,23,23,31,41,51,11,52,21]
C = [82,55,0,68,46,55,23,43,41,29,79,21,64,31,51]
D = [46,46,68,0,82,15,72,31,62,42,21,51,51,43,64]
E = [68,42,46,82,0,74,23,52,21,46,82,58,46,65,23]
F = [52,43,55,15,74,0,61,23,55,31,33,37,51,29,59]
G = [72,43,23,72,23,61,0,42,23,31,77,37,51,46,33]
H = [42,23,43,31,52,23,42,0,33,15,37,33,33,31,37]
I = [51,23,41,62,21,55,23,33,0,29,62,46,29,51,11]
J = [55,31,29,42,46,31,31,15,29,0,51,21,41,23,37]
K = [29,41,79,21,82,33,77,37,62,51,0,65,42,59,61]
L = [74,51,21,51,58,37,37,33,46,21,65,0,61,11,55]
M = [23,11,64,51,46,51,51,33,29,41,42,61,0,62,23]
N = [72,52,31,43,65,29,46,31,51,23,59,11,62,0,59]
O = [46,21,51,64,23,59,33,37,11,37,61,55,23,59,0]

data = np.array([A,B,C,D,E,F,G,H,I,J,K,L,M,N,O])
travelledTo = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
route = []
cityToStart = rand.randint(0,14)

travelledTest = [True] * 10
print travelledTest

def getAllCities(input):
    cityList = []
    for (x,y),dist in input:
        if x not in cityList:
            cityList.append(x)
        if y not in cityList:
            cityList.append(y)
    return cityList




def ifAllVisited(booList):
    return reduce(lambda x,y:x&y, booList)

def minCity(subdata,index):
    minIndex = 0
    min = sys.maxint
    for city in range(0,len(subdata)):
        if(city==index):
            continue
        elif (subdata[city] < min):
            if(travelledTo[city]):
                continue
            else:
                minIndex = city
                min = subdata[city]
    route.append(minIndex)
    travelledTo[minIndex] = True
    return minIndex

