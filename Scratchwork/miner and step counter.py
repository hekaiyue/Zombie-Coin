import random
import math






class GraphAnalyzer(object):
	def __init__(self):
		self.movingUp=True #whether the person is moving up or down
		self.threshold=0#at the beginning, there is no threshold to overcome
		self.alreadyNoted=False#does the program know the peak has been reached?
		self.miner=AlteredSortelectionSort()
		self.calibrator=[]

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
			print average
			self.adjustGait(average)
		else:
			pass

	def adjustGait(self,average):
		minimumrate=0.8 #this is the fraction of your threshold at which you need to be performing at least
		self.threshold=(average)*minimumrate
		print self.threshold

	def detectStep(self):
		if len(self.calibrator)>=10:
			x1=float(self.graph[0])
			y1=float(self.graph[1])
			z1=float(self.graph[2])
			magnitude=(x1**2+y1**2+z1**2)**(0.5) #distance formula
			if magnitude>self.threshold and not self.alreadyNoted:
				print magnitude
				self.runCalculation()
				self.alreadyNoted=True
			elif magnitude<self.threshold and self.alreadyNoted:
				self.alreadyNoted=False

	def runCalculation(self):
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



