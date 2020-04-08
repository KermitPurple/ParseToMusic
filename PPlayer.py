from winsound import Beep
from time import sleep
from frequencies import NotesDict

class PPlayer:

	mspb = 1000
	whole = mspb * 4
	half = mspb * 2
	quarter = mspb
	eighth = mspb / 2
	sixteenth = mspb / 4
	TimesDict = {
			"w": whole,
			"h": half,
			"q": quarter,
			"e": eighth,
			"s": sixteenth,
			}

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
					try:
						time = round(self.TimesDict[note[1]])
					except:
						raise SyntaxError("Could not read time of note")
				else:
					try:
						noteLetter = NotesDict[note[0]]
					except:
						raise SyntaxError("Could not read letter of note")
					try:
						octive = int(note[1])
					except:
						raise SyntaxError("Could not read octive of note")
					try:
						time = round(self.TimesDict[note[2]])
					except:
						raise SyntaxError("Could not read time of note")
				if not rest:
					Beep(round(noteLetter[octive]), time)
				else:
					sleep(time/1000)

