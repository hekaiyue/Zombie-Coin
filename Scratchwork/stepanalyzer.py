class GraphAnalyzer(object):
	def __init__(self, graph):

		self.graph=graph #2d array of coordinates ex. [3,3,3]
		self.movingUp=True #whether the person is moving up or down
		self.threshold=0#at the beginning, there is no threshold to overcome
		self.alreadyNoted=False#does the program know the peak has been reached?
		self.miner=AlteredSortelectionSort()

	def adjustGait(self,high,low):
		minimumrate=0.8 #this is the fraction of your threshold at which you need to be performing at least
		#maximumrate=2
		self.threshold=(float(high)-float(low))*minimumrate
		#self.threshold2=(float(high)-float(low))*

	def detectStep(self):
		x1=float(self.graph[0])
		y1=float(self.graph[1])
		z1=float(self.graph[2])
		magnitude=(x1**2+y1**2+z1**2)**(0.5) #distance formula
		if magnitude>self.threshold and not self.alreadyNoted:
			runCalculation()
			self.alreadyNoted=True
		elif magnitude<self.threshold and self.alreadyNoted:
			self.alreadyNoted=False

	def runCalculation(self):
		self.miner.performIteration()
