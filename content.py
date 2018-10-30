'''
For out.txt outputs:
all box/folders with descriptions
Fields the JSON needs will be:
Title
Subject
Desc
Creator
Publisher
Date
Rights
Format
Language
Type
ID
Hashmap of Box/Folder->Description

The Hashmap is the difficult part as the rest can be lifted from omeka

I'm trying to distinguish between multi-line descriptions and headers

it is a new item if it matches the following regex:
^(\d+ ?\/ ?\d+) ?((—|-)\d+)?.*

note: add
-c tosp_min_sane_kn_sp=8.5
to tesseract to deal with random intraword spaces
'''

class folder():
	box = 0
	folder = 0
	desc = ""
	section = ""	#the bold header
	collection = ""

	def __init__(self, box, folder, dec, col):
		this.box = box
		this.folder = folder
		this.desc = dec
		this.collection = col


#for every line in out.txt there are 3 cases:
#it begins with #/# in which case this is a NEW item!
#else, it is blank.
#else, it is a header or continuation of a line
#	if the line above is blank, its a header
#	else its a continuation of a line

import re
pat = re.compile("^(\d+ ?\/ ?\d+) ?((—|-)\d+)?.*", re.M|re.I)
out = open("out.txt", "r")
last = ""
next = ""
flag = 0
items = []
cat = ""
for line in out:


	if len(re.findall(pat, line)) > 0:
		print(next)
		next = line[:-1]

	elif line != "\n" and line != " \n" and last != "\n" and last != " \n":
		next += line[:-1]
	elif line != "\n" and line != " \n" and (last == "\n" or last == " \n"):
		print(next)
		next = ""
		print('\n'+"**"+line[:-1]+"**", end='')

	last = line

print(next)

