'''
For every pdf of a finding aid in the ./pdf/ folder outputs
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

'''


#for each pdf	
	#convert to pages
	#for each page
		#for each line
			#if line fits regex
				#

import pyslibtesseract

tesseract_config = pyslibtesseract.TesseractConfig(psm=pyslibtesseract.PageSegMode.PSM_SINGLE_LINE, hocr=True)
print(pyslibtesseract.LibTesseract.simple_read(tesseract_config, '4-0.png'))
