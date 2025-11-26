# Author: Matt Cummings
# Date: 11/25/2025
# Hash something out


import csv
import time

class DataItem:
    def __init__(self, line):
        self.title = line[0]
        self.genre = line[1]
        self.releaseDate = line[2]
        self.director = line[3]
        self.revenue = line[4]
        self.rating = line[5]
        self.minDuration = line[6]
        self.prodComp = line[7]
        self.quote = line[8]


def hashFunction(stringData):
    key = 0
    for i in range (len(stringData)):
        key = key + ord(stringData[i])
    key = key % 7
    return key

def hash2(stringData):
    key = 0 
    for i in range (len(stringData)):
        key = key + ord(stringData[i])
    key = 1+ (key % 5)
    return key 

# This function was acquired from the internet, specifically https://mojoauth.com/hashing/bernsteins-hash-djb2-in-python/
def djbHash(stringData):
    key = 5381
    for char in stringData:
        key = ((key << 5) + key) + ord(char)
    return key

start = time.time()
size = 15001
hashTitleTable = [None] * size
hashQuoteTable = [None] * size

file = "MOCK_DATA.csv"
counter = 0
titleCollisions = 0
quoteCollisions = 0

with open(file, 'r', newline='', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # create a DataItem from row
        if counter != 0:
            temp = DataItem(row)
        # feed appropriate field into the hashfunction to get a key
            titleKey = hashFunction(temp.title)
            quoteKey = hashFunction(temp.quote)
        # mod the key value by the hash table length
            titleLoc = titleKey % len(hashTitleTable)
            quoteLoc = quoteKey % len(hashQuoteTable)
        # try to insert DataItem into hash table
            if hashTitleTable[titleLoc] == None:
                hashTitleTable[titleLoc] = temp
        # handle any collisions
            else:
                titleCollisions += 1
                #hashTitleTable[titleLoc].next = Node(temp)
                hashNum = 0
                while hashTitleTable[titleLoc] != None:
                    hashNum +=1
                    newHash = (titleLoc + (hashNum * hash2(temp.title))) % len(hashTitleTable)
                    if hashTitleTable[newHash] == None:
                        hashTitleTable[newHash] = temp
                        break
                        
        # try to insert DataItem into Table
            if hashQuoteTable[quoteLoc] == None:
                hashQuoteTable[quoteLoc] = temp
            else:
        # handle any collisions
                quoteCollisions += 1
                #hashQuoteTable[quoteLoc].next = Node(temp)
                hashNum = 0
                while hashQuoteTable[quoteLoc] != None:
                    hashNum += 1
                    newHash = (quoteLoc + (hashNum * hash2(temp.quote))) % len(hashQuoteTable)
                    if hashQuoteTable[newHash] == None:
                        hashQuoteTable[newHash] = temp
                        break
        counter += 1
end = time.time()


print("Attempt 4")
print(f"Title table collisions: {titleCollisions}")
print(f"Quote table collisions: {quoteCollisions}")
titleEmptySpace = 0
quoteEmptySpace = 0
for i in range(len(hashTitleTable)-1):
    if hashTitleTable[i] == None:
        titleEmptySpace += 1
for i in range(len(hashQuoteTable)-1):
    if hashQuoteTable[i] == None:
        quoteEmptySpace += 1
print(f"Title table empty space: {titleEmptySpace}")
print(f"Quote table empty space: {quoteEmptySpace}")
print(f"Constructing both hash tables took {end-start:0.2f} seconds")