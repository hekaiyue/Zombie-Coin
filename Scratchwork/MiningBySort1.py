#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Galanta
#
# Created:     31/01/2014
# Copyright:   (c) Galanta 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

class AlteredSortelectionSort(object):
    def __init__(self):
        self.init()

    def init(self):
        self.walkCounter = 0
        self.difficulty = 1
        self.listSlice = 0 #This tells selectionSort where to start looking for
                           #the min value
        self.epsilon = 0
        self.makeList()

    def selectionSort(self):
        i = self.listSlice
        for j in xrange(self.listSlice,len(self.unsortedList)):
            if (self.unsortedList[j] < self.unsortedList[i]):
                i = j
        lowestN = self.unsortedList[i]
        firstN = self.unsortedList[self.listSlice]
        self.unsortedList[self.listSlice] = lowestN
        self.unsortedList[i] = firstN
        self.listSlice += 1

    def checkSort(self):
        if (self.unsortedList == self.sortedList):
            self.difficulty += 1
            self.listSlice = 0
            return True
        return False

    def makeList(self):
        self.unsortedList = []
        length = 10 * self.difficulty #length of list to be generated
        for x in xrange(length):
            self.unsortedList.append(random.randint(0,10))
        self.sortedList = sorted(self.unsortedList)
        print self.unsortedList
        print self.walkCounter

    def performIteration(self): #perform a step of sorting
        self.walkCounter += 1
        self.epsilon = 0.0002 * self.walkCounter if self.epsilon < 0.6 else 0.6
        print self.epsilon
        randomX = random.random()
        if (0 < randomX and randomX < (0.2 + self.epsilon)):
            self.selectionSort()



def testClassSort(n):
    A = AlteredSortelectionSort()
    counter = 0
    while(counter<n):
        if(A.checkSort()==True):
            A.makeList()
            counter += 1
        A.performIteration()
    print "done"





def main():
    pass

if __name__== '__main__':
    main()
    testClassSort(5)
