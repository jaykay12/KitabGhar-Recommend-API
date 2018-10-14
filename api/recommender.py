import MySQLdb
import dbconnections
import dataprovider
import numpy as np
from math import sqrt
import sys

dbCon = dbconnections.DBConnections()
cur = dbCon.getCursorObject()

class PopularityRecommenderSales:
    def firstElement(self, element):
        return element[0]

    def gatherSalesData(self):
        self.purchaseBooksCounter = []
        query = "SELECT bookid, count(*) from shelfs GROUP BY bookid"
        cur.execute(query)

        for row in cur.fetchall():
            self.purchaseBooksCounter.append((row[1],row[0]))

        self.purchaseBooksCounter.sort(reverse = True, key = self.firstElement)
        print("Done: Sales Data Gathered from Database!")

    def generateRecommendations(self):
        finalRecommendations = []
        for i,book in enumerate(self.purchaseBooksCounter):
            if i>5:
                break
            finalRecommendations.append(book[1])
        
        print("Generated: Popular Recommendations on Sales!")
        return finalRecommendations

    def getRecommendations(self):
        self.gatherSalesData()
        finalRecommendations = self.generateRecommendations()
        return finalRecommendations

class PopularityRecommenderRatings:
    def firstElement(self, element):
        return element[0]

    def gatherRatingsData(self):
        self.ratingCalculatorBooks = []
        query = "SELECT bookid, sum(rating), count(*) from reviews GROUP BY bookid"
        cur.execute(query)

        for row in cur.fetchall():
            normalizedRating = round((int(row[1])/int(row[2])),2)
            self.ratingCalculatorBooks.append((normalizedRating, row[0], row[2]))
            
        self.ratingCalculatorBooks.sort(reverse = True, key = self.firstElement)
        print("Done: Rating Data Gathering from Database!")

    def generateRecommendations(self):
        finalRecommendations = []
        for i,book in enumerate(self.ratingCalculatorBooks):
            if i>5:
                break
            finalRecommendations.append(book[1])

        print("Generated: Popular Recommendations on Ratings!")
        return finalRecommendations

    def getRecommendations(self):
        self.gatherRatingsData()
        finalRecommendations = self.generateRecommendations()
        return finalRecommendations

class ItemSimilarityRecommender:
    def secondElement(self, element):
            return element[1]

    def generateHashes(self):
        hashOBJ = dataprovider.HashingFunctionality()
        self.numUsers, self.hashUsers, self.reverseHashUsers = hashOBJ.getHashUsers()
        self.numBooks, self.hashBooks, self.reverseHashBooks = hashOBJ.getHashBooks()
        print("Done: Hashing!")

    def gatherPersonalisedData(self, userid):
        self.alreadyBooksRead = []
        query = "SELECT bookid from shelfs WHERE userid = '{uid}'".format(uid = userid)
        cur.execute(query)

        self.alreadyRecommended = {}

        for row in cur.fetchall():
            self.alreadyBooksRead.append(row[0])
            self.alreadyRecommended[row[0]] = True

        print("Done: Retrived Current Books of User!")
        print(self.alreadyBooksRead)
    
    def generateMatrices(self):
        self.generateHashes()
        retrieveOBJ = dataprovider.DynamicRecommendations()
        retrieveOBJ.getDynamicRating()
        retrieveOBJ.getDataMatrix()
        self.itemSimilarityMatrix = retrieveOBJ.getSimilarityMatrix()
        print("Generated: Matrices!")
                

    def generateRecommendations(self, userid):
        Totalrecommendations = []

        for book in self.alreadyBooksRead:
            for i,simValue in enumerate(self.itemSimilarityMatrix[self.hashBooks[book]]):
                Totalrecommendations.append((self.reverseHashBooks[i],float(simValue)))

        Totalrecommendations.sort(reverse = True, key=self.secondElement)

        finalRecommendations = []
        booksRecommenderCounter = 0
        for entry in Totalrecommendations:
            if booksRecommenderCounter>=18:
                break
                
            if entry[1] != 1 and entry[0] not in self.alreadyRecommended:
                finalRecommendations.append(entry[0])
                self.alreadyRecommended[entry[0]] = True
                booksRecommenderCounter += 1
                
        print("Generated: Item-Item Similarity Recommendations")
        return finalRecommendations

    def getRecommendations(self, userid):
        self.gatherPersonalisedData(userid)
        self.generateMatrices()
        finalRecommendations = self.generateRecommendations(userid)
        return finalRecommendations
