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

\n(\d+ ?\/ ?\d+) ?((—|-)\d+)?.*

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


#for each pdf	
	#convert to pages
	#for each page
		#for each line
			#if line fits regex


import pyslibtesseract

tesseract_config = pyslibtesseract.TesseractConfig(psm=pyslibtesseract.PageSegMode.PSM_SINGLE_LINE, hocr=True)
print(pyslibtesseract.LibTesseract.simple_read(tesseract_config, '4-0.png'))

