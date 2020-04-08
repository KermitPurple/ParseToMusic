from winsound import Beep
from time import sleep
from frequencies import C, d, D, e, E, F, G, a, A, b, B

class PPlayer:

	mspb = 1000
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
	
	def play(self):
		print("Playing " + self.file)
		for note in self.list:
			rest = False
			if note[0] == 'r':
				rest = True
				time = round(self.getTime(note[1]))
			else:
				noteLetter = self.getNote(note[0])
				try:
					octive = int(note[1])
				except:
					raise SyntaxError("Could not read octive of note")
				time = round(self.getTime(note[2]))
			if not rest:
				Beep(round(noteLetter[octive]), time)
			else:
				sleep(time/1000)


	def getNote(self, ch):
		if ch == 'C':
			return C
		elif ch == 'd':
			return d
		elif ch == 'D':
			return D
		elif ch == 'e':
			return e
		elif ch == 'E':
			return E
		elif ch == 'F':
			return F
		elif ch == 'G':
			return G
		elif ch == 'a':
			return a
		elif ch == 'A':
			return A
		elif ch == 'b':
			return b
		elif ch == 'B':
			return B
		raise SyntaxError("Could not read letter of note")

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

