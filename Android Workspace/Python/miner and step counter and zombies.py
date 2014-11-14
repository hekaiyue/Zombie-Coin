import random
import math
import time




class GraphAnalyzer(object):
    def __init__(self):
        self.movingUp=True #whether the person is moving up or down
        self.threshold=0#at the beginning, there is no threshold to overcome
        self.alreadyNoted=False#does the program know the peak has been reached?
        self.miner=AlteredSortelectionSort()
        self.calibrator=[]
        self.speed = 0
        self.steps = 0
        self.currentTime = 0
        self.pastTime = 0
        self.zombieSpeed = 
        self.isZombieThere = False
        self.zombieEpsilon = 0.001
        self.zombieTime = 0

    def createZombie(self):
        self.isZombieThere = True
        self.zombieSpeed = 1.5 * self.speed
        self.zombieTime = time.time()

    def escapeZombie(self):
        self.isZombieThere = False
        self.zombieSpeed = 0
        self.zombieTime = 0

    def startAnalysis(self,graph):
        self.graph=graph
        if len(self.calibrator)<10:
            sum1=0
            for value in self.graph:
                sum1+=float(value)**2
            magnitude=sum1**0.5
            self.calibrator.append(magnitude)
        elif self.threshold==0:
            average=sum(self.calibrator)/float(len(self.calibrator))
            self.adjustGait(average)
        else:
            pass

    def adjustGait(self,average):
        minimumrate=0.8 #this is the fraction of your threshold at which you need to be performing at least
        self.threshold=(average)*minimumrate

    def checkZombie(self):
        if (self.speed > self.zombieSpeed):
            self.escapeZombie()
        elif (self.zombieTime - time.time()) > 10000:
            pass
            #lost coin here


    def detectStep(self, graph):
        if (len(self.calibrator)>=10):
            self.checkZombie()
            zombieRandom = random.random()
            self.zombieEpsilon += self.zombieEpsilon * 2
            if 0 < zombieRandom and zombieRandom < (0.001 + self.zombieEpsilon):
                #starts off slowly, but over time zombies come more often
                self.createZombie()
                #make the phone vibrate here
            if(self.steps == 0):
                self.startTimer()
            if (self.steps == 10):
                self.speed = self.steps / (time.time()-self.pastTime)
                self.steps = 0

            x1=float(self.graph[0])
            y1=float(self.graph[1])
            z1=float(self.graph[2])
            magnitude=(x1**2+y1**2+z1**2)**(0.5) #distance formula
            if magnitude>self.threshold and not self.alreadyNoted:
				self.runCalculation()
				self.alreadyNoted=True
        elif magnitude<self.threshold and self.alreadyNoted:
				self.alreadyNoted=False

    def startTimer(self):
        self.pastTime = time.time()

    def runCalculation(self):
        self.steps += 1
        self.miner.performIteration()

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
        print self.unsortedList
        for j in xrange(self.listSlice,len(self.unsortedList)):
            if (self.unsortedList[j] < self.unsortedList[i]):
                i = j
        lowestN = self.unsortedList[i]
        firstN = self.unsortedList[self.listSlice]
        self.unsortedList[self.listSlice] = lowestN
        self.unsortedList[i] = firstN
        self.listSlice += 1
        print self.unsortedList

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
        print self.unsortedList,self.walkCounter

    def performIteration(self): #perform a step of sorting
        self.walkCounter += 1
        self.epsilon = 0.0002 * self.walkCounter if self.epsilon < 0.6 else 0.6
        print self.epsilon,self.walkCounter
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
    #testClassSort(5)

x=[[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4],[1,2,3],[0,0,0],[-1,-1,-1],[1,2,3],[2,3,4]]
g=GraphAnalyzer()
for value in x:
	g.startAnalysis(value)
	g.detectStep()



