from winsound import Beep
from time import sleep
from frequencies import NotesDict

class PPlayer:

	mspb = 1500
	whole = mspb * 4
	half = mspb * 2
	quarter = mspb
	eighth = mspb / 2
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
	
	def play(self, loop=1):
		print("Playing " + self.file)
		for _ in range(0, loop):
			for note in self.list:
				rest = False
				if note[0] == 'r':
					rest = True
					time = round(self.getTime(note[1]))
				else:
					try:
						noteLetter = NotesDict[note[0]]
					except:
						raise SyntaxError("Could not read letter of note")
					try:
						octive = int(note[1])
					except:
						raise SyntaxError("Could not read octive of note")
					time = round(self.getTime(note[2]))
				if not rest:
					Beep(round(noteLetter[octive]), time)
				else:
					sleep(time/1000)


	def getTime(self, ch):
		if ch == 'w':
			return self.whole
		elif ch == 'h':
			return self.half
		elif ch == 'q':
			return self.quarter
		elif ch == 'e':
			return self.eighth
		elif ch == 's':
			return self.sixteenth
		raise SyntaxError("Could not read time of note")

