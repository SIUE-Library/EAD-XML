'''
Takes a txt file output from 
for file in <source>/*.tsv; do \cp -rf $file html.tsv; python getFirstWord.py; done
and edits it so it does not have any of the headers/footers:it will just have row after
row of box/folder:description data with the occasional header.  Juicy and tender.

for file in *.png ; do tesseract $file $file -c tosp_min_sane_kn_sp=8.5 tsv; done
to generate files for all pngs in current folder
'''

import re
def removeFooters(text):
	findURL = re.compile(r'.*[A-Z]:\\.*\n') #returns  and line that has a file location

	text = (re.sub(findURL, '', text))

	return text #no, YOU deal with this



def removeHeaders(text):
	findBlockA = re.compile('((UNIVERSITY)|(SIUE) ARCHIVES)(\n|.){1,750}Acc.{0,4}([A-Z][0-9]{1,2}:( )?[0-9]{1,2})', re.I)

	findBlockB = re.compile('((UNIVERSITY)|(SIUE) ARCHIVES)(\n|.){1,750}(Box\/Folder (Descri(p|g)tion|mm))', re.I) #returns any block going from SIUE ARCHIVES to B/F D

	#I used 2 blocks to ensure BOTH cases get got, because there is SIGNIFICANT overlap and I don't trust python's regex engine

	text = (re.sub(findBlockB, '', text))

	text = (re.sub(findBlockA, '', text))

	text = re.sub("\n\n \n\n","\n",text)
	return text #no, YOU deal with this

#MAIN
out = (removeHeaders(removeFooters(open("out.txt","r").read())))
open("out.txt","w").write(out)
