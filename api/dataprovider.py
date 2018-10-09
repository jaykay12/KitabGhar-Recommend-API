import MySQLdb
import dbconnections
import scipy.spatial
import numpy as np

dbCon = dbconnections.DBConnections()
cur = dbCon.getCursorObject()

class HashingFunctionality:
    def getHashUsers(self):
        hashUsers = {}
        reverseHashUsers = []
        query = "SELECT userid from users"
        cur.execute(query)

        for i,row in enumerate(cur.fetchall()):
            hashUsers[row[0]] = i
            reverseHashUsers.append(row[0])
        numUsers = len(hashUsers)
        print("Total Subscribers: {}".format(numUsers))

        return numUsers, hashUsers, reverseHashUsers

    def getHashBooks(self):
        hashBooks = {}
        reverseHashBooks = []
        query = "SELECT bookid from books"
        cur.execute(query)

        for i,row in enumerate(cur.fetchall()):
            hashBooks[row[0]] = i
            reverseHashBooks.append(row[0])
        numBooks = len(hashBooks)
        print("Total Books: {}".format(numBooks))

        return numBooks, hashBooks, reverseHashBooks


class DynamicRecommendations:
    def generateHashes(self):
        hashOBJ = HashingFunctionality()
        self.numUsers, self.hashUsers, self.reverseHashUsers = hashOBJ.getHashUsers()
        self.numBooks, self.hashBooks, self.reverseHashBooks = hashOBJ.getHashBooks()
        print("Done: Hashing!")

    def getDynamicRating(self):
        self.generateHashes()

        self.ratingData = []
        query = "SELECT userid,bookid,rating from reviews"
        cur.execute(query)

        for row in cur.fetchall():
            self.ratingData.append((self.hashUsers[row[0]], row[0], self.hashBooks[row[1]], row[1], row[2]))
        print("Done: Dynamic Rating Extracted from Database!")

    def getDataMatrix(self):
        self.dataMatrix = np.zeros((self.numUsers,self.numBooks))
        for entry in self.ratingData:
            self.dataMatrix[entry[0]][entry[2]] = entry[4]
              
        print("Done: Constructed Data Matrix!")

    def getSimilarityMatrix(self):
        itemSimilarityMatrix = np.zeros((self.numBooks,self.numBooks))
        for book1 in range(self.numBooks):
            for book2 in range(self.numBooks):
                if np.count_nonzero(self.dataMatrix[:, book1]) and np.count_nonzero(self.dataMatrix[:, book2]):
                    similarity_value = round((1 - scipy.spatial.distance.cosine(self.dataMatrix[:, book1], self.dataMatrix[:, book2])),3)
                    itemSimilarityMatrix[book1][book2] = similarity_value
                    
        print("Done: Constructed Similarity Matrix!")
        return itemSimilarityMatrix

