
import random
import hashlib  


def GetRandomStringArray():
    randomNumbers = random.sample(range(10000, 10000000), 10000)
    stringList = []
    for num in randomNumbers:
        stringList.append(str(num))
    return stringList

def HashArrayValues(someArray):
    hashedArray = []
    for clearString in someArray:
        hashedArray.append(hashlib.sha256(clearString.encode()).hexdigest())
    return hashedArray

def GenerateArrayAndHash():
    #get string array
    stringList = GetRandomStringArray()
    hashedValues = HashArrayValues(stringList)
    return hashedValues

def Drive(loopCount=10):
    for index in range(loopCount):
        randValuesList = GenerateArrayAndHash()
        randValuesList.sort()
        #print("loop complete : " + str(index))



