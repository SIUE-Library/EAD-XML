'''
Looks at a hOCR file in TSV format and identifies any blank lines in the middle of the document
'''

import sys
import csv, io, json
convertedFile = open(sys.argv[1]+".txt", "a")

class Word:
	def __init__(self, top, left, word, width):
		self.top = top
		self.width = width
		self.left = left
		self.word = word

	def __lt__(self, other):
		if self.top+30 > other.top and self.top-30 < other.top:
			#then top is basically the same, sort by left
			return self.left < other.left
		else:
			#else top is different, return higher point
			return self.top < other.top

	def __str__(self):
		return self.word

class Line:
	def __init__(self, wordList, top):
		self.wordList = wordList
		self.top = top

	def __str__(self):
		out = ""
		for st in range(0, len(self.wordList)):

			if (self.wordList[st]).left - (self.wordList[st-1].left + self.wordList[st-1].width) > 10 :
				out += " "
			out += str(self.wordList[st])

		return out
def toint(input):
	if input == 'top' or input == 'left' or input == 'width':
		return 0
	else:
		return int(input)

tab = csv.DictReader(io.StringIO(open("html.tsv", "r").read()), delimiter="\t")

listOfWords = []

with open('html.tsv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
	for row in spamreader:
		if row[10] != "-1":
			listOfWords.append( Word( toint(row[7]), toint(row[6]), row[11], toint(row[8]) ) )

listOfWords = sorted(listOfWords)

allLines = [] #line array
thisLine = [] #list of Words that we collect then add to our Line array

for w in listOfWords:
	if len(thisLine) == 0:
		thisLine.append(w)
	else:
		if thisLine[0].top+30 > w.top and thisLine[0].top-30 < w.top:
			thisLine.append(w)
		else:
			#that line is over
			allLines.append( Line(thisLine, thisLine[0].top) )
			thisLine = []
			thisLine.append(w)

for i in range(1, len(allLines)):
	if(allLines[i].top - allLines[i-1].top > 85):
		convertedFile.write("\n")
	convertedFile.write(str(allLines[i])+"\n")



