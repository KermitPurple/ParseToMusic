from winsound import Beep
from frequencies import C, d, D, e, E, F, G, a, A, b, B

class PPlayer:

	mspb = 500
	whole = mspb * 4
	half = mspb * 2
	quarter = mspb
	eight = mspb / 2
	sixteenth = mspb / 4

	def __init__(self, FileToParse):
		self.file = FileToParse
		self.list = self.ParseToList()

	def ParseToList(self):
		wordList = []
		with open(self.file) as f:
			for line in f:
				wordList += line.split(" ")
		return wordList
	
		def play(self):
			for note in self.list:
				for ch in note:
					pass
