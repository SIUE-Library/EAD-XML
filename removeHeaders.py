'''
Takes a txt file output from 
for file in <source>/*.tsv; do \cp -rf $file html.tsv; python getFirstWord.py; done
and edits it so it does not have any of the headers/footers:it will just have row after
row of box/folder:description data with the occasional header.  Juicy and tender.

for file in *.png ; do tesseract $file $file -c tosp_min_sane_kn_sp=8.5 tsv; done
to generate files for all pngs in current folder
'''

import re, sys
def removeFooters(text):
	findURL = re.compile('^[A-Z]:.*$', re.M|re.I) #returns  and line that has a file location
	text = (re.sub(findURL, '', text))
	return text #no, YOU deal with this

def removeHeaders(text):
	findBlockA = re.compile('((UNIVERSITY)|(SIUE) ARCHIVES)(\n|.){1,750}Acc.{0,4}([A-Z]{0,1}[0-9]{1,2}:( )?[0-9]{1,2})', re.I)
	findBlockB = re.compile('((UNIVERSITY)|(SIUE) ?ARCHIVES)(\n|.){1,750}((Box\/Folder)|(m?) (Descri(p|g)tion|mm))', re.I) #returns any block going from SIUE ARCHIVES to B/F D

	#I used 2 blocks to ensure BOTH cases get got, because there is SIGNIFICANT overlap and I don't trust python's regex engine
	text = (re.sub(findBlockB, '', text))
	text = (re.sub(findBlockA, '', text))
	text = re.sub("\n\n \n\n","\n",text)
	text = re.sub("\n\n\n\n", "\n", text)
	print(text)
	return text #no, YOU deal with this

def convertText(text):
	#when there's an instance like "Apri15 this should be percieved as "April 5".
	#if we see a series of consecutive letters followed by a "1[0-9]*" replace with "l [0-9]*"
	#other instances include "C0."='Co.' and "L0ca1255"='Local 255'
	old = re.compile("[A-Z]{3,8}1[0-9]*", re.I)
	zero = re.compile("([A-Z]0)|0[A-Z]", re.I)
	#find all instaces of old pattern

	for match in re.findall(old, text):
		text = text.replace(match, match.replace("1", "l ", 1))

	return text

#MAIN
out = removeHeaders(open(sys.argv[1]+".txt","r").read())
out = removeFooters(out)
out = convertText(out)
open(sys.argv[1]+".txt","w").write(out)
